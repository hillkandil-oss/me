#!/usr/bin/env python3
"""
build_mc_import.py — Turn a scraped catalog into a Merchant-Center-oriented
WooCommerce import CSV.

Policy:
  * KEEP manufacturer brand names (Google Merchant Center needs the `brand`
    attribute) and populate the WooCommerce **Brands** column from them.
  * REMOVE the SOURCE STORE's identity — its name, domain, product permalinks,
    and any URLs / e-mails — so nothing points back to the store you scraped.
  * Leave GTIN EMPTY (never invent identifiers). For brand-less products set
    "identifier exists = no" in the Google feed.
  * Flag duplicate / near-duplicate / empty descriptions (Google prohibits
    duplicate content) in a separate audit CSV.

Input : JSON produced by store_scraper.py
Output: (1) 49-column WooCommerce product-import CSV matching this repo's proven
            schema (data/products-mc-cleaned.csv);
        (2) an audit CSV: per-row brand, description status, and recommendation.

It does NOT rewrite copy — scraped descriptions are the source store's words. The
audit tells you which need original copy before they are truly submit-ready.

Usage:
  python3 build_mc_import.py scraped.json \\
      --brands-file brands.txt --store-terms-file store-terms.txt \\
      --out-csv mc-import.csv --out-audit mc-audit.csv
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from typing import Any, Dict, List, Optional, Tuple

from strip_brands import build_pattern, clean_field, strip_links

# Canonical brand -> alias patterns (longest / most specific listed first so
# "Mitsubishi Heavy" wins over bare "Mitsubishi").
BRANDS: List[Tuple[str, List[str]]] = [
    ("Mitsubishi Heavy", ["mitsubishi heavy"]),
    ("Mitsubishi Electric", ["mitsubishi electric"]),
    ("Mitsubishi", ["mitsubishi"]),
    ("Daikin", ["daikin"]),
    ("EcoFlow", ["ecoflow", "eco flow"]),
    ("Remko", ["remko"]),
    ("GREE", ["gree"]),
    ("Fendt", ["fendt"]),
    ("Franc", ["franc"]),
    ("Variant", ["variant"]),
    ("Humbaur", ["humbaur"]),
    ("Anssems", ["anssems"]),
    ("TPV", ["tpv"]),
    ("Eduard", ["eduard"]),
    ("Ifor Williams", ["ifor williams", "ifor"]),
    ("Cheval Liberté", ["cheval liberté", "cheval liberte", "cheval"]),
    ("Stahlworks", ["stahlworks"]),
    ("Aiper", ["aiper"]),
    ("Beatbot", ["beatbot"]),
    ("Pool Expert", ["pool expert"]),
]


def load_brand_matchers(brands_file: Optional[str]) -> List[Tuple[str, re.Pattern]]:
    """Build (canonical, compiled-pattern) list. brands_file, if given, may add
    extra canonical brands (one per line) beyond the built-in list."""
    table = list(BRANDS)
    if brands_file:
        known = {c.lower() for c, _ in table}
        for line in open(brands_file, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#") and line.lower() not in known:
                table.append((line, [line.lower()]))
                known.add(line.lower())
    matchers = []
    for canonical, aliases in table:
        alt = "|".join(re.escape(a) for a in sorted(aliases, key=len, reverse=True))
        matchers.append((canonical, re.compile(rf"(?<!\w)(?:{alt})(?!\w)", re.IGNORECASE)))
    return matchers


def detect_brand(text: str, matchers) -> str:
    if not text:
        return ""
    for canonical, pat in matchers:  # ordered: specific brands first
        if pat.search(text):
            return canonical
    return ""


# Exact 49-column header used by data/products-mc-cleaned.csv (WooCommerce export).
WOO_COLUMNS = [
    "ID", "Type", "SKU", "GTIN, UPC, EAN, or ISBN", "Name", "Published",
    "Is featured?", "Visibility in catalog", "Short description", "Description",
    "Date sale price starts", "Date sale price ends", "Tax status", "Tax class",
    "In stock?", "Stock", "Low stock amount", "Backorders allowed?",
    "Sold individually?", "Weight (lbs)", "Length (in)", "Width (in)", "Height (in)",
    "Allow customer reviews?", "Purchase note", "Sale price", "Regular price",
    "Categories", "Tags", "Shipping class", "Images", "Download limit",
    "Download expiry days", "Parent", "Grouped products", "Upsells", "Cross-sells",
    "External URL", "Button text", "Position", "Brands", "Attribute 1 name",
    "Attribute 1 value(s)", "Attribute 1 visible", "Attribute 1 global",
    "Attribute 2 name", "Attribute 2 value(s)", "Attribute 2 visible",
    "Attribute 2 global",
]

AUDIT_COLUMNS = [
    "ID", "Name", "Brand", "Category", "Price", "Currency", "In stock", "Images",
    "Description chars", "Description status", "Duplicate group", "Recommendation",
    "Source URL",
]


def norm_desc(text: str) -> str:
    return re.sub(r"[^a-z0-9äöüß]+", " ", (text or "").lower()).strip()


def shingles(text: str, n: int = 6):
    words = norm_desc(text).split()
    if len(words) < n:
        return frozenset(words)
    return frozenset(tuple(words[i:i + n]) for i in range(len(words) - n + 1))


def cluster_duplicates(items, threshold: float = 0.30):
    """Union-find clustering of descriptions by shingle Jaccard similarity.
    Returns {id: (group_label, is_exact)} for items sharing substantial copy."""
    ids = [it["id"] for it in items if it["desc"]]
    sets = {it["id"]: shingles(it["desc"]) for it in items if it["desc"]}
    parent = {i: i for i in ids}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    max_sim = {}
    for a in range(len(ids)):
        sa = sets[ids[a]]
        if not sa:
            continue
        for b in range(a + 1, len(ids)):
            sb = sets[ids[b]]
            if not sb:
                continue
            inter = len(sa & sb)
            if not inter:
                continue
            j = inter / len(sa | sb)
            if j >= threshold:
                ra, rb = find(ids[a]), find(ids[b])
                if ra != rb:
                    parent[ra] = rb
                key = tuple(sorted((ra, rb)))
                max_sim[find(ids[a])] = max(max_sim.get(find(ids[a]), 0), j)

    groups: Dict[Any, List[Any]] = {}
    for i in ids:
        groups.setdefault(find(i), []).append(i)

    out: Dict[Any, tuple] = {}
    gi = 0
    for root, members in groups.items():
        if len(members) < 2:
            continue
        gi += 1
        # highest pairwise similarity inside this component
        sim = 0.0
        for a in range(len(members)):
            for b in range(a + 1, len(members)):
                sa, sb = sets[members[a]], sets[members[b]]
                if sa and sb:
                    sim = max(sim, len(sa & sb) / len(sa | sb))
        exact = sim >= 0.85
        label = f"{'dup' if exact else 'near'}-{gi}"
        for m in members:
            out[m] = (label, exact)
    return out


def short_desc(text: str, limit: int = 160) -> str:
    if not text or len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0] + "…"


def build(records: List[Dict[str, Any]], brands_file, store_terms_file, overrides=None):
    matchers = load_brand_matchers(brands_file)
    overrides = overrides or {}

    # Store-name / link removal only — brands are intentionally preserved.
    store_terms = []
    if store_terms_file:
        store_terms = [ln.strip() for ln in open(store_terms_file, encoding="utf-8")
                       if ln.strip() and not ln.startswith("#")]
    store_pat = build_pattern(store_terms) if store_terms else None

    def descrub(text: str) -> str:
        text = strip_links(text or "")
        if store_pat:
            text = clean_field(text, store_pat)
        else:
            text = re.sub(r"\s{2,}", " ", text).strip()
        return text

    cleaned: List[Dict[str, Any]] = []
    for r in records:
        v = (r.get("variants") or [{}])[0]
        name = descrub(r.get("title", ""))
        raw_desc = overrides.get(str(r.get("id", "")), r.get("description", ""))
        desc = descrub(raw_desc)
        brand = detect_brand(r.get("title", ""), matchers) or detect_brand(r.get("description", ""), matchers)
        item = {
            "id": r.get("id", ""), "sku": v.get("sku", "") or "", "name": name,
            "desc": desc, "short": short_desc(desc), "brand": brand,
            "category": descrub(r.get("product_type", "")),
            "tags": ", ".join(t for t in (descrub(t) for t in r.get("tags", [])) if t),
            "price": v.get("price"), "regular": v.get("compare_at_price") or v.get("price"),
            "currency": v.get("currency") or "", "available": v.get("available"),
            "images": ", ".join(r.get("images", [])), "image_count": len(r.get("images", [])),
            "source_url": r.get("url", ""),
        }
        cleaned.append(item)

    dup_info = cluster_duplicates(cleaned)
    dup_group_of = {pid: label for pid, (label, _) in dup_info.items()}

    woo_rows, audit_rows = [], []
    for it in cleaned:
        regular, price = it["regular"] or "", it["price"] or ""
        if regular and price and regular != price:
            regular_price, sale_price = regular, price
        else:
            regular_price, sale_price = price or regular, ""

        woo_rows.append({
            "ID": it["id"], "Type": "simple", "SKU": it["sku"],
            "GTIN, UPC, EAN, or ISBN": "", "Name": it["name"], "Published": 1,
            "Is featured?": 0, "Visibility in catalog": "visible",
            "Short description": it["short"], "Description": it["desc"],
            "Date sale price starts": "", "Date sale price ends": "",
            "Tax status": "taxable", "Tax class": "",
            "In stock?": 1 if it["available"] in (True, None, "True", "") else 0,
            "Stock": "", "Low stock amount": "", "Backorders allowed?": 0,
            "Sold individually?": 0, "Weight (lbs)": "", "Length (in)": "",
            "Width (in)": "", "Height (in)": "", "Allow customer reviews?": 1,
            "Purchase note": "", "Sale price": sale_price, "Regular price": regular_price,
            "Categories": it["category"], "Tags": it["tags"], "Shipping class": "",
            "Images": it["images"], "Download limit": "", "Download expiry days": "",
            "Parent": "", "Grouped products": "", "Upsells": "", "Cross-sells": "",
            "External URL": "", "Button text": "", "Position": 0,
            "Brands": it["brand"],
            "Attribute 1 name": "", "Attribute 1 value(s)": "",
            "Attribute 1 visible": "", "Attribute 1 global": "",
            "Attribute 2 name": "", "Attribute 2 value(s)": "",
            "Attribute 2 visible": "", "Attribute 2 global": "",
        })

        group = dup_group_of.get(it["id"], "")
        if not it["desc"]:
            status, rec = "empty", "Write an original description before submitting"
        elif group.startswith("dup"):
            status, rec = "duplicate", "Rewrite — identical copy shared with other products"
        elif group.startswith("near"):
            status, rec = "near-duplicate", "Rewrite — largely shared copy with other products"
        elif it["image_count"] == 0:
            status, rec = "no-image", "Add a product image before submitting"
        else:
            status, rec = "unique", "Spot-check copy is original + accurate, then submit"

        audit_rows.append({
            "ID": it["id"], "Name": it["name"], "Brand": it["brand"],
            "Category": it["category"], "Price": price, "Currency": it["currency"],
            "In stock": it["available"], "Images": it["image_count"],
            "Description chars": len(it["desc"]), "Description status": status,
            "Duplicate group": group, "Recommendation": rec, "Source URL": it["source_url"],
        })

    return woo_rows, audit_rows


def write_csv(path: str, columns: List[str], rows: List[Dict[str, Any]]):
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", help="Scraped .json from store_scraper.py")
    ap.add_argument("--brands-file", help="Extra canonical brands, one per line (optional)")
    ap.add_argument("--store-terms-file", help="Source-store name variants to remove (optional)")
    ap.add_argument("--desc-overrides", help="JSON {product_id: new_description} to replace copy (optional)")
    ap.add_argument("--out-csv", required=True)
    ap.add_argument("--out-audit", required=True)
    args = ap.parse_args(argv)

    records = json.load(open(args.input, encoding="utf-8"))
    overrides = {}
    if args.desc_overrides:
        overrides = {str(k): v for k, v in json.load(open(args.desc_overrides, encoding="utf-8")).items()}
    woo_rows, audit_rows = build(records, args.brands_file, args.store_terms_file, overrides)
    write_csv(args.out_csv, WOO_COLUMNS, woo_rows)
    write_csv(args.out_audit, AUDIT_COLUMNS, audit_rows)

    dstat = Counter(r["Description status"] for r in audit_rows)
    branded = sum(1 for r in audit_rows if r["Brand"])
    print(f"Wrote {args.out_csv} ({len(woo_rows)} products) and {args.out_audit}", file=sys.stderr)
    print(f"Brand populated: {branded}/{len(audit_rows)}  |  Description audit: {dict(dstat)}",
          file=sys.stderr)
    ready = dstat.get("unique", 0)
    print(f"Submit-ready as-is (unique + imaged): {ready}; need rewrite/fix: {len(audit_rows) - ready}",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
