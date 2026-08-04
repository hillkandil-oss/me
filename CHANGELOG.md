# Changelog — kaisercontainers build

All notable changes to the deliverables in this repo.

## [Unreleased]

### Added
- Project scaffold: `content/`, `docs/`, `theme/`, `data/`, `prototype/`, `assets/`.
- `README.md` — repo map + non-negotiables.
- `REQUIRED-FROM-OWNER.md` — verified-fact checklist (blocks publication where 🔴).

### Decisions
- **Working mode:** build-in-repo; owner deploys to the WordPress/Flux/WooCommerce install.
- **Store phone:** held as internal placeholder — brief's number is a Hamburg code but the
  store is in Duisburg; owner to provide the correct number.
- **Condition:** containers sold **both new and used** → per-product `condition` attribute.

### Audited (live site, read-only)
- Authenticated to live WordPress via Application Password (admin). Reachable from sandbox.
- Recorded findings in `docs/site-audit.md`: theme **Tranzix v1.0.1**, WooCommerce +
  Elementor + CF7 + LiteSpeed on Hostinger; **20 real German products** + German categories
  already present; config wrong for DE (en_US/USD/US:CA/GMT0, no homepage); legal pages
  missing; menus unassigned; product feed gaps (no dims/condition/brand/GTIN).

### Built (live site, staged as drafts / unassigned)
- Store config: Europe/Berlin, EUR (German format), DE-NRW, Duisburg/47138, tagline.
- German Contact Form 7 → info@kaisercontainers.de + customer confirmation.
- 10 pages (draft): Startseite, Kontakt, Über uns, Impressum, Datenschutz, AGB,
  Widerruf, Versand, Zahlung, FAQ — with 〔BITTE BESTÄTIGEN〕 markers, nothing fabricated.
- Navigation menu (id 28) with Container dropdown (4 real categories) — not yet assigned.
- Zustand (Neu/Gebraucht) attribute on all 20 products (17 neu, 3 gebraucht).
- Rank Math SEO installed + active (finish config in GUI; see go-live checklist §D2).
- German descriptions on all 9 real product categories.
- WooCommerce: guest checkout + login reminder + account registration enabled;
  "Deutschland" shipping zone with **store pickup** ("Abholung in Duisburg", enabled).
- Note: woocommerce_terms_page_id (AGB) won't persist via REST → set in GUI at go-live.

### Delivered (repo)
- design-system.md + brand.css; header/footer snippets; merchant-center-feed.csv (20 rows)
  + feed audit; localbusiness.jsonld + schema-jsonld.php; product-dimensions-reference.md;
  go-live-checklist.md; merchant-center-readiness.md (NOT READY — owner facts pending).

### Removed
- Unrelated prior project (BeepWear watch store) — recoverable from git history.
