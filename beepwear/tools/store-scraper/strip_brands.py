#!/usr/bin/env python3
"""
strip_brands.py — Remove brand / manufacturer names from a scraped catalog.

Reads a JSON or CSV produced by store_scraper.py, deletes every configured brand
name from the product title, variant title, brand, tags and category fields
(case-insensitive, whole-word), tidies up the punctuation left behind, and writes
a brand-free CSV (or JSON).

Model numbers, sizes, colours (RAL codes) and descriptive words are preserved —
only the brand tokens in --brands (or a --brands-file, one per line) are removed.

Examples:
  python3 strip_brands.py in.json  --brands-file brands.txt -o clean.csv
  python3 strip_brands.py in.csv   --brands "Daikin,GREE,Aiper" --format csv -o clean.csv
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
import sys
from typing import Any, Dict, List

# Reuse the flat-CSV writer so output columns match store_scraper.py exactly.
from store_scraper import write_flat_csv, write_json, write_woo_import_csv

# URLs, www.links, markdown links, e-mail addresses, and bare domains.
_LINK_RE = re.compile(
    r"""(?xi)
      \[([^\]]+)\]\(https?://[^)]+\)      # [text](url) markdown  -> keep text
    | <https?://[^>]+>                     # <url>
    | https?://\S+                         # http(s)://...
    | www\.\S+                             # www....
    | \b[\w.+-]+@[\w-]+\.[\w.-]+\b         # emails
    | \b(?:[a-z0-9-]+\.)+(?:de|com|net|eu|org|shop|store)\b(?:/\S*)?  # bare domains
    """
)


def strip_links(text: str) -> str:
    if not text:
        return text
    # Preserve the anchor text of markdown links, drop everything else.
    text = re.sub(r"\[([^\]]+)\]\(https?://[^)]+\)", r"\1", text)
    return _LINK_RE.sub("", text)


def build_pattern(brands: List[str]) -> re.Pattern:
    # Longest first so "Mitsubishi Heavy" is consumed before "Mitsubishi".
    ordered = sorted({b.strip() for b in brands if b.strip()}, key=len, reverse=True)
    # (?<!\w) / (?!\w) are unicode-friendly word boundaries (German umlauts etc.).
    alt = "|".join(re.escape(b) for b in ordered)
    return re.compile(rf"(?<!\w)(?:{alt})(?!\w)", re.IGNORECASE)


# Separators/quotes that can be left dangling once a brand token is removed.
_LEADING_JUNK = re.compile(r"^[\s–—\-\|,/:·•„“”\"']+")
_TRAILING_JUNK = re.compile(r"[\s–—\-\|,/:·•„“”\"']+$")


def clean_field(text: str, pat: re.Pattern) -> str:
    if not text:
        return text
    text = pat.sub("", text)
    text = re.sub(r'[„“"”]\s*[”“"]', "", text)          # empty quote pairs „"
    text = re.sub(r"\(\s*\)", "", text)                    # empty ()
    text = re.sub(r"\s{2,}", " ", text)                    # collapse spaces
    text = re.sub(r"\s*\|\s*", " | ", text)                # normalize pipes to ' | '
    text = re.sub(r"\s+,", ",", text)                      # space before comma
    text = re.sub(r"([|/–—-])\s*\1+", r"\1", text)         # doubled separators
    text = _LEADING_JUNK.sub("", text)
    text = _TRAILING_JUNK.sub("", text)
    return text.strip()


def load_records(path: str) -> List[Dict[str, Any]]:
    with open(path, encoding="utf-8") as fh:
        if path.lower().endswith(".json"):
            return json.load(fh)
        # Rebuild minimal normalized records from a flat CSV.
        recs: Dict[str, Dict[str, Any]] = {}
        for row in csv.DictReader(fh):
            pid = row.get("product_id") or row.get("url") or row.get("title")
            rec = recs.get(pid)
            if rec is None:
                rec = {
                    "platform": row.get("platform", ""), "source_url": row.get("source_url", ""),
                    "id": row.get("product_id", ""), "handle": row.get("handle", ""),
                    "url": row.get("url", ""), "title": row.get("title", ""),
                    "brand": row.get("brand", ""), "product_type": row.get("product_type", ""),
                    "tags": [t.strip() for t in (row.get("tags") or "").split(",") if t.strip()],
                    "description": "", "images": [row["image"]] if row.get("image") else [],
                    "variants": [],
                }
                recs[pid] = rec
            rec["variants"].append(
                {
                    "id": row.get("variant_id"), "title": row.get("variant_title"),
                    "sku": row.get("sku"), "price": row.get("price"),
                    "compare_at_price": row.get("compare_at_price"),
                    "currency": row.get("currency"), "options": {}, "available": row.get("available"),
                }
            )
        return list(recs.values())


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", help="Scraped .json or .csv from store_scraper.py")
    ap.add_argument("--brands", help="Comma-separated brand names to remove")
    ap.add_argument("--brands-file", help="File with one brand name per line")
    ap.add_argument("--format", choices=["csv", "json"], default="csv")
    ap.add_argument("-o", "--output", help="Output file (default: stdout)")
    args = ap.parse_args(argv)

    brands: List[str] = []
    if args.brands:
        brands += args.brands.split(",")
    if args.brands_file:
        with open(args.brands_file, encoding="utf-8") as fh:
            brands += [ln for ln in fh.read().splitlines() if ln.strip() and not ln.startswith("#")]
    if not brands:
        print("Error: no brands given (use --brands or --brands-file)", file=sys.stderr)
        return 1

    pat = build_pattern(brands)
    records = load_records(args.input)

    removed = 0
    for r in records:
        before = r.get("title", "")
        r["title"] = clean_field(before, pat)
        if r["title"] != before:
            removed += 1
        r["brand"] = clean_field(r.get("brand", ""), pat)
        r["product_type"] = clean_field(r.get("product_type", ""), pat)
        r["tags"] = [clean_field(t, pat) for t in r.get("tags", [])]
        for v in r.get("variants", []):
            v["title"] = clean_field(v.get("title", ""), pat)

    buf = io.StringIO()
    (write_json if args.format == "json" else write_flat_csv)(records, buf)
    data = buf.getvalue()
    if args.output:
        with open(args.output, "w", encoding="utf-8", newline="") as fh:
            fh.write(data)
        print(f"Wrote {args.output} — brand names removed from {removed}/{len(records)} titles",
              file=sys.stderr)
    else:
        sys.stdout.write(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
