# BeepWear — Information Architecture

Milestone 3 addendum (Master Prompt Part 3). Site structure, URL scheme, navigation,
search, filtering, and the on-brand error/empty states. This is the map the page
milestones (M4–M10) build against.

## 1. Site map

```
Home (/)
├─ Shop (/beepwear-shop/)                     all products
│  ├─ Men (/mens-watches/)
│  ├─ Women (/womens-watches/)
│  └─ Unisex (/unisex-watches/)
├─ Collections (/collections/)                curated by style
│  ├─ Automatic (/automatic-watches/)
│  ├─ Chronograph (/chronograph-watches/)
│  ├─ Diver (/diver-watches/)
│  ├─ Dress (/dress-watches/)
│  ├─ Pilot (/pilot-watches/)
│  └─ GMT / Travel (/gmt-watches/)
├─ Brands (/brands/)                          brand index → /brands/{brand}/
├─ New Arrivals (/new-arrivals/)
├─ Best Sellers (/best-sellers/)
├─ Limited Editions (/limited-edition/)
├─ Sale (/sale/)
├─ Accessories (/accessories/)                straps, cases, care
├─ About (/about/)
├─ Journal (/journal/)                        buying guides, care, brand stories
├─ Support (/support/)                        hub → contact + policies + FAQ
│  └─ Contact (/contact/)
└─ Account / Cart / Checkout / Wishlist       (Woo + wishlist plugin)
```

**Header nav:** Shop · Collections · Brands · Journal · About · (Search · Account ·
Wishlist · Cart icons). **Mega menu** on Shop/Collections/Brands. **Footer** carries the
full map including policies.

## 2. URL structure

Clean, descriptive, lowercase, hyphenated; no query parameters for canonical pages.

| Page | URL |
|------|-----|
| Shop | `/beepwear-shop/` |
| Men / Women | `/mens-watches/`, `/womens-watches/` |
| Style collections | `/automatic-watches/`, `/chronograph-watches/`, `/diver-watches/`, … |
| Limited editions | `/limited-edition/` |
| Brand index / brand | `/brands/`, `/brands/{brand}/` |
| Product (PDP) | `/product/{product-slug}/` (Woo default; kept for schema/breadcrumb clarity) |
| About / Contact / Journal | `/about/`, `/contact/`, `/journal/` |
| Policies | `/shipping-policy/`, `/returns/`, `/privacy-policy/`, `/terms-and-conditions/` |

WordPress permalinks: **Post name** (`/%postname%/`); WooCommerce product base left at
`/product/`; category base removed where a dedicated landing URL exists (via the SEO/
redirect plugin). Filters use query parameters (`?filter_brand=`) and are `noindex` +
canonicalized to the clean category URL to avoid duplicate-content and thin index pages.

## 3. Search

WooCommerce product search, enhanced:
- **Scope:** products, categories, brands, collections.
- **Autocomplete** with product thumbnail, name, price; keyboard navigable (arrow/enter),
  ARIA combobox semantics.
- **Popular searches** surfaced on focus; **no-results** state suggests popular brands +
  a link to the full shop (never a dead end).
- Implementation: native search first; a lightweight search plugin (e.g., FiboSearch)
  only if native proves insufficient — evaluated against the plugin policy in `PLUGINS.md`.

## 4. Filtering & sorting

Faceted filters on shop/category/brand archives:

**Filter by:** Brand · Price · Movement · Case size · Dial color · Band material ·
Gender · Water resistance · Glass (crystal) type · Availability · New arrival ·
Best seller · Sale · Limited edition.
(All map to the taxonomy/attributes locked in `DATA-MODEL.md`.)

**Sort by:** Popularity · Newest · Price (low→high, high→low) · Alphabetical ·
Customer rating.

Rules: filter URLs are `noindex,follow` + canonical to the base archive; filter state is
keyboard operable and announced to assistive tech; applied filters shown as removable
chips; results update without layout shift.

## 5. Error & empty states (on-brand, never dead ends)

| State | Behavior |
|-------|----------|
| **404** | Branded page: short line in BeepWear voice + search + links to Shop, Collections, Journal. |
| **Search — no results** | "No timepieces match that search." + popular brands + Shop link. |
| **Cart empty** | "Your bag is empty." + New Arrivals + Best Sellers links. |
| **Wishlist empty** | "Nothing saved yet." + link to Shop. |
| **Order failure** | Explains what happened + how to retry/contact support; never a bare error. |
| **Maintenance** | Branded holding page (server-level). |
| **Coming soon** | Development only; removed before launch. |

Each is a `template-parts/` partial styled with the design system; copy lives in
`content/` and follows the voice guide (active, specific, no apology).

## 6. Breadcrumbs & internal linking

- Breadcrumbs on every archive and PDP: `Home / {Category} / {Product}` with
  `BreadcrumbList` schema (owned by Rank Math; owner milestone M5/M6).
- Internal links: PDP → related products + brand page; Journal guides → relevant
  collections; collections cross-link. Every page reachable within three clicks of Home.
