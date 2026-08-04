#!/usr/bin/env python3
"""Build a Google Merchant Center product feed from a live WooCommerce store.

Reads the public Store API — the same data Google's crawler can see — and emits
a Merchant Center feed plus a validation report.

Design decisions that matter for approval:

  * `id` uses the SKU where one exists, otherwise the WooCommerce product id.
    Never invented, always unique, always stable.
  * `gtin`/`mpn` are emitted ONLY where a real identifier exists. Where none does,
    `identifier_exists` is set to `no` rather than fabricating a code. For
    unbranded goods that is the correct and honest declaration.
  * `brand` comes only from an assigned brand term. No inference.
  * `price` is emitted gross (VAT-inclusive), which is what German B2C law requires
    and what the landing page shows — feed and page must agree.
  * `condition` is read from the store's condition attribute, not assumed.
  * `shipping` carries the real flat rate so Merchant Center and checkout agree.

Usage:
    python3 build-feed.py https://example.com --out feed.xml --country DE --currency EUR
    python3 build-feed.py https://example.com --format tsv --out feed.tsv
"""

from __future__ import annotations

import argparse
import html
import json
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from typing import Any
from xml.sax.saxutils import escape

UA = "Mozilla/5.0 (compatible; MerchantFeedBuilder/1.0)"
TIMEOUT = 60

# Attributes Merchant Center requires for every item.
REQUIRED = ["id", "title", "description", "link", "image_link", "availability",
            "price", "condition"]


def fetch(url: str) -> Any:
    try:
        url.encode("ascii")
    except UnicodeEncodeError:
        s = urllib.parse.urlsplit(url)
        url = urllib.parse.urlunsplit((
            s.scheme, s.netloc.encode("idna").decode("ascii"),
            urllib.parse.quote(s.path, safe="/%"),
            urllib.parse.quote(s.query, safe="=&%"), s.fragment))
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def clean_text(raw: str, limit: int) -> str:
    """Strip markup and entities; Merchant Center wants plain text."""
    t = re.sub(r"<(script|style)\b.*?</\1>", " ", raw or "", flags=re.S | re.I)
    t = re.sub(r"<li[^>]*>", " • ", t, flags=re.I)
    t = re.sub(r"</(p|h[1-6]|ul|ol|div|tr)>", "\n", t, flags=re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t ]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t).strip()
    return t[:limit].rstrip()


# Store category slug -> Google product taxonomy path. Full paths are used rather
# than numeric ids because a mistyped id silently mis-categorises, whereas a wrong
# path is rejected at upload and can be corrected. Verify against Google's current
# taxonomy file before submitting.
GOOGLE_CATEGORY = {
    "lagercontainer":     "Business & Industrial > Material Handling > Shipping Containers",
    "werkstattcontainer": "Business & Industrial > Material Handling > Shipping Containers",
    "wohncontainer":      "Business & Industrial > Material Handling > Shipping Containers",
    "sanitarcontainer":   "Business & Industrial > Material Handling > Shipping Containers",
    "poolcontainer":      "Home & Garden > Pool & Spa > Swimming Pools",
    "poolroboter":        "Home & Garden > Pool & Spa > Pool & Spa Accessories",
    "klimaanlage":        "Home & Garden > Household Appliances > Climate Control Appliances > Air Conditioners",
    "anhanger":           "Vehicles & Parts > Vehicle Parts & Accessories > Vehicle Towing > Towing Trailers",
    "pferdeanhanger":     "Vehicles & Parts > Vehicle Parts & Accessories > Vehicle Towing > Towing Trailers",
    "bootsanhanger":      "Vehicles & Parts > Vehicle Parts & Accessories > Vehicle Towing > Towing Trailers",
}


def google_category(product: dict) -> str:
    """Most specific mapped category wins; unmapped returns empty rather than a guess."""
    slugs = [c.get("slug", "") for c in (product.get("categories") or [])]
    for s in slugs:
        if s in GOOGLE_CATEGORY:
            return GOOGLE_CATEGORY[s]
    return ""


def condition_of(product: dict) -> str | None:
    """Read condition from the store's own attribute rather than assuming."""
    mapping = {"neu": "new", "new": "new",
               "gebraucht": "used", "used": "used",
               "generalüberholt": "refurbished", "refurbished": "refurbished"}
    for attr in product.get("attributes") or []:
        name = ((attr.get("taxonomy") or attr.get("name") or "")).lower()
        if "condition" in name or "zustand" in name:
            for term in attr.get("terms") or []:
                v = (term.get("name") or "").strip().lower()
                if v in mapping:
                    return mapping[v]
    return None


def build(base: str, country: str, currency: str, shipping_cost: str | None,
          max_products: int,
          reference_prices_verified: bool = False) -> tuple[list[dict], list[str]]:
    items: list[dict] = []
    notes: list[str] = []
    unsubstantiated: list[tuple[str, float, float]] = []
    page = 1
    raw: list[dict] = []
    while len(raw) < max_products:
        batch = fetch(f"{base}/wp-json/wc/store/v1/products?per_page=100&page={page}")
        if not isinstance(batch, list) or not batch:
            break
        raw += batch
        if len(batch) < 100:
            break
        page += 1

    seen_ids: Counter = Counter()
    for p in raw:
        prices = p.get("prices") or {}
        minor = int(prices.get("currency_minor_unit", 2) or 2)
        price_major = int(prices.get("price") or 0) / (10 ** minor)
        regular = int(prices.get("regular_price") or 0) / (10 ** minor)

        sku = (p.get("sku") or "").strip()
        item_id = sku or str(p["id"])
        seen_ids[item_id] += 1

        brands = [b.get("name") for b in (p.get("brands") or []) if b.get("name")]
        brand = brands[0] if brands else None

        images = p.get("images") or []
        cond = condition_of(p)

        item = {
            "id": item_id,
            "title": clean_text(p.get("name", ""), 150),
            "description": clean_text(p.get("description") or p.get("short_description") or "", 5000),
            "link": p.get("permalink", ""),
            "image_link": images[0]["src"] if images else "",
            "additional_image_link": [i["src"] for i in images[1:11]],
            "availability": "in_stock" if p.get("is_in_stock") else "out_of_stock",
            "price": f"{price_major:.2f} {prices.get('currency_code') or currency}",
            "condition": cond or "",
            "brand": brand or "",
            "google_product_category": google_category(p),
            "product_type": " > ".join(c["name"] for c in (p.get("categories") or [])[:3]),
            "identifier_exists": "",
            "gtin": "",
            "mpn": "",
        }

        # A sale price is a CLAIM: that the reference price was really charged before.
        #
        # WooCommerce having a higher regular_price does not substantiate that. Under
        # PAngV §11 (Germany, implementing EU 98/6/EC Art. 6a) an advertised reduction
        # must state the lowest price the trader applied in the preceding 30 days, and
        # Google treats an unsubstantiated strikethrough as misrepresentation.
        #
        # So the reference price has to be verified out-of-band by someone who knows
        # the shop's price history. Until it is, the feed carries the price the
        # customer actually pays and makes no reduction claim at all — which is always
        # true, and never a policy risk.
        if p.get("on_sale") and regular > price_major > 0:
            if reference_prices_verified:
                item["price"] = f"{regular:.2f} {prices.get('currency_code') or currency}"
                item["sale_price"] = f"{price_major:.2f} {prices.get('currency_code') or currency}"
            else:
                unsubstantiated.append((item_id, regular, price_major))

        # No GTIN or MPN is available from the store. Declaring identifier_exists=no
        # is the honest option; inventing a code is a policy violation.
        if not item["gtin"] and not item["mpn"]:
            item["identifier_exists"] = "no"

        if shipping_cost:
            item["shipping"] = f"{country}:::{shipping_cost} {currency}"

        items.append(item)

    dupes = [i for i, c in seen_ids.items() if c > 1]
    if dupes:
        notes.append(f"DUPLICATE ids: {len(dupes)} — {dupes[:5]}")
    if unsubstantiated:
        worst = max(100 * (r - s) / r for _, r, s in unsubstantiated)
        notes.append(
            f"SALE PRICES WITHHELD: {len(unsubstantiated)} product(s) have a higher "
            f"regular_price in WooCommerce (up to {worst:.1f}% apparent reduction), but "
            f"nothing substantiates that it was ever charged. The feed carries the actual "
            f"selling price and makes no reduction claim. Pass --reference-prices-verified "
            f"once the 30-day price history is confirmed (PAngV §11).")
    return items, notes


def validate(items: list[dict]) -> list[tuple[str, str, int]]:
    findings = []
    def add(sev, msg, n): findings.append((sev, msg, n))

    for field in REQUIRED:
        missing = [i for i in items if not str(i.get(field, "")).strip()]
        if missing:
            sev = "BLOCKER" if field != "condition" else "HIGH"
            add(sev, f"missing required attribute '{field}'", len(missing))

    add("HIGH", "no brand (identifier_exists=no applies)",
        len([i for i in items if not i["brand"]]))
    add("INFO", "declaring identifier_exists=no",
        len([i for i in items if i["identifier_exists"] == "no"]))
    add("MEDIUM", "title longer than 150 chars",
        len([i for i in items if len(i["title"]) > 150]))
    add("MEDIUM", "description shorter than 100 chars",
        len([i for i in items if len(i["description"]) < 100]))
    add("MEDIUM", "no additional images",
        len([i for i in items if not i["additional_image_link"]]))
    add("HIGH", "out of stock",
        len([i for i in items if i["availability"] != "in_stock"]))
    # Bare "%" is not promotional — "100% Made in Germany", "100% Polypropylen" are
    # ordinary product facts. Only flag a percentage tied to a discount word.
    promo = re.compile(
        r"\b(sale|sonderangebot|rabatt|gratis|kostenlos|angebot|reduziert|"
        r"\d+\s*%\s*(?:off|rabatt|reduziert|sparen)|!!)", re.I)
    add("HIGH", "promotional text in title",
        len([i for i in items if promo.search(i["title"])]))
    add("MEDIUM", "no google_product_category",
        len([i for i in items if not i["google_product_category"]]))
    return [(s, m, n) for s, m, n in findings if n]


def to_xml(items: list[dict], title: str, link: str) -> str:
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<rss version="2.0" xmlns:g="http://base.google.com/ns/1.0">', "<channel>",
           f"<title>{escape(title)}</title>", f"<link>{escape(link)}</link>",
           "<description>Product feed</description>"]
    multi = {"additional_image_link"}
    for it in items:
        out.append("<item>")
        for k, v in it.items():
            if not v:
                continue
            if k in multi:
                for one in v:
                    out.append(f"<g:{k}>{escape(one)}</g:{k}>")
            else:
                out.append(f"<g:{k}>{escape(str(v))}</g:{k}>")
        out.append("</item>")
    out += ["</channel>", "</rss>"]
    return "\n".join(out)


def to_tsv(items: list[dict]) -> str:
    cols = ["id", "title", "description", "link", "image_link", "additional_image_link",
            "availability", "price", "sale_price", "brand", "gtin", "mpn",
            "identifier_exists", "condition", "google_product_category",
            "product_type", "shipping"]
    rows = ["\t".join(cols)]
    for it in items:
        vals = []
        for c in cols:
            v = it.get(c, "")
            if isinstance(v, list):
                v = ",".join(v)
            vals.append(str(v).replace("\t", " ").replace("\n", " "))
        rows.append("\t".join(vals))
    return "\n".join(rows)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--out", default="feed.xml")
    ap.add_argument("--format", choices=["xml", "tsv"], default="xml")
    ap.add_argument("--country", default="DE")
    ap.add_argument("--currency", default="EUR")
    ap.add_argument("--shipping", help="flat shipping cost, e.g. 170.00")
    ap.add_argument("--max-products", type=int, default=5000)
    ap.add_argument("--reference-prices-verified", action="store_true",
                    help="Emit sale_price. Only pass this once someone has confirmed "
                         "the struck-through reference price was genuinely charged in "
                         "the preceding 30 days (PAngV §11). Off by default, because an "
                         "unsubstantiated reduction is a misrepresentation risk.")
    a = ap.parse_args()

    base = a.url if "://" in a.url else "https://" + a.url
    base = base.rstrip("/")
    items, notes = build(base, a.country, a.currency, a.shipping, a.max_products,
                         a.reference_prices_verified)

    print(f"\nMerchant Center feed — {base}")
    print("=" * 70)
    print(f"  products in feed: {len(items)}")
    for n in notes:
        print(f"  note: {n}")

    print("\n  Validation")
    order = {"BLOCKER": 0, "CRITICAL": 1, "HIGH": 2, "MEDIUM": 3, "INFO": 4}
    findings = sorted(validate(items), key=lambda f: order.get(f[0], 9))
    if not findings:
        print("    no findings")
    for sev, msg, n in findings:
        print(f"    [{sev:8}] {n:4} item(s)  {msg}")

    body = to_xml(items, "omarscontainers", base) if a.format == "xml" else to_tsv(items)
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write(body)
    print(f"\n  written: {a.out}  ({len(body)/1024:.0f} KB)")

    blocking = sum(n for s, _, n in findings if s in ("BLOCKER", "CRITICAL"))
    print(f"\n  {'NOT SUBMITTABLE' if blocking else 'No blocking feed errors'}"
          f" — feed-level checks only. Merchant Center performs its own validation on "
          f"upload, and approval remains Google's decision.")
    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())
