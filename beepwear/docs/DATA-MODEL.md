# BeepWear — Commerce Data Model

Milestone 3. The WooCommerce taxonomy for a multi-brand luxury watch retailer. Locking
this now prevents costly product re-tagging later. WooCommerce is the source of truth.

## 1. Product types

- **Simple product** — a single timepiece SKU (most listings).
- **Variable product** — one model sold with genuine purchasable variants only
  (e.g., bracelet vs leather strap, or dial color). Do **not** invent variants that
  aren't real, distinct SKUs — Merchant Center penalizes mismatched variants.

Each product carries: title, brand, SKU, GTIN/UPC (when the manufacturer provides one),
price, stock status/quantity, short description (specs summary), long description
(story + care), gallery, and the attributes below.

## 2. Product categories (`product_cat`, hierarchical — navigation & merchandising)

Categories are how customers browse; keep them shallow and meaningful.

```
Watches
├─ Men
├─ Women
└─ Unisex

Style
├─ Dress
├─ Sport
├─ Diver
├─ Chronograph
├─ Pilot / Aviator
├─ Field
└─ GMT / Travel

Editorial
├─ New Arrivals
├─ Best Sellers
└─ Gifts
```

A product may sit in one gender + one or more style categories. "Editorial" categories
are merchandising surfaces populated by rules, not core classification.

## 3. Brand (`brand` taxonomy)

Use WooCommerce's **native Brands** taxonomy (WooCommerce 9.6+) — one term per
manufacturer. Brand drives the mega-menu brand list, brand landing pages, faceted
filtering, `Product.brand` schema, and the Merchant Center `brand` attribute (required).
Never list a brand BeepWear is not authorized to sell.

## 4. Global attributes (`pa_*`) — filtering, specs, variations

Global (not per-product) so filters stay consistent and Merchant Center feed mapping is
clean.

| Attribute (`pa_`) | Example terms | Purpose |
|---|---|---|
| `movement` | Automatic, Manual, Quartz, Solar, Kinetic | Filter, spec, buyer education |
| `case-material` | Stainless Steel, Titanium, Gold, Two-Tone, Ceramic, Bronze | Filter, spec |
| `case-size` | 34mm, 36mm, 38mm, 40mm, 42mm, 44mm | Filter (fit), spec |
| `dial-color` | Black, White, Blue, Silver, Green, Champagne | Filter, variation axis |
| `strap-material` | Leather, Steel Bracelet, Rubber, NATO, Mesh | Filter, variation axis |
| `water-resistance` | 30m, 50m, 100m, 200m, 300m+ | Filter (use case), spec |
| `crystal` | Sapphire, Mineral, Acrylic | Spec, trust signal |
| `features` | Date, Chronograph, GMT, Moonphase, Skeleton | Filter, spec |
| `gender` | Men, Women, Unisex | Mirrors category for filtering |

**Variation axes** are limited to `strap-material`, `dial-color`, and `case-size` when a
model genuinely ships in those options. Everything else is descriptive (used for filters
and specs, not variations).

## 5. Custom post types & taxonomies

Minimal, per the "no unnecessary tech" rule:

- **Blog / Journal** → native `post` with a `Journal` category and sub-categories for
  **Buying Guides**, **Watch Care**, **Brand Stories**. No CPT needed.
- **No custom CPTs** for now. Collections/lookbooks are Elementor landing pages driven by
  category/brand queries. Revisit only if editorial needs outgrow pages.

## 6. Attribute → Merchant Center feed mapping (preview; finalized in M12)

| Merchant Center attribute | Source |
|---|---|
| `id`, `title`, `description`, `link`, `image_link` | product core |
| `price`, `availability` | WooCommerce price / stock |
| `brand` | `brand` taxonomy (**required**) |
| `gtin` / `mpn` | product SKU / GTIN field |
| `condition` | "new" (default; used/vintage flagged explicitly if ever sold) |
| `google_product_category` | "Apparel & Accessories > Jewelry > Watches" (201) |
| `shipping`, `tax` | WooCommerce shipping zones / tax classes |
| `color`, `material`, `size` | `dial-color` / `case-material` / `case-size` |

## 7. Data-entry rules (Merchant Center & trust)

- Every product **must** have: brand, ≥1 real product photo, price, stock status,
  accurate short description, and a GTIN when one exists.
- No fabricated specs, reviews, ratings, or certifications.
- Prices and availability on the page must match the feed exactly.
