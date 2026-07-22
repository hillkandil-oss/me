# BeepWear — Product CSV: Merchant Center Compliance Audit

Audit + cleaning of the supplied WooCommerce export (1,490 products). Goal: a
submit-ready subset that won't trigger a Merchant Center suspension. Files:
`data/products-mc-cleaned.csv` (import this) and `data/products-mc-audit.csv`
(per-row keep/drop + reason).

## Result

| | Count |
|---|---|
| Products in source | 1,490 |
| **Kept (compliant candidates)** | **269** |
| Dropped | 1,221 |

### Why products were dropped

| Reason | Count | Note |
|--------|------|------|
| Duplicated description (shared across products) | 1,003 | Generic filler reused on many products — Google prohibits duplicate content. Can't be kept without **original, per-product** descriptions. |
| Non-watch / no product signal | 152 | Not timepieces. |
| Demo/junk category | 61 | Plants, bakery, stuffed animals, "Dokan" multivendor demo data. |
| Empty description | 5 | No content. |

The dropped products aren't compliant **as written** — most need original descriptions
before they can join the feed. Nothing was dropped for authenticity (confirmed by the owner).

## What was fixed on the kept 269

- **Brands column populated** from the product name/category (222 of 269). **47 still need a
  brand** assigned manually — flagged in the audit file.
- **Categories cleaned** — brand-as-category and junk tokens removed; "Watches" ensured.
- Placeholder/duplicate/junk removed so the remaining set is unique and watch-only.
- Standard WooCommerce columns preserved — the file imports directly.

## Still required before/at submission (owner)

1. **Verify descriptions are original + accurate.** "Unique in this file" ≠ "original" — spot-
   check the kept 269 for copied manufacturer copy (copyright) and factual accuracy. Rewrite
   any that are lifted verbatim.
2. **Assign brands to the 47 unbranded** kept products (Merchant Center requires `brand`).
3. **Authenticity documentation** — keep proof of authorized/legitimate sourcing for the
   luxury brands (Rolex ×103, Omega, Ulysse Nardin, TAG Heuer, Zenith, Tudor, etc.). Google
   may request it; heavy-scrutiny brands can still be manually reviewed.
4. **GTIN/UPC/EAN** — none present. Not fatal, but add them where they genuinely exist
   (set "identifier exists = no" in the feed for those without). **Never invent identifiers.**
5. **Prices/availability** must match the live product pages exactly.
6. **Product images** must accurately depict each watch (no stock-photo mismatches).

## Import notes

- Import `products-mc-cleaned.csv` via WooCommerce → Products → Import (match columns; the
  export format maps automatically).
- Set the WooCommerce **Brands** taxonomy to the populated column.
- Configure Google product category **Apparel & Accessories > Jewelry > Watches (201)** in the
  Google for WooCommerce feed; condition = new.
- Then run the per-product checklist in `MERCHANT-CENTER.md §12`.

> Honest bottom line: the file yields ~269 submit-ready candidates, not 1,490. To sell the
> larger catalogue, those products need **original descriptions** — which require real,
> per-product data, not generated filler.
