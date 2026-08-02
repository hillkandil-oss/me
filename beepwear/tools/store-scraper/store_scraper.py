#!/usr/bin/env python3
"""
store_scraper.py — Scrape public product catalogs from Shopify and WooCommerce stores.

Zero third-party dependencies (Python 3.8+, standard library only).

It reads the *public* product endpoints that these platforms expose by default:

  Shopify      GET  /products.json?limit=250&page=N        (unauthenticated)
  WooCommerce  GET  /wp-json/wc/store/v1/products?...       (Store API, unauthenticated)
  WooCommerce  GET  /wp-json/wc/v3/products?...             (REST API, needs key+secret)

Platform is auto-detected unless you pass --platform.

Output formats:
  json  full normalized records (one object per product)
  csv   flat table, one row per variant
  woo   WooCommerce product-importer CSV (drop into WooCommerce → Products → Import)

Examples:
  python3 store_scraper.py https://somebrand.com --format json  -o out.json
  python3 store_scraper.py https://somebrand.com --format csv   -o out.csv
  python3 store_scraper.py https://somebrand.com --format woo   -o woo-import.csv
  python3 store_scraper.py https://shop.example.com \\
      --platform woocommerce --wc-key ck_xxx --wc-secret cs_xxx --format json

Only scrape stores you are authorized to scrape, and respect each site's Terms of
Service and robots.txt. These endpoints are public by design, but you are responsible
for how you use them. Be polite: keep --delay > 0 so you don't hammer a store.
"""

from __future__ import annotations

import argparse
import base64
import csv
import html
import io
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, Iterable, List, Optional

USER_AGENT = "store-scraper/1.0 (+https://github.com/hillkandil-oss/me)"
DEFAULT_TIMEOUT = 30


# --------------------------------------------------------------------------- #
# HTTP helpers
# --------------------------------------------------------------------------- #
def http_get(
    url: str,
    *,
    headers: Optional[Dict[str, str]] = None,
    timeout: int = DEFAULT_TIMEOUT,
    retries: int = 3,
    backoff: float = 2.0,
) -> tuple[int, bytes]:
    """GET a URL with retries + exponential backoff. Returns (status, body)."""
    hdrs = {"User-Agent": USER_AGENT, "Accept": "application/json, */*"}
    if headers:
        hdrs.update(headers)

    last_err: Optional[Exception] = None
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, headers=hdrs, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.getcode(), resp.read()
        except urllib.error.HTTPError as exc:
            # 404/401/403 are answers, not transient failures — don't retry those.
            if exc.code in (401, 403, 404, 406):
                return exc.code, exc.read()
            last_err = exc
        except (urllib.error.URLError, TimeoutError, ConnectionError) as exc:
            last_err = exc
        if attempt < retries:
            time.sleep(backoff * (2 ** attempt))
    raise RuntimeError(f"GET failed after {retries + 1} attempts: {url} ({last_err})")


def normalize_base(url: str) -> str:
    """Return scheme://host from any URL the user pastes."""
    if "://" not in url:
        url = "https://" + url
    parts = urllib.parse.urlparse(url)
    if not parts.netloc:
        raise ValueError(f"Cannot parse a host out of {url!r}")
    return f"{parts.scheme}://{parts.netloc}"


def strip_html(text: Optional[str]) -> str:
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


# --------------------------------------------------------------------------- #
# Normalized record shape
# --------------------------------------------------------------------------- #
# Each scraped product is normalized to:
# {
#   platform, source_url, id, handle, url, title, brand, product_type,
#   tags: [str], description: str, images: [str],
#   variants: [{id, title, sku, price, compare_at_price, currency,
#               options: {name: value}, available}]
# }


def _num(value: Any) -> Optional[str]:
    if value in (None, "", False):
        return None
    return str(value)


# --------------------------------------------------------------------------- #
# Shopify
# --------------------------------------------------------------------------- #
def detect_shopify(base: str, timeout: int) -> bool:
    status, body = http_get(f"{base}/products.json?limit=1", timeout=timeout, retries=1)
    if status != 200:
        return False
    try:
        return isinstance(json.loads(body).get("products"), list)
    except (json.JSONDecodeError, AttributeError):
        return False


def scrape_shopify(
    base: str, *, delay: float, max_pages: int, timeout: int, log
) -> Iterable[Dict[str, Any]]:
    page = 1
    while page <= max_pages:
        url = f"{base}/products.json?limit=250&page={page}"
        status, body = http_get(url, timeout=timeout)
        if status != 200:
            log(f"  shopify page {page}: HTTP {status}, stopping")
            break
        products = json.loads(body).get("products", [])
        if not products:
            break
        log(f"  shopify page {page}: {len(products)} products")
        for p in products:
            yield _normalize_shopify(base, p)
        if len(products) < 250:
            break
        page += 1
        if delay:
            time.sleep(delay)


def _normalize_shopify(base: str, p: Dict[str, Any]) -> Dict[str, Any]:
    option_names = [o.get("name", f"Option {i+1}") for i, o in enumerate(p.get("options", []))]
    variants = []
    for v in p.get("variants", []):
        opts = {}
        for i, name in enumerate(option_names):
            key = f"option{i+1}"
            if v.get(key) not in (None, "", "Default Title"):
                opts[name] = v[key]
        variants.append(
            {
                "id": _num(v.get("id")),
                "title": v.get("title"),
                "sku": v.get("sku") or "",
                "price": _num(v.get("price")),
                "compare_at_price": _num(v.get("compare_at_price")),
                "currency": None,  # products.json doesn't include currency
                "options": opts,
                "available": v.get("available"),
            }
        )
    return {
        "platform": "shopify",
        "source_url": base,
        "id": _num(p.get("id")),
        "handle": p.get("handle"),
        "url": f"{base}/products/{p.get('handle')}" if p.get("handle") else base,
        "title": p.get("title"),
        "brand": p.get("vendor") or "",
        "product_type": p.get("product_type") or "",
        "tags": p.get("tags") if isinstance(p.get("tags"), list) else _split_tags(p.get("tags")),
        "description": strip_html(p.get("body_html")),
        "images": [img.get("src") for img in p.get("images", []) if img.get("src")],
        "variants": variants,
    }


def _split_tags(tags: Any) -> List[str]:
    if isinstance(tags, list):
        return tags
    if isinstance(tags, str):
        return [t.strip() for t in tags.split(",") if t.strip()]
    return []


# --------------------------------------------------------------------------- #
# WooCommerce — Store API (public, unauthenticated)
# --------------------------------------------------------------------------- #
def detect_woocommerce(base: str, timeout: int) -> bool:
    for path in ("/wp-json/wc/store/v1/products?per_page=1", "/wp-json/wc/store/products?per_page=1"):
        status, body = http_get(f"{base}{path}", timeout=timeout, retries=1)
        if status == 200:
            try:
                if isinstance(json.loads(body), list):
                    return True
            except json.JSONDecodeError:
                pass
    return False


def scrape_woocommerce_store(
    base: str, *, delay: float, max_pages: int, timeout: int, log
) -> Iterable[Dict[str, Any]]:
    # Prefer the versioned path; fall back to the unversioned one.
    api = "/wp-json/wc/store/v1/products"
    status, _ = http_get(f"{base}{api}?per_page=1", timeout=timeout, retries=1)
    if status != 200:
        api = "/wp-json/wc/store/products"

    page = 1
    while page <= max_pages:
        url = f"{base}{api}?per_page=100&page={page}"
        status, body = http_get(url, timeout=timeout)
        if status != 200:
            log(f"  woo store page {page}: HTTP {status}, stopping")
            break
        products = json.loads(body)
        if not isinstance(products, list) or not products:
            break
        log(f"  woo store page {page}: {len(products)} products")
        for p in products:
            yield _normalize_woo_store(base, p)
        if len(products) < 100:
            break
        page += 1
        if delay:
            time.sleep(delay)


def _woo_price(minor: Any, minor_unit: Any) -> Optional[str]:
    """WooCommerce Store API returns prices as integer strings in minor units."""
    if minor in (None, ""):
        return None
    try:
        unit = int(minor_unit) if minor_unit not in (None, "") else 2
        return f"{int(minor) / (10 ** unit):.{unit}f}"
    except (ValueError, TypeError):
        return str(minor)


def _normalize_woo_store(base: str, p: Dict[str, Any]) -> Dict[str, Any]:
    prices = p.get("prices", {}) or {}
    unit = prices.get("currency_minor_unit", 2)
    currency = prices.get("currency_code")
    variant = {
        "id": _num(p.get("id")),
        "title": p.get("name"),
        "sku": p.get("sku") or "",
        "price": _woo_price(prices.get("price"), unit),
        "compare_at_price": _woo_price(prices.get("regular_price"), unit),
        "currency": currency,
        "options": {},
        "available": p.get("is_in_stock"),
    }
    return {
        "platform": "woocommerce",
        "source_url": base,
        "id": _num(p.get("id")),
        "handle": p.get("slug"),
        "url": p.get("permalink") or base,
        "title": p.get("name"),
        "brand": "",  # brand is a plugin taxonomy; not exposed by Store API
        "product_type": ", ".join(c.get("name", "") for c in p.get("categories", [])),
        "tags": [t.get("name", "") for t in p.get("tags", [])],
        "description": strip_html(p.get("description") or p.get("short_description")),
        "images": [img.get("src") for img in p.get("images", []) if img.get("src")],
        "variants": [variant],
    }


# --------------------------------------------------------------------------- #
# WooCommerce — REST API (authenticated, richer data)
# --------------------------------------------------------------------------- #
def scrape_woocommerce_rest(
    base: str, key: str, secret: str, *, delay: float, max_pages: int, timeout: int, log
) -> Iterable[Dict[str, Any]]:
    token = base64.b64encode(f"{key}:{secret}".encode()).decode()
    headers = {"Authorization": f"Basic {token}"}
    page = 1
    while page <= max_pages:
        url = f"{base}/wp-json/wc/v3/products?per_page=100&page={page}&status=publish"
        status, body = http_get(url, headers=headers, timeout=timeout)
        if status != 200:
            log(f"  woo rest page {page}: HTTP {status} — check API keys / permissions")
            break
        products = json.loads(body)
        if not isinstance(products, list) or not products:
            break
        log(f"  woo rest page {page}: {len(products)} products")
        for p in products:
            yield _normalize_woo_rest(base, p)
        if len(products) < 100:
            break
        page += 1
        if delay:
            time.sleep(delay)


def _normalize_woo_rest(base: str, p: Dict[str, Any]) -> Dict[str, Any]:
    variants = [
        {
            "id": _num(p.get("id")),
            "title": p.get("name"),
            "sku": p.get("sku") or "",
            "price": _num(p.get("price")),
            "compare_at_price": _num(p.get("regular_price")),
            "currency": None,
            "options": {a.get("name"): ", ".join(a.get("options", [])) for a in p.get("attributes", [])},
            "available": p.get("stock_status") == "instock",
        }
    ]
    return {
        "platform": "woocommerce",
        "source_url": base,
        "id": _num(p.get("id")),
        "handle": p.get("slug"),
        "url": p.get("permalink") or base,
        "title": p.get("name"),
        "brand": "",
        "product_type": ", ".join(c.get("name", "") for c in p.get("categories", [])),
        "tags": [t.get("name", "") for t in p.get("tags", [])],
        "description": strip_html(p.get("description") or p.get("short_description")),
        "images": [img.get("src") for img in p.get("images", []) if img.get("src")],
        "variants": variants,
    }


# --------------------------------------------------------------------------- #
# Output writers
# --------------------------------------------------------------------------- #
def write_json(records: List[Dict[str, Any]], out) -> None:
    json.dump(records, out, indent=2, ensure_ascii=False)
    out.write("\n")


def write_flat_csv(records: List[Dict[str, Any]], out) -> None:
    cols = [
        "platform", "source_url", "product_id", "handle", "url", "title", "brand",
        "product_type", "tags", "variant_id", "variant_title", "sku", "price",
        "compare_at_price", "currency", "options", "available", "image",
    ]
    w = csv.DictWriter(out, fieldnames=cols, extrasaction="ignore")
    w.writeheader()
    for r in records:
        first_image = r["images"][0] if r["images"] else ""
        for v in r["variants"] or [{}]:
            opts = "; ".join(f"{k}: {val}" for k, val in (v.get("options") or {}).items())
            w.writerow(
                {
                    "platform": r["platform"], "source_url": r["source_url"],
                    "product_id": r["id"], "handle": r["handle"], "url": r["url"],
                    "title": r["title"], "brand": r["brand"], "product_type": r["product_type"],
                    "tags": ", ".join(r["tags"]), "variant_id": v.get("id"),
                    "variant_title": v.get("title"), "sku": v.get("sku"),
                    "price": v.get("price"), "compare_at_price": v.get("compare_at_price"),
                    "currency": v.get("currency"), "options": opts,
                    "available": v.get("available"), "image": first_image,
                }
            )


def write_woo_import_csv(records: List[Dict[str, Any]], out) -> None:
    """Emit the column set the WooCommerce product importer understands."""
    cols = [
        "Type", "SKU", "Name", "Published", "Is featured?", "Visibility in catalog",
        "Short description", "Description", "In stock?", "Regular price", "Sale price",
        "Categories", "Tags", "Brands", "Images", "External URL",
    ]
    w = csv.DictWriter(out, fieldnames=cols, extrasaction="ignore")
    w.writeheader()
    for r in records:
        v = (r["variants"] or [{}])[0]
        price = v.get("compare_at_price") or v.get("price") or ""
        sale = v.get("price") if v.get("compare_at_price") and v.get("price") != v.get("compare_at_price") else ""
        desc = r["description"]
        w.writerow(
            {
                "Type": "simple",
                "SKU": v.get("sku") or "",
                "Name": r["title"] or "",
                "Published": 1,
                "Is featured?": 0,
                "Visibility in catalog": "visible",
                "Short description": desc[:200],
                "Description": desc,
                "In stock?": 1 if v.get("available") in (True, None) else 0,
                "Regular price": price,
                "Sale price": sale,
                "Categories": r["product_type"] or "",
                "Tags": ", ".join(r["tags"]),
                "Brands": r["brand"] or "",
                "Images": ", ".join(r["images"]),
                "External URL": r["url"],
            }
        )


# --------------------------------------------------------------------------- #
# Orchestration
# --------------------------------------------------------------------------- #
def scrape(args, log) -> List[Dict[str, Any]]:
    base = normalize_base(args.store_url)
    log(f"Store: {base}")

    platform = args.platform
    if platform == "auto":
        log("Detecting platform…")
        if detect_shopify(base, args.timeout):
            platform = "shopify"
        elif detect_woocommerce(base, args.timeout):
            platform = "woocommerce"
        else:
            raise SystemExit(
                "Could not auto-detect the platform. Neither /products.json (Shopify) "
                "nor /wp-json/wc/store/v1/products (WooCommerce) responded as expected.\n"
                "Pass --platform shopify|woocommerce explicitly, or check the URL / that "
                "the store exposes its public product API."
            )
    log(f"Platform: {platform}")

    if platform == "shopify":
        gen = scrape_shopify(base, delay=args.delay, max_pages=args.max_pages,
                             timeout=args.timeout, log=log)
    elif platform == "woocommerce":
        if args.wc_key and args.wc_secret:
            log("Using WooCommerce REST API (authenticated)")
            gen = scrape_woocommerce_rest(base, args.wc_key, args.wc_secret,
                                         delay=args.delay, max_pages=args.max_pages,
                                         timeout=args.timeout, log=log)
        else:
            gen = scrape_woocommerce_store(base, delay=args.delay, max_pages=args.max_pages,
                                          timeout=args.timeout, log=log)
    else:
        raise SystemExit(f"Unknown platform: {platform}")

    records: List[Dict[str, Any]] = []
    for rec in gen:
        records.append(rec)
        if args.limit and len(records) >= args.limit:
            log(f"Reached --limit {args.limit}, stopping")
            break
    return records


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Scrape public product catalogs from Shopify and WooCommerce stores.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__.split("Examples:")[1] if "Examples:" in __doc__ else None,
    )
    p.add_argument("store_url", help="Store URL, e.g. https://somebrand.com")
    p.add_argument("--platform", choices=["auto", "shopify", "woocommerce"], default="auto")
    p.add_argument("--format", choices=["json", "csv", "woo"], default="json",
                   help="json=full records, csv=flat per-variant table, woo=WooCommerce import CSV")
    p.add_argument("-o", "--output", help="Output file (default: stdout)")
    p.add_argument("--limit", type=int, default=0, help="Stop after N products (0 = all)")
    p.add_argument("--max-pages", type=int, default=1000, help="Safety cap on pages fetched")
    p.add_argument("--delay", type=float, default=0.5, help="Seconds to wait between page requests")
    p.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="Per-request timeout (s)")
    p.add_argument("--wc-key", help="WooCommerce REST API consumer key (ck_...)")
    p.add_argument("--wc-secret", help="WooCommerce REST API consumer secret (cs_...)")
    p.add_argument("--quiet", action="store_true", help="Suppress progress logging to stderr")
    return p


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)

    def log(msg: str) -> None:
        if not args.quiet:
            print(msg, file=sys.stderr)

    try:
        records = scrape(args, log)
    except (ValueError, RuntimeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    log(f"Scraped {len(records)} products "
        f"({sum(len(r['variants']) for r in records)} variants).")

    # Write to the chosen sink.
    buf = io.StringIO()
    if args.format == "json":
        write_json(records, buf)
    elif args.format == "csv":
        write_flat_csv(records, buf)
    elif args.format == "woo":
        write_woo_import_csv(records, buf)

    data = buf.getvalue()
    if args.output:
        with open(args.output, "w", encoding="utf-8", newline="") as fh:
            fh.write(data)
        log(f"Wrote {args.output}")
    else:
        sys.stdout.write(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
