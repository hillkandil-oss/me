#!/usr/bin/env python3
"""
push_to_woo.py — Create products in a WooCommerce store via the REST API,
bypassing the CSV importer entirely.

Reads the scraped JSON (store_scraper.py output) or the 49-column MC import CSV
and POSTs each product to /wp-json/wc/v3/products with your API key/secret.
Idempotent by SKU (or by name when SKU is blank): re-running updates existing
products instead of duplicating them.

Get API keys: WooCommerce -> Settings -> Advanced -> REST API -> Add key
(Permissions: Read/Write). Needs HTTPS.

Examples:
  # Dry run first — shows what would be created, changes nothing:
  python3 push_to_woo.py products.json \\
      --store https://your-new-store.com --key ck_xxx --secret cs_xxx --dry-run

  # Real import:
  python3 push_to_woo.py products.json \\
      --store https://your-new-store.com --key ck_xxx --secret cs_xxx

  # From the MC import CSV instead of JSON:
  python3 push_to_woo.py mc-import.csv --format csv \\
      --store https://your-new-store.com --key ck_xxx --secret cs_xxx
"""
from __future__ import annotations

import argparse
import base64
import csv
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, List, Optional

from store_scraper import normalize_base

TIMEOUT = 60


def api(method: str, base: str, path: str, key: str, secret: str,
        payload: Optional[dict] = None, params: Optional[dict] = None):
    url = f"{base}/wp-json/wc/v3/{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    token = base64.b64encode(f"{key}:{secret}".encode()).decode()
    headers = {"Authorization": f"Basic {token}", "Content-Type": "application/json",
               "User-Agent": "store-scraper-push/1.0"}
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                return resp.getcode(), json.loads(resp.read() or "null")
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", "replace")
            if exc.code in (429, 500, 502, 503, 504) and attempt < 3:
                time.sleep(2 ** attempt)
                continue
            return exc.code, body
        except (urllib.error.URLError, TimeoutError, ConnectionError) as exc:
            if attempt < 3:
                time.sleep(2 ** attempt)
                continue
            raise RuntimeError(f"{method} {url} failed: {exc}")
    return 0, None


def find_existing(base, key, secret, sku: str, name: str) -> Optional[int]:
    if sku:
        code, data = api("GET", base, "products", key, secret, params={"sku": sku})
        if code == 200 and isinstance(data, list) and data:
            return data[0]["id"]
    code, data = api("GET", base, "products", key, secret,
                     params={"search": name, "per_page": 5})
    if code == 200 and isinstance(data, list):
        for p in data:
            if p.get("name", "").strip().lower() == name.strip().lower():
                return p["id"]
    return None


def records_from_json(path: str) -> List[Dict[str, Any]]:
    out = []
    for r in json.load(open(path, encoding="utf-8")):
        v = (r.get("variants") or [{}])[0]
        regular = v.get("compare_at_price") or v.get("price")
        price = v.get("price")
        out.append({
            "name": r.get("title", ""), "sku": v.get("sku", "") or "",
            "description": r.get("description", ""), "brand": r.get("brand", ""),
            "regular": regular if regular and price and regular != price else (price or regular),
            "sale": price if regular and price and regular != price else "",
            "category": r.get("product_type", ""), "images": r.get("images", []),
            "in_stock": v.get("available") in (True, None),
        })
    return out


def records_from_csv(path: str) -> List[Dict[str, Any]]:
    out = []
    for r in csv.DictReader(open(path, encoding="utf-8")):
        out.append({
            "name": r.get("Name", ""), "sku": r.get("SKU", "") or "",
            "description": r.get("Description", ""), "brand": r.get("Brands", ""),
            "regular": r.get("Regular price", ""), "sale": r.get("Sale price", ""),
            "category": r.get("Categories", ""),
            "images": [u.strip() for u in (r.get("Images", "") or "").split(",") if u.strip()],
            "in_stock": str(r.get("In stock?", "1")) in ("1", "true", "True", ""),
        })
    return out


def to_payload(rec: Dict[str, Any]) -> dict:
    p: Dict[str, Any] = {
        "name": rec["name"], "type": "simple", "status": "publish",
        "description": rec["description"],
        "short_description": (rec["description"] or "")[:200],
        "regular_price": str(rec["regular"] or ""),
        "stock_status": "instock" if rec["in_stock"] else "outofstock",
    }
    if rec.get("sku"):
        p["sku"] = rec["sku"]
    if rec.get("sale"):
        p["sale_price"] = str(rec["sale"])
    if rec.get("category"):
        p["categories"] = [{"name": c.strip()} for c in rec["category"].split(",") if c.strip()]
    if rec.get("images"):
        p["images"] = [{"src": u} for u in rec["images"]]
    if rec.get("brand"):
        # Native WooCommerce Brands taxonomy (WC 9.6+). Ignored by stores without it.
        p["brands"] = [{"name": rec["brand"]}]
    return p


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", help="products.json or mc-import.csv")
    ap.add_argument("--format", choices=["json", "csv"], default="json")
    ap.add_argument("--store", required=True, help="New store URL (https://...)")
    ap.add_argument("--key", required=True, help="WooCommerce consumer key (ck_...)")
    ap.add_argument("--secret", required=True, help="WooCommerce consumer secret (cs_...)")
    ap.add_argument("--dry-run", action="store_true", help="Show actions, change nothing")
    ap.add_argument("--limit", type=int, default=0, help="Only process first N (0=all)")
    ap.add_argument("--delay", type=float, default=0.3, help="Seconds between requests")
    args = ap.parse_args(argv)

    base = normalize_base(args.store)
    recs = (records_from_csv if args.format == "csv" else records_from_json)(args.input)
    if args.limit:
        recs = recs[:args.limit]

    if not args.dry_run:
        code, _ = api("GET", base, "products", args.key, args.secret, params={"per_page": 1})
        if code != 200:
            print(f"Auth/connection check failed (HTTP {code}). Verify --store is HTTPS and "
                  f"the key/secret have Read/Write permission.", file=sys.stderr)
            return 1

    created = updated = failed = 0
    for i, rec in enumerate(recs, 1):
        if not rec["name"]:
            continue
        if args.dry_run:
            print(f"[dry-run] would import: {rec['name'][:60]}  "
                  f"(sku={rec['sku'] or '-'}, price={rec['regular']}, imgs={len(rec['images'])})")
            continue
        existing = find_existing(base, args.key, args.secret, rec["sku"], rec["name"])
        payload = to_payload(rec)
        if existing:
            code, data = api("PUT", base, f"products/{existing}", args.key, args.secret, payload)
            action = "updated"
        else:
            code, data = api("POST", base, "products", args.key, args.secret, payload)
            action = "created"
        if code in (200, 201):
            created += action == "created"
            updated += action == "updated"
            print(f"  [{i}/{len(recs)}] {action}: {rec['name'][:55]}")
        else:
            failed += 1
            msg = data if isinstance(data, str) else json.dumps(data)
            print(f"  [{i}/{len(recs)}] FAILED ({code}): {rec['name'][:45]} -> {msg[:120]}",
                  file=sys.stderr)
        time.sleep(args.delay)

    if args.dry_run:
        print(f"\nDry run: {len(recs)} products would be imported.", file=sys.stderr)
    else:
        print(f"\nDone. created={created} updated={updated} failed={failed}", file=sys.stderr)
    return 0 if failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
