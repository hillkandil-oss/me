#!/usr/bin/env python3
"""
gmc-audit scanner — deterministic Google Merchant Center compliance checks.

Three modes (combine as needed):

  --feed  PATH        Audit a product feed CSV (WooCommerce/Shopify-style or
                      Google feed columns). Flags required-attribute gaps, brand
                      coverage, missing GTINs, price anomalies, duplicate
                      descriptions, and condition issues.
  --html  GLOB/DIR    Scan local .html/.md files for placeholder leaks, missing
                      contact info, and missing policy links.
  --url   URL         Best-effort live fetch of key pages (may be blocked by a
                      proxy; if so, fetch pages with WebFetch instead).

Exit code is 0 on success; findings are printed as a report (and JSON with
--json). This script never edits anything and never invents data — it only
reports what it sees.

Examples:
  python scan_site.py --feed products.csv
  python scan_site.py --html 'content/**/*.md'
  python scan_site.py --url https://example.com --json
"""
import argparse
import csv
import glob
import json
import os
import re
import sys
from collections import Counter

# ---- signals -------------------------------------------------------------

PLACEHOLDER_PATTERNS = [
    (r"\[confirm:", "unresolved [confirm: …] marker"),
    (r"\blorem ipsum\b", "Lorem ipsum placeholder text"),
    (r"\bTBD\b", "TBD placeholder"),
    (r"\bTODO\b", "TODO marker"),
    (r"\bplaceholder\b", "literal 'placeholder' text"),
    (r"\bxxxx+\b", "xxxx placeholder"),
    (r"\*\*\s*\*\*", "empty bold/blank (** **) — missing value"),
    (r"\[\s*\]", "empty [] bracket"),
    (r"insert .{0,20} here", "'insert … here' template instruction"),
]

CONTACT_PATTERNS = {
    "email": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    "phone": r"(\+?\d[\d\s().-]{7,}\d)",
    "address": r"\d{1,6}\s+[A-Za-z0-9.\s]+,\s*[A-Za-z\s]+,?\s*[A-Z]{2}\s*\d{5}",
}

POLICY_KEYWORDS = {
    "returns/refunds": ["return", "refund"],
    "shipping": ["shipping", "delivery"],
    "privacy": ["privacy"],
    "terms": ["terms", "conditions"],
    "contact": ["contact"],
}

# columns we try to map (case-insensitive), across common feed dialects
COL_ALIASES = {
    "name": ["name", "title", "product title", "product name"],
    "description": ["description", "body (html)", "long description"],
    "price": ["regular price", "price", "variant price"],
    "brand": ["brands", "brand", "vendor", "manufacturer"],
    "gtin": ["gtin", "upc", "ean", "barcode", "isbn"],
    "condition": ["condition"],
    "availability": ["availability", "in stock?", "stock status"],
    "image": ["images", "image", "image_link", "image link", "image url"],
}

LUXURY_BRANDS = [
    "rolex", "omega", "patek", "audemars", "tag heuer", "cartier", "breitling",
    "ulysse nardin", "zenith", "panerai", "iwc", "vacheron", "jaeger", "hublot",
    "tudor", "tiffany", "louis vuitton", "gucci", "chanel", "hermes", "prada",
]


def _find_col(header, aliases):
    low = [h.strip().lower() for h in header]
    for alias in aliases:
        if alias in low:
            return low.index(alias)
    return None


def scan_feed(path):
    findings = []
    with open(path, newline="", encoding="utf-8", errors="replace") as f:
        rows = list(csv.reader(f))
    if not rows:
        return [{"severity": "P1", "check": "feed-empty",
                 "detail": f"{path} has no rows"}]
    header, data = rows[0], rows[1:]
    cols = {k: _find_col(header, v) for k, v in COL_ALIASES.items()}

    def cell(row, key):
        i = cols.get(key)
        return row[i].strip() if i is not None and i < len(row) else ""

    n = len(data)
    findings.append({"severity": "info", "check": "feed-size",
                     "detail": f"{n} products; columns mapped: "
                     + ", ".join(k for k, v in cols.items() if v is not None)})

    # required-attribute coverage
    for key, sev in [("name", "P1"), ("description", "P1"), ("price", "P1"),
                     ("brand", "P1"), ("image", "P2")]:
        if cols.get(key) is None:
            findings.append({"severity": sev, "check": f"missing-column:{key}",
                             "detail": f"No '{key}' column found in feed header"})
            continue
        missing = sum(1 for r in data if not cell(r, key))
        if missing:
            findings.append({"severity": sev, "check": f"blank-{key}",
                             "detail": f"{missing}/{n} products have no {key}"})

    # GTIN / identifiers
    if cols.get("gtin") is None:
        findings.append({"severity": "P2", "check": "no-gtin-column",
                         "detail": "No GTIN/UPC/EAN column. Add real identifiers "
                         "where they exist; set identifier_exists=no otherwise. "
                         "Never invent identifiers."})
    else:
        missing = sum(1 for r in data if not cell(r, "gtin"))
        if missing:
            findings.append({"severity": "P2", "check": "blank-gtin",
                             "detail": f"{missing}/{n} products have no GTIN"})

    # condition
    if cols.get("condition") is None:
        findings.append({"severity": "P2", "check": "no-condition",
                         "detail": "No condition column (new/used/refurbished). "
                         "Merchant Center wants condition; must match reality."})

    # duplicate descriptions (low-quality/duplicate content signal)
    if cols.get("description") is not None:
        descs = [cell(r, "description") for r in data if cell(r, "description")]
        norm = [re.sub(r"\s+", " ", d.lower()).strip() for d in descs]
        dupes = [(txt, c) for txt, c in Counter(norm).items() if c > 1]
        shared = sum(c for _, c in dupes)
        if shared:
            worst = max(dupes, key=lambda x: x[1])
            findings.append({"severity": "P1", "check": "duplicate-descriptions",
                             "detail": f"{shared} products share a description with "
                             f"another (worst: 1 blurb reused {worst[1]}×). Google "
                             f"treats reused copy as low-quality/duplicate content — "
                             f"each product needs an original description."})

    # price anomalies + cheap-luxury counterfeit flag
    if cols.get("price") is not None:
        prices = []
        cheap_lux = []
        for r in data:
            raw = cell(r, "price")
            try:
                p = float(re.sub(r"[^0-9.]", "", raw)) if raw else None
            except ValueError:
                p = None
            if p is not None:
                prices.append(p)
                hay = (cell(r, "name") + " " + cell(r, "brand")).lower()
                if p < 500 and any(b in hay for b in LUXURY_BRANDS):
                    cheap_lux.append((cell(r, "name")[:60], p))
        if prices:
            prices_sorted = sorted(prices)
            med = prices_sorted[len(prices_sorted) // 2]
            findings.append({"severity": "info", "check": "price-range",
                             "detail": f"min ${min(prices):.0f} / median "
                             f"${med:.0f} / max ${max(prices):.0f}"})
        if cheap_lux:
            ex = "; ".join(f"{n} (${p:.0f})" for n, p in cheap_lux[:5])
            findings.append({"severity": "P0", "check": "cheap-luxury",
                             "detail": f"{len(cheap_lux)} luxury-brand items priced "
                             f"under $500 — a top counterfeit flag. Verify these are "
                             f"genuine and priced believably. e.g. {ex}"})
    return findings


def _read_text_files(pattern):
    paths = []
    if os.path.isdir(pattern):
        for root, _, files in os.walk(pattern):
            for fn in files:
                if fn.lower().endswith((".html", ".htm", ".md", ".txt")):
                    paths.append(os.path.join(root, fn))
    else:
        paths = [p for p in glob.glob(pattern, recursive=True) if os.path.isfile(p)]
    return paths


def scan_html(pattern):
    findings = []
    paths = _read_text_files(pattern)
    if not paths:
        return [{"severity": "P2", "check": "no-files",
                 "detail": f"No .html/.md/.txt files matched '{pattern}'"}]
    all_text = ""
    for p in paths:
        try:
            txt = open(p, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        all_text += "\n" + txt
        for pat, label in PLACEHOLDER_PATTERNS:
            for m in re.finditer(pat, txt, re.IGNORECASE):
                line = txt[:m.start()].count("\n") + 1
                findings.append({"severity": "P1", "check": "placeholder",
                                 "detail": f"{p}:{line} — {label}: "
                                 f"'{m.group(0)[:40]}'"})

    # contact-info presence across the whole corpus
    for kind, pat in CONTACT_PATTERNS.items():
        if not re.search(pat, all_text):
            findings.append({"severity": "P1", "check": f"no-{kind}",
                             "detail": f"No {kind} found anywhere in scanned files "
                             f"— Merchant Center wants visible {kind}."})

    # policy-page presence (by keyword in filenames or content)
    joined_names = " ".join(paths).lower()
    for policy, kws in POLICY_KEYWORDS.items():
        if not any(k in joined_names or k in all_text.lower() for k in kws):
            findings.append({"severity": "P1", "check": f"no-policy:{policy}",
                             "detail": f"No {policy} policy detected."})
    return findings


def scan_url(url, pages):
    findings = []
    try:
        import urllib.request
        import ssl
    except ImportError:
        return [{"severity": "info", "check": "url-skip",
                 "detail": "urllib unavailable"}]
    if not url.startswith("https://"):
        findings.append({"severity": "P1", "check": "not-https",
                         "detail": f"{url} is not HTTPS — Merchant Center requires "
                         f"secure checkout/site."})
    ctx = ssl.create_default_context()
    base = url.rstrip("/")
    for page in [""] + pages:
        target = base + page
        try:
            req = urllib.request.Request(target, headers={"User-Agent":
                                         "gmc-audit-bot/1.0"})
            with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
                body = resp.read().decode("utf-8", "replace")
            for pat, label in PLACEHOLDER_PATTERNS:
                if re.search(pat, body, re.IGNORECASE):
                    findings.append({"severity": "P1", "check": "live-placeholder",
                                     "detail": f"{target} contains {label}"})
        except Exception as e:  # noqa: BLE001 - report, don't crash
            findings.append({"severity": "info", "check": "fetch-failed",
                             "detail": f"{target}: {e.__class__.__name__} — fetch "
                             f"with WebFetch instead and check manually."})
    return findings


def main():
    ap = argparse.ArgumentParser(description="Google Merchant Center compliance scanner")
    ap.add_argument("--feed", help="product feed CSV to audit")
    ap.add_argument("--html", help="glob or directory of local HTML/MD to scan")
    ap.add_argument("--url", help="live site base URL (best-effort)")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    args = ap.parse_args()

    if not any([args.feed, args.html, args.url]):
        ap.print_help()
        return 1

    findings = []
    if args.feed:
        findings += [{**f, "mode": "feed"} for f in scan_feed(args.feed)]
    if args.html:
        findings += [{**f, "mode": "html"} for f in scan_html(args.html)]
    if args.url:
        pages = ["/about", "/contact", "/returns", "/shipping-policy",
                 "/privacy-policy", "/terms"]
        findings += [{**f, "mode": "url"} for f in scan_url(args.url, pages)]

    if args.json:
        print(json.dumps(findings, indent=2))
        return 0

    order = {"P0": 0, "P1": 1, "P2": 2, "P3": 3, "info": 9}
    findings.sort(key=lambda x: order.get(x["severity"], 5))
    counts = Counter(f["severity"] for f in findings)
    print("=" * 66)
    print("  GOOGLE MERCHANT CENTER — AUTOMATED COMPLIANCE SCAN")
    print("=" * 66)
    for f in findings:
        tag = f["severity"].upper().ljust(4)
        print(f"[{tag}] ({f['mode']}/{f['check']}) {f['detail']}")
    print("-" * 66)
    print("Summary: " + ", ".join(f"{k}={counts[k]}" for k in
          ["P0", "P1", "P2", "P3", "info"] if counts.get(k)))
    print("Note: automated scan finds mechanical issues only. Judgment items "
          "(fabricated identity, authenticity claims, price plausibility) still "
          "need a human/Claude read of the live pages.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
