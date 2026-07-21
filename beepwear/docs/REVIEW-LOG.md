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

### M2 revision — Part 4 design system (client-pinned)

Master Prompt Part 4 pinned specifics that override the initial creative choices; the
brief's own words win. Design system realigned and reimplemented (theme v0.3.0):

- **Palette** → Luxury Black `#141310` · Pure White · Champagne Gold `#C2A15C`, with
  charcoal/stone/silver supporting and off-white/light-gray grounds. Replaces the earlier
  warm-porcelain ground. Named semantic colors adopted (crimson/emerald/amber/royal blue).
- **Body type** → Manrope (was Jost); display stays Cormorant Garamond. Font references,
  preload, and README updated.
- **Buttons** → three variants (primary/secondary/ghost) with `4px` radius per Part 4;
  cards/images stay square.
- **Contrast re-audit** — bright champagne fails as text on white (≈2.4:1); rule updated to
  use `--bw-champagne-deep` (≈4.6:1) for gold text/links on white, bright gold for large/
  non-text only. Design + Accessibility gates re-pass.

Component specs (cards, header, trust band, footer, mega menu) captured in BRAND.md and
built in M4/M5.

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

### M3 addendum — Part 3 standards integrated

Development standards from Master Prompt Part 3 folded into the architecture without
reopening sign-off (additive, no contradictions):

- **Modular theme structure** — `functions.php` refactored to a thin bootstrap loading
  `/inc` modules (`setup`, `enqueue`, `woocommerce`, `schema`); `/template-parts` and
  `/templates` scaffolded per the required folder layout. All PHP re-linted clean. v0.2.0.
- **Information architecture** — `docs/INFORMATION-ARCHITECTURE.md`: site map, clean URL
  scheme, header/mega-menu/footer nav, search, faceted filters + sort, on-brand error/
  empty states, breadcrumb/internal-linking rules. Filter URLs `noindex` + canonical to
  base archive (duplicate-content guard).
- **Plugin list reconciled** — added Google Site Kit, WP Mail SMTP, Redirection, Broken
  Link Checker; documented why no separate image-optimization plugin (LiteSpeed covers it).
- **Standards adopted** — WordPress Coding Standards / PSR where applicable; security
  (2FA, DB-prefix, disable file editing, secure REST) and logging/monitoring specified in
  `ARCHITECTURE.md` for execution in M14.

### M5 addendum — Part 5 page inventory integrated

Master Prompt Part 5 (complete site/page structure) captured as the build backbone:

- **`docs/PAGE-INVENTORY.md`** — every required page with sections, content source, and
  owner milestone: global chrome, the 15-section homepage order, commerce templates
  (shop/category/brand directory + brand/collection/PDP/cart/checkout/order/account/
  wishlist/search), content pages (about/support/contact/journal + article template),
  legal + customer-policy + trust pages, buying guides, categorized FAQ, error/empty
  states, internal-linking rules, and the pre-launch structure-review checklist.
- **`DATA-MODEL.md`** — categories expanded (Accessories: straps/boxes/cases/care;
  Skeleton/Moonphase styles; Limited Editions as editorial); movement collections kept
  attribute-driven (no duplicate taxonomy); added §8 **product specification fields** for
  the PDP (reference, movement origin, case thickness, lug width, bezel, clasp, power
  reserve, weight, country — accuracy-gated), mapping to attributes vs custom fields.
- **Nav reconciled** — Part 5's 12-item primary nav grouped into a clean top bar + mega
  menu (`INFORMATION-ARCHITECTURE.md §1`); full set in the footer.

### PM brief — Milestone 4 (Homepage) · next

```
Objectives   Build the BeepWear homepage — the 15-section stack (PAGE-INVENTORY §B) — as
             an Elementor page plus the child-theme sections/CSS and original copy it needs.
Tasks        1. Wireframe the 15 sections in order (hero → featured collections → featured
                brands → best sellers → new arrivals → staff picks → why BeepWear →
                editorial banner → testimonials → latest articles → newsletter → footer).
             2. Write original hero + section copy in BeepWear voice (Content lens).
             3. Build reusable sections as child-theme CSS + template-parts + an Elementor
                build guide; Woo-driven rails (best sellers / new arrivals) documented.
             4. Higgsfield prompts for hero + editorial banner (no product misrepresentation).
             5. Supply real subset woff2 (Cormorant Garamond + Manrope) so type renders true.
             6. Announcement bar as an admin-configurable theme feature.
Dependencies BRAND.md, ARCHITECTURE.md, DATA-MODEL.md, PAGE-INVENTORY.md (done); fonts.
Risks        Hero/editorial imagery not yet produced → design with art-directed placeholders
             + documented prompts; swap real assets before launch. Testimonials/ratings show
             only when genuine — omit until real reviews exist.
Deliverables docs/ELEMENTOR-BUILD-GUIDE.md (homepage), content/homepage.md, homepage CSS +
             template-parts, docs/IMAGE-PROMPTS.md, announcement-bar feature.
Acceptance   Passes all six gates; premium on mobile/desktop; no placeholder copy; no
             fabricated trust signals; every section links onward (internal-linking rules).
```
