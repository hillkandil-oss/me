# BeepWear — Review Log

Milestone briefs and review-gate sign-offs. Each entry records real findings; blocking
items are fixed before sign-off, non-blocking items carry an owner milestone.

---

## Milestone 1 — Project Planning · ✅ signed off

**Deliverables:** `README.md`, `docs/PROJECT-GOVERNANCE.md` (operating model, review
gates, milestone plan of record, feature workflow).
**Acceptance:** governance adopted; stack reconciled to classic WordPress; milestones
sequenced. Met.

---

## Milestone 2 — Brand Identity · ✅ signed off (1 action item)

**Deliverables:** `docs/BRAND.md` — palette, typography, spacing, motion, imagery, voice.

| Gate | Result | Notes |
|------|--------|-------|
| Design | ✅ | Coherent luxury system; avoids AI-default cream+terracotta and Inter/Space Grotesk. |
| SEO | n/a | Doc-only milestone. |
| Accessibility | ✅ | Contrast rule codified: gold never carries body text; use `--bw-bronze` (≈4.7:1). |
| Performance | ✅ | Self-hosted font strategy specified. |
| Merchant Center | ✅ | Imagery rule bars AI images as primary product photos. |
| QA | ✅ | Tokens are internally consistent with `style.css`. |

**Action item → M2b:** deliver logo concepts + favicon/app icons (currently referenced
by JSON-LD but not yet designed).

---

## Milestone 3 — Architecture · 🟡 in progress (foundation reviewed)

**Deliverables so far:** child theme (`style.css`, `functions.php`, `assets/js/beepwear.js`),
asset scaffolding. Remaining for M3: data model (categories, attributes, variations),
plugin list, and a `header.php`/`footer.php` or Elementor Theme Builder decision.

### Review of the foundation

| Gate | Result | Findings |
|------|--------|----------|
| Design | ✅ | WooCommerce grid/PDP/forms styled to tokens; square corners, hairlines, roomy grid. |
| SEO | 🟡 | Organization/WebSite/Product JSON-LD emitted and guarded against SEO-plugin duplication. **Open:** BreadcrumbList schema (owner M5/M6); Product schema lacks `brand`, `gtin`, `aggregateRating` (owner M7/M12). |
| Accessibility | ✅ | `:focus-visible` outlines global; reduced-motion disables transforms/reveals; reveal falls back to visible without IntersectionObserver. |
| Performance | 🟡 | Fonts preloaded with `crossorigin`. **Open:** ship real subset woff2 (latin/latin-ext) — placeholders only; verify no CLS from font swap on live. |
| Security | 🟡 | `ABSPATH` guard; output via `wp_json_encode`/`esc_url`. **Open:** hardening checklist (owner M14) — disable XML-RPC, limit login, security headers. |
| Merchant Center | 🟡 | Schema foundation present. **Open:** availability/shipping/returns surfacing and feed (owner M12). |
| QA | ✅ | `php -l functions.php` passes; CSS selectors namespaced (`.bw-`, scoped Woo overrides) to avoid cascade collisions. |

**Not signed off yet** — M3 completes when the data model, plugin list, and
header/footer strategy land and the open SEO/Perf items above are assigned.

### PM brief — Milestone 3 remainder

```
Objectives   Finish the architecture: define the commerce data model and the
             template strategy so page milestones (4–10) have a stable base.
Tasks        1. Data model: watch categories, global attributes (brand, movement,
                case size/material, water resistance, strap), variation strategy.
             2. Plugin list with purpose + Merchant Center/SEO/security rationale.
             3. Template strategy: Elementor Theme Builder (header/footer/PDP) vs
                theme PHP templates — decide and document.
             4. Assign open SEO (breadcrumb/product-schema) and Perf (fonts) items.
Dependencies BRAND.md (done); WooCommerce installed on target (deploy-time).
Risks        Attribute schema churn later forces product re-tagging → lock taxonomy now.
Deliverables docs/DATA-MODEL.md, docs/PLUGINS.md, template decision in this log.
Acceptance   Taxonomy stable; every planned page maps to a template; open items owned.
```
