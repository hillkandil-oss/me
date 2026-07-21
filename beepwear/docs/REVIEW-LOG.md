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

## Milestone 3 — Architecture · ✅ signed off (open items owned by later milestones)

**Deliverables:** child theme (`style.css`, `functions.php`, `assets/js/beepwear.js`),
`docs/ARCHITECTURE.md`, `docs/DATA-MODEL.md`, `docs/PLUGINS.md`.
**Template decision (resolved):** Elementor Pro Theme Builder renders header, footer,
shop archive, single product, and blog templates; the child theme supplies the design
system, JSON-LD, and accessibility/performance helpers; cart/checkout/account stay on
WooCommerce's own flow. Recorded in `ARCHITECTURE.md §2`.
**Schema de-duplication (resolved):** Rank Math owns Product/Breadcrumb schema in
production; set `BEEPWEAR_EMIT_SCHEMA=false`; theme schema is the fallback. `PLUGINS.md`.
**Data model (resolved & locked):** product types, categories, native `brand` taxonomy,
nine global attributes, variation axes limited to strap/dial/case-size, no custom CPTs.
`DATA-MODEL.md`.

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

**Open items carried forward (owned):** BreadcrumbList schema → M5/M6; Product schema
`brand`/`gtin`/`aggregateRating` → M7/M12; real subset woff2 files → M4 (needed to render
homepage); security-hardening execution → M14; MC feed + availability/shipping/returns
surfacing → M12. All tracked; none block M3 architecture sign-off.

**Acceptance met:** taxonomy locked; every planned page (M4–M10) maps to a template in
`ARCHITECTURE.md §2`; plugin stack chosen with rationale; open items assigned.

### PM brief — Milestone 4 (Homepage) · next

```
Objectives   Design and build the BeepWear homepage — the brand thesis — as an Elementor
             page plus the child-theme sections/CSS it depends on.
Tasks        1. Wireframe the homepage section stack (hero, featured collections, brand
                strip, editorial feature, trust/service band, journal teaser, newsletter).
             2. Write original hero + section copy (Content lens).
             3. Build sections as child-theme CSS + an Elementor build guide.
             4. Prepare Higgsfield hero/editorial image prompts (no product misrepresentation).
             5. Supply real subset woff2 fonts so type renders as designed.
Dependencies BRAND.md, ARCHITECTURE.md, DATA-MODEL.md (done); fonts (this milestone).
Risks        Hero imagery not yet produced → design with art-directed placeholders +
             documented prompts; swap real assets before launch.
Deliverables docs/ELEMENTOR-BUILD-GUIDE.md (homepage), content/homepage.md, homepage CSS,
             docs/IMAGE-PROMPTS.md (hero/editorial).
Acceptance   Passes all six gates; renders premium on mobile/desktop; no placeholder copy.
```
