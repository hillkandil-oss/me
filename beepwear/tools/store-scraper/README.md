# Store Scraper — Shopify & WooCommerce catalog extractor

A single-file, dependency-free Python tool that pulls product catalogs from the
**public** product APIs that Shopify and WooCommerce stores expose by default.
Built for BeepWear catalog research and import prep, but works against any store.

- **Shopify** → `GET /products.json` (unauthenticated, paginated)
- **WooCommerce** → `GET /wp-json/wc/store/v1/products` (Store API, unauthenticated)
- **WooCommerce (authenticated)** → `GET /wp-json/wc/v3/products` (REST API, richer data — needs a key/secret)

Platform is auto-detected. Output is **JSON**, a **flat CSV** (one row per variant),
or a **WooCommerce-importer CSV** you can feed straight into
*WooCommerce → Products → Import*.

## Requirements

Python 3.8+. No `pip install` needed — standard library only.

## Usage

```bash
# Full normalized JSON
python3 store_scraper.py https://somebrand.com --format json -o catalog.json

# Flat CSV, one row per variant (good for spreadsheets)
python3 store_scraper.py https://somebrand.com --format csv -o catalog.csv

# WooCommerce importer CSV (drop into WooCommerce → Products → Import)
python3 store_scraper.py https://somebrand.com --format woo -o woo-import.csv

# Force platform + use WooCommerce REST API keys for richer data
python3 store_scraper.py https://shop.example.com \
    --platform woocommerce --wc-key ck_xxx --wc-secret cs_xxx --format json
```

### Options

| Flag | Default | Purpose |
|------|---------|---------|
| `--platform` | `auto` | `auto` \| `shopify` \| `woocommerce` |
| `--format` | `json` | `json` \| `csv` \| `woo` |
| `-o, --output` | stdout | Output file path |
| `--limit` | `0` (all) | Stop after N products |
| `--max-pages` | `1000` | Safety cap on pages fetched |
| `--delay` | `0.5` | Seconds between page requests (be polite) |
| `--timeout` | `30` | Per-request timeout (seconds) |
| `--wc-key` / `--wc-secret` | – | WooCommerce REST API credentials |
| `--quiet` | off | Silence progress logging on stderr |

## Output schema (JSON)

```jsonc
{
  "platform": "shopify",
  "source_url": "https://somebrand.com",
  "id": "111",
  "handle": "aviator-chrono",
  "url": "https://somebrand.com/products/aviator-chrono",
  "title": "Aviator Chrono",
  "brand": "BeepWear",
  "product_type": "Watches",
  "tags": ["pilot", "chrono"],
  "description": "A bold pilot watch.",
  "images": ["https://cdn.example.com/av.jpg"],
  "variants": [
    { "id": "1", "title": "Leather", "sku": "AV-L", "price": "499.00",
      "compare_at_price": "599.00", "currency": null,
      "options": { "Strap": "Leather" }, "available": true }
  ]
}
```

Notes:
- Shopify `/products.json` does not include a currency code; the `currency` field is
  `null` there. The WooCommerce Store API does include it.
- WooCommerce Store API returns prices in **minor units** (e.g. cents); the tool
  converts them to decimal using each product's `currency_minor_unit`.
- WooCommerce "brand" is a plugin taxonomy and is not exposed by the Store API, so
  `brand` comes back empty on that path. Use the REST API (`--wc-key/--wc-secret`)
  or the store's brand plugin export if you need it.

## Companion scripts: brand handling + Merchant Center import

Two helpers turn a raw scrape into a re-import-ready catalogue:

- **`strip_brands.py`** — remove brand names (and links) from a scrape, e.g. to
  anonymize titles/descriptions.
  ```bash
  python3 strip_brands.py scraped.json --brands-file brands.txt --format csv -o clean.csv
  ```

- **`build_mc_import.py`** — build a Merchant-Center-oriented WooCommerce import CSV.
  It **keeps** manufacturer brands (and fills the WooCommerce *Brands* column, which
  Google Merchant Center needs), **removes** the source store's identity + links +
  permalinks, leaves GTIN blank (never invents identifiers), and writes an **audit
  CSV** that flags duplicate / near-duplicate / empty descriptions — the top
  Merchant Center suspension risks.
  ```bash
  python3 build_mc_import.py scraped.json \
      --brands-file brands.txt --store-terms-file store-terms.txt \
      --out-csv mc-import.csv --out-audit mc-audit.csv
  ```
  Near-duplicate detection uses 6-word shingle Jaccard similarity (≥0.30). The
  output CSV matches this repo's proven 49-column schema
  (`beepwear/data/products-mc-cleaned.csv`) so it imports directly. See
  `beepwear/data/research/README.md` for a worked example.

## Running in Claude Code on the web

This environment's egress proxy blocks arbitrary external domains by default, so the
scraper cannot reach a live store from a web session unless you **allowlist the target
domain** for the environment (claude.ai/code → environment → Network access) and start
a **new** session. Otherwise, run the tool from a machine with normal network access.

## Please scrape responsibly

These endpoints are public by design, but only scrape stores you're authorized to,
respect each site's Terms of Service and `robots.txt`, and keep `--delay > 0` so you
don't overload a store. You are responsible for how you use the data.
