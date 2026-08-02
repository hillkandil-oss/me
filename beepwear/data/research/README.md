# Research scrape — containersolutionscs.de

Product catalogue scraped from `containersolutionscs.de` (WooCommerce Store API,
public) on 2026-08-02 for research + re-import prep, using
`beepwear/tools/store-scraper/`.

## Files

| File | What it is |
|------|-----------|
| `containersolutionscs-products.json` | Raw normalized scrape (118 products, full data) |
| `containersolutionscs-products.csv` | Flat one-row-per-variant table (all fields) |
| `containersolutionscs-mc-import.csv` | **Import this** — 49-col WooCommerce importer CSV, Merchant-Center-oriented |
| `containersolutionscs-mc-audit.csv` | Per-product brand + description status + recommendation |
| `brands.txt` | Manufacturer brands to detect/keep (feeds the Brands column) |
| `store-terms.txt` | Source-store identity to strip from copy (safety net) |
| `description-rewrites.json` | Original rewritten copy for the 7 formerly near-duplicate products |

## What was done for the import file

- **Manufacturer brands kept** and written to the WooCommerce **Brands** column
  (58/118 products have a brand; Google Merchant Center needs `brand`).
- **Source store removed** — product permalinks dropped (External URL blank), and
  the store name/domain scrubbed from copy (it did not actually appear in any
  title/description, but the scrub runs anyway).
- **Links removed** from descriptions (none were present after HTML stripping).
- **GTIN left blank** — never invent identifiers. For the 60 brand-less products,
  set **"identifier exists = no"** in the Google feed.
- **Prices** carried through in EUR; regular/sale split when a discount exists.
- **Images** kept as source-CDN URLs — WooCommerce sideloads them into your media
  library on import, so they end up re-hosted under your own domain.

## Honest Merchant Center status (read before submitting)

Per `beepwear/docs/MERCHANT-CENTER-CSV-AUDIT.md`, the biggest suspension risks are
**duplicate content** and **copied descriptions**. For this scrape:

- The 7 previously near-duplicate descriptions (Ifor Williams TA5 trailer
  size-variants + one container pair) have been **rewritten as original, distinct
  copy** — see `description-rewrites.json`. The audit now shows **118/118 unique,
  0 near-duplicate** (6-word shingle Jaccard < 0.30 between all pairs).
- The **other 111 descriptions are unique within this set** — but "unique here" is
  not "original." They are still the **source store's own words**. Before submitting,
  spot-check for copied manufacturer/competitor copy (copyright) and rewrite as
  needed. Prices, availability and images must match your live product pages.

The rewritten copy is applied at build time via `--desc-overrides
description-rewrites.json` — the raw scrape JSON is left untouched, so the rewrite
is reproducible and auditable.

## Reproduce

```bash
cd beepwear/tools/store-scraper
python3 store_scraper.py https://containersolutionscs.de --platform woocommerce \
    --format json -o ../../data/research/containersolutionscs-products.json
python3 build_mc_import.py ../../data/research/containersolutionscs-products.json \
    --brands-file ../../data/research/brands.txt \
    --store-terms-file ../../data/research/store-terms.txt \
    --desc-overrides ../../data/research/description-rewrites.json \
    --out-csv   ../../data/research/containersolutionscs-mc-import.csv \
    --out-audit ../../data/research/containersolutionscs-mc-audit.csv
```
