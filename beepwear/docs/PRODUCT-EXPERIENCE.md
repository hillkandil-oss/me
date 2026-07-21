# BeepWear — Product Experience Specification

Master Prompt Part 7. The spec-of-record for the catalog and product experience: PDP
layout, category/brand/collection page layouts, filtering/sorting/search, recommendations,
and the product + Merchant Center review checklists. Owner milestones: **M6** (shop,
category, brand, collection, search) and **M7** (product page). Data model in
`DATA-MODEL.md`; feed detail in `docs/MERCHANT-CENTER.md` (M12).

Governing rule throughout: **accuracy and transparency.** Never fabricate specs, reviews,
identifiers (GTIN/MPN), warranties, or "what's included" items. Omit rather than guess.

## 1. Catalog structure

- **Brands** — WooCommerce native `brand` taxonomy; a page per brand actually sold.
- **Categories** — gender + style + accessories (see `DATA-MODEL.md §2`). Only categories
  that match real inventory.
- **Collections** — dynamic where possible: New Arrivals / Best Sellers are rule-driven;
  named collections (Heritage, Executive, Everyday, Gift, Limited Edition) use a
  `collection` taxonomy so products can be assigned and pages populate automatically.

## 2. Product page (PDP) — layout, top to bottom (M7)

1. **Gallery** — high-res images, zoom, multiple angles, packaging + lifestyle shots,
   optional video / 360°. Images must depict the actual item (no misleading AI images).
2. **Summary** — brand, model, reference number, price, availability, short description,
   variation selector, quantity, **Add to Cart**, Wishlist, Compare.
3. **Highlights** — concise, accurate bullets (case material, crystal, movement, water
   resistance, strap, warranty) — only true features.
4. **Detailed description** — original copy: design, craftsmanship, materials, function,
   who it suits, care. Never paste manufacturer copy verbatim without rights.
5. **Technical specifications** — clean table from `DATA-MODEL.md §8`. Verified fields only.
6. **What's included** — real package contents only.
7. **Shipping** — processing time, methods, tracking, destinations + link to full policy.
8. **Returns & refunds** — summary + link to full policy.
9. **Warranty** — duration, provider, coverage, exclusions, claim process (only if offered).
10. **Payment methods** — only options customers can actually use.
11. **Related products** — same brand/collection/category/price band.
12. **Recently viewed** — from the visitor's browsing history.
13. **Reviews** — genuine only: stars, text, date, verified-purchase indicator. Hidden
    until real reviews exist.
14. **FAQ** — product-appropriate (authenticity, warranty, international shipping, returns,
    care) → feeds `FAQPage` schema.

**PDP SEO:** unique title + meta, clean URL `/product/{descriptive-slug}/`, optimized alt
text, valid **Product** schema (brand, sku, gtin/mpn when real, offers, availability),
breadcrumbs, internal links to brand/collection/buying guide.

## 3. Variations

Support real variants (strap color, dial color, case finish/size). Selecting a variation
updates image, price, availability, and SKU. No invented variants (Merchant Center flags
mismatches).

## 4. Category page layout (M6)

Hero banner · category description (SEO intro) · filter sidebar · sort · product grid ·
pagination · buying-guide section · FAQ · related categories · newsletter · internal links.

## 5. Brand page layout (M6)

Brand hero · history · philosophy · signature collections · featured products · buying
guide · FAQ · related articles · internal links. **All content original.**

## 6. Collection page layout (M6)

Luxury hero · overview · featured products · filters · buying recommendations · related
collections · educational content · newsletter.

## 7. Filtering, sorting, search

**Filter by:** Brand · Price · Movement · Case size · Case material · Band material · Band
color · Dial color · Water resistance · Glass (crystal) type · Collection · Availability ·
Style · Gender · New arrival · Best seller · Sale · Limited edition. (All map to the
taxonomy/attributes in `DATA-MODEL.md`.)

**Sort by:** Featured · Newest · Price low→high · Price high→low · Best selling · Highest
rated · Alphabetical.

**Search:** instant suggestions across product names, brands, reference numbers, categories,
collections, and articles; helpful no-results suggestions (never a dead end). Detail in
`INFORMATION-ARCHITECTURE.md §3`.

Filter URLs are `noindex,follow` + canonical to the base archive (duplicate-content guard).

## 8. Inventory

WooCommerce manages stock quantity, backorders (if enabled), out-of-stock visibility, low-
stock alerts, SKUs, and sync. Only accurate availability is shown — and it must match the
feed exactly.

## 9. Recommendations, cross-sells, up-sells, comparison

- **Recommendations:** by brand / category / browsing / price band / complementary
  accessories. No unrelated suggestions.
- **Cross-sells (cart):** straps, travel cases, boxes, cleaning kits, gift wrap — only if
  actually stocked.
- **Up-sells (PDP):** premium alternatives, shown without disrupting the flow.
- **Comparison (optional):** simple, readable table — specs, movement, case size, water
  resistance, price, materials, features.

## 10. Product image standards

Primary, front, rear, side, close-up detail, packaging (if available), lifestyle;
zoom-ready resolution; consistent background; no watermarks; no misleading AI images.

## 11. Final product review checklist (M7 gate — per product)

- [ ] Information accurate; images match the product; price correct; availability current.
- [ ] Specifications complete; identifiers (GTIN/MPN) accurate where available, never invented.
- [ ] SEO fields filled; Product schema validates; links work.
- [ ] Correct categories; appears in relevant collections.
- [ ] Merchant Center attributes complete where applicable.

## 12. Google Merchant Center product checklist (M12 gate — per product in feed)

- [ ] Clear, accurate title (no promotional text in titles/descriptions meant for feeds).
- [ ] Original description; high-quality images; price matches site; availability accurate.
- [ ] Consistent brand; valid identifiers when available; publicly accessible HTTPS page.
- [ ] Visible return + shipping info; functional Add to Cart; no misleading claims.
- [ ] Product schema implemented correctly.
