# kaisercontainers — E-Commerce Build

Deliverables for **kaisercontainers** (https://kaisercontainers.de), a brick-and-mortar
shipping-container retailer in Duisburg (Homberg/Baerl), Germany. German-language store,
Euro pricing, prepared (not guaranteed) for Google Merchant Center review.

> **Working mode:** deliverables are built in this repo and deployed by the store owner to
> the existing WordPress / Flux / WooCommerce install. Nothing here fabricates business,
> legal, location, contact, review, or product data — gaps live in
> [`REQUIRED-FROM-OWNER.md`](REQUIRED-FROM-OWNER.md).

## Layout

| Path | What it holds |
|---|---|
| `REQUIRED-FROM-OWNER.md` | Every fact that must be verified before publication |
| `docs/design-system.md` | Brand palette, type, spacing, components |
| `docs/merchant-center-readiness.md` | Readiness audit + prioritised action plan |
| `content/` | German page copy, ready to paste into WordPress |
| `content/policies/` | Versand, Rückgabe, Datenschutz, AGB, Impressum, … |
| `theme/schema/` | LocalBusiness / Organization / Product JSON-LD |
| `theme/snippets/` | Header contact bar, footer, reusable HTML/CSS |
| `data/` | Merchant Center product-feed template (German columns) |
| `prototype/` | Static visual prototype of the storefront |
| `assets/` | Logo, icons, imagery placeholders |

## Non-negotiables (from the brief)

- Google Merchant Center approval **cannot be guaranteed**.
- No fabricated address, phone, hours, photos, reviews, certifications, GTINs, or claims.
- Reuse the installed theme + demo as the foundation; do not rebuild needlessly.
- German legal pages (**Impressum**, Datenschutz, AGB, Widerruf) are mandatory.

## Status

See [`CHANGELOG.md`](CHANGELOG.md). Current phase: **Foundation**.
