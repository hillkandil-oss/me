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
├─ GMT / Travel
├─ Skeleton
└─ Moonphase

Accessories
├─ Replacement Straps
├─ Watch Boxes
├─ Travel Cases
└─ Care Products

Editorial (rule-driven surfaces, not core classification)
├─ New Arrivals
├─ Best Sellers
├─ Limited Editions
└─ Gifts
```

A product may sit in one gender + one or more style categories. "Editorial" categories are
merchandising surfaces populated by rules.

**Movement-based collections** (Automatic, Quartz, Mechanical) are **not** separate
categories — `movement` is already a global attribute (§4). Their landing pages
(`/automatic-watches/`, etc.) are attribute-driven collection pages, avoiding duplicate
taxonomy. Same for material/complication collections. Create only categories that map to
products actually offered (Part 5).

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
| `band-color` | Black, Brown, Tan, Silver, Gold, Blue | Filter, variation axis |
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
- **`collection` taxonomy** (product taxonomy) → for **named** collections (Heritage,
  Executive, Everyday, Gift, Limited Edition). Products are assigned terms so collection
  pages populate dynamically. Rule-based collections (New Arrivals = recent, Best Sellers =
  sales) stay query-driven and need no term.
- **No custom CPTs** for now. Collection/brand pages are Elementor templates driven by
  taxonomy/query. Revisit only if editorial needs outgrow pages.

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

## 8. Product specification fields (PDP)

The PDP renders a specifications table from these fields (Part 5). Global attributes
(§4) drive filtering; the remaining descriptive fields are stored as product custom fields
(a "Specifications" field group) so they display consistently without polluting the filter
UI. Only populate a field when the value is accurate — omit rather than guess.

| Field | Source | Notes |
|-------|--------|-------|
| Brand | `brand` taxonomy | Required |
| Model | product title / field | |
| Reference Number | custom field | Manufacturer reference |
| Movement Type | `pa_movement` | Filterable |
| Movement Origin | custom field | **Only if accurate** |
| Case Material | `pa_case-material` | Filterable |
| Case Diameter | `pa_case-size` | Filterable |
| Case Thickness | custom field | mm |
| Lug Width | custom field | mm |
| Crystal Type | `pa_crystal` | |
| Water Resistance | `pa_water-resistance` | Filterable |
| Dial Color | `pa_dial-color` | Filterable / variation axis |
| Bezel Material | custom field | |
| Strap Material | `pa_strap-material` | Filterable / variation axis |
| Clasp Type | custom field | |
| Power Reserve | custom field | If applicable (mechanical) |
| Weight | custom field | grams |
| Warranty | custom field / global | e.g., store/manufacturer term |
| Country of Manufacture | custom field | **Only if accurate** |

"What's included" (box, papers, extra strap, tools) is a separate PDP field group.
