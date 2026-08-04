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

### Removed
- Unrelated prior project (BeepWear watch store) — recoverable from git history.
