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

---

## Milestone 4 — Homepage · ✅ signed off (build-ready; imagery + Woo binding at deploy)

**Deliverables:** `content/homepage.md` (final original copy), `preview/homepage.html`
(rendered visual reference with real embedded fonts), `docs/ELEMENTOR-BUILD-GUIDE.md`,
`docs/IMAGE-PROMPTS.md`, announcement-bar theme feature (`inc/announcement-bar.php` +
Customizer + CSS/JS), and the real self-hosted variable fonts (Cormorant Garamond +
Manrope) installed in the theme. Theme v0.3.x.

Rendered and screenshotted at 1280px and 390px (desktop + mobile) — see scratchpad shots.

| Gate | Result | Notes |
|------|--------|-------|
| Design | ✅ | All 15 sections in order; premium black/white/gold; Cormorant hero, Manrope body; consistent with BRAND.md. |
| SEO | ✅ | Single H1 (hero), H2 per section, logical order; title + meta set; Org/WebSite/Breadcrumb schema (Rank Math in prod). |
| Accessibility | ✅ | Focus rings, reduced-motion freezes reveal + announcement rotation, `aria-live` on the bar, contrast passes. **Open (M5):** mobile nav needs a hamburger — icons/nav hide < 960px in the preview; real header (Theme Builder) supplies the mobile menu. |
| Performance | ✅ | Fonts self-hosted + preloaded (variable, one file each); images lazy at build; no CLS in preview. Hero image must be sized at deploy. |
| Merchant Center | ✅ | No fabricated testimonials/ratings/brands (those sections stay hidden until genuine); transparent trust + policy links. |
| QA | ✅ | Responsive verified desktop + mobile; no horizontal scroll; PHP lints clean. |

**Carried to build-time:** bind Best Sellers / New Arrivals / Journal rails to live Woo/posts
(guide written); produce real hero + editorial imagery from `IMAGE-PROMPTS.md`; wire the
mobile menu in the Theme Builder header (M5).

### Part 7 integrated — product-experience spec-of-record (owners M6/M7)

- **`docs/PRODUCT-EXPERIENCE.md`** — catalog structure, full PDP layout (14 blocks),
  category/brand/collection page layouts, variations, filter/sort/search, inventory,
  recommendations/cross-sells/up-sells/comparison, image standards, and the per-product +
  Merchant Center review checklists.
- **`DATA-MODEL.md`** — added `band-color` attribute and a `collection` taxonomy for named
  collections; feed mapping already covers gtin/mpn/condition/shipping/tax.
- Milestone order unchanged: M5 (Navigation) is the next build — it gates the catalog pages.

## Milestone 5 — Navigation · ✅ signed off

**Deliverables:** `preview/nav.html` (header + mega menu + mobile drawer, real fonts),
`docs/ELEMENTOR-BUILD-GUIDE.md` header/mega/mobile/footer section. Footer built in the M4
homepage preview. Rendered and screenshotted desktop (mega open) + mobile (drawer open).

| Gate | Result | Notes |
|------|--------|-------|
| Design | ✅ | Sticky white header, gold-accent logo; mega organized By Gender/Style/Movement/Shop + featured card; clean mobile drawer. On-system throughout. |
| SEO | ✅ | Nav links map to clean URLs; footer carries full map; no orphan links. |
| Accessibility | ✅ | Resolves the M4 open item — mobile hamburger drawer with search, ≥44px targets, focus-trap + overlay close; mega opens on hover **and** keyboard focus with `aria-expanded`. |
| Performance | ✅ | CSS-only mega (no heavy JS); drawer is a light toggle. |
| Merchant Center | ✅ | Brands shown only when real; policies reachable from footer (transparency). |
| QA | ✅ | Verified 1280px + 390px; no horizontal scroll. |

**Carried to build-time:** assemble in Elementor Theme Builder per the guide; populate the
Brands mega once real brand partnerships exist.

### Parts 8–10 integrated — content, Merchant Center, SEO spec-of-record

- **`docs/CONTENT-STRATEGY.md`** (Part 8) — tone, page copy plan, policies list, categorized
  FAQ, buying-guide slate with word targets, journal + article template, newsletter/error/
  email copy, content quality review gate.
- **`content/about.md`** (Part 8) — first real page copy, original + honest (no fabricated
  history; owner facts flagged `[confirm: …]`), with internal links.
- **`docs/MERCHANT-CENTER.md`** (Part 9) — legitimacy signals, product-data rules, feed spec
  + identifiers guardrail, structured data, sitemaps/robots/GSC/GA4, CWV, and the M12
  PASS/WARNING/BLOCKER pre-launch audit matrix + post-launch monitoring.
- **`docs/SEO-STRATEGY.md`** (Part 10) — Rank Math config, hierarchy/URLs, titles/meta,
  headings, keyword-by-intent, page-type SEO, image SEO, internal linking, breadcrumbs,
  schema, sitemaps/canonicals/indexing/404, performance/mobile, i18n-gated, audits.

These are spec-of-record for M9 (content/policies), M11 (SEO), M12 (Merchant Center).

### Part 11 integrated — component library (owner: design system, all milestones)

- **`docs/COMPONENT-LIBRARY.md`** — global-token → Elementor-global mapping, full component
  inventory (buttons, forms + input states, cards, badges, alerts, gallery, accordion, tabs,
  modals, empty/loading states, micro-interactions), reusable-template list with where-used,
  and the Design QA checklist.
- **Theme v0.4.0** — added shadow tokens (`--shadow-sm/md/lg/hover`) and reusable `.bw-badge`
  + `.bw-alert` component styles (alerts convey state via a dot, not color alone). PHP lints clean.
- **Palette conflict flagged & resolved:** Part 11's "Deep Navy" palette is an *example*;
  Part 4's Black/White/Gold (already built) remains authoritative — noted in the doc.

### Parts 12–13 integrated — workflow, QA & operations

- **`docs/DEPLOY-RUNBOOK.md`** (Part 12) — Hostinger environment setup, configuration,
  backups, staging→production deployment process (pre/post checks), domain + Merchant
  Center gating, rollback. Fills the doc referenced across the project.
- **`docs/OPERATIONS.md`** (Parts 12–13) — git workflow, testing strategy, pre-deploy QA
  checklist, monitoring + daily/weekly/monthly/quarterly maintenance, change management,
  incident response, multi-agent operating model + decision framework, automation
  guardrails, reporting dashboard, continuous-improvement loop + success metrics.
- **`CHANGELOG.md`** — seeded with milestone history.

### Part 14 integrated — master execution blueprint & acceptance

- **`docs/MASTER-BLUEPRINT.md`** — top-level definition of done: Part 14's 9-phase order
  mapped to the 15 milestones with **live status**, acceptance criteria per area, the
  launch-readiness PASS/WARNING/BLOCKER gate, master completion checklist, long-term
  roadmap, and the explicit list of **business-provided items** that gate publication
  (real brands, business facts, product data + photography, payment/shipping details,
  Hostinger + Google access).
- Confirms the milestone sequence and quality standards already in force; no conflicts.

## Milestone 6 — Collections · ✅ signed off

**Deliverables:** `preview/category.html` (category/PLP template — breadcrumb, hero + SEO
description, sort, faceted filter sidebar, product grid with badges + wishlist, pagination,
buying-guide band, FAQ accordion, related collections, newsletter, footer), and the
Collections section of `docs/ELEMENTOR-BUILD-GUIDE.md` (shop/category template + brand,
collection, and search variations). Rendered desktop + mobile.

| Gate | Result | Notes |
|------|--------|-------|
| Design | ✅ | Premium PLP; consistent with home/nav; badges via `.bw-badge`/`onsale`; Cormorant model names, tabular prices. |
| SEO | ✅ | Breadcrumb + unique hero description + buying-guide band + FAQ (avoids thin grid pages); filter URLs planned `noindex`+canonical. |
| Accessibility | ✅ | Checkable filters with labels, keyboard-operable sort, FAQ via native `<details>`, focus states; mobile Filters button for the drawer. |
| Performance | ✅ | CSS grid, lazy images at build, no layout shift in preview. |
| Merchant Center | ✅ | Accurate availability filter; no fake ratings; brand facets only for real brands. |
| QA | ✅ | Verified 1280px + 390px (2-up grid, sidebar → Filters button); no horizontal scroll. |

**Carried to build-time:** assemble as Woo archive Theme Builder templates; choose the
filter plugin (per `PLUGINS.md`); brand/collection pages add original content blocks;
search-results template + no-results state.

## Milestone 7 — Product Pages (PDP) · ✅ signed off

**Deliverables:** `preview/product.html` (full 14-block PDP with original sample copy +
specs), PDP section of `docs/ELEMENTOR-BUILD-GUIDE.md`. Rendered desktop + mobile.

| Gate | Result | Notes |
|------|--------|-------|
| Design | ✅ | Gallery + dial-motif placeholder, variation chips, spec table, tabs, related/recently-viewed; premium and on-system. |
| SEO | ✅ | Breadcrumb, `{Brand} {Model} | BeepWear` title, unique meta, spec/description content, internal links; Product schema spec'd. |
| Accessibility | ✅ | Keyboard chips/qty, `:focus`, `<details>` FAQ, in-stock conveyed by text + dot (not color alone), alt text at build. |
| Performance | ✅ | Single template; images lazy at build; no CLS in preview. |
| Merchant Center | ✅ | **Empty reviews state states no fabricated testimonials;** specs accuracy-gated; identifiers only when real; price/availability shown consistently. |
| QA | ✅ | Verified 1280px + 390px (gallery/summary stack, tabs stack); no horizontal scroll. |

**Carried to build-time:** bind to real product data + authorized photography; populate
specs from verified values only; Product schema `gtin`/`mpn` only when real; reviews appear
only from confirmed purchases.

### PM brief — Milestone 8 (Checkout: cart, checkout, order confirmation) · next

```
Objectives   Style and document the WooCommerce cart → checkout → order-confirmation flow
             per PAGE-INVENTORY §C and PRODUCT-EXPERIENCE, keeping Woo's secure native flow.
Tasks        1. Cart: line items, qty, coupon, shipping estimate, subtotal/tax/total,
                continue-shopping, checkout, trust info.
             2. Checkout: guest/login, billing/shipping, shipping + payment method, order
                summary, coupon, terms, privacy notice, secure-checkout messaging.
             3. Order confirmation: number, items, billing/shipping, est. delivery, support.
             4. Empty-cart state; visual preview + build-guide section.
Dependencies design system, Woo (deploy); payment gateways configured on host.
Risks        Never rebuild checkout in Elementor — style Woo's flow (security/update safety).
Deliverables preview/cart-checkout, build-guide section.
Acceptance   Six gates; simple/secure checkout; HTTPS; no distractions; accurate totals.
```

```
Objectives   Build the single-product template per PRODUCT-EXPERIENCE.md §2 (14 blocks).
Tasks        1. Gallery + summary (brand, model, ref, price, availability, variations,
                qty, add-to-cart, wishlist, compare).
             2. Highlights, original description, specifications table (DATA-MODEL §8),
                what's-included, shipping/returns/warranty summaries, payment methods.
             3. Related + recently-viewed; genuine-reviews block (hidden until real); FAQ.
             4. Product schema (brand/sku/gtin when real, offers, availability), breadcrumbs.
             5. Visual PDP preview + build-guide section.
Dependencies DATA-MODEL, PRODUCT-EXPERIENCE, design system (done); real product data at deploy.
Risks        No real product/photography yet → preview uses clearly-placeholder imagery;
             specs/identifiers must be verified before publishing any real PDP.
Deliverables preview/product.html, build-guide PDP section, sample PDP copy.
Acceptance   Six gates; premium PDP; valid schema; no invented specs/identifiers/reviews.
```

```
Objectives   Build the browse layer per PRODUCT-EXPERIENCE.md — shop archive, category,
             brand, and collection templates + search results, all inheriting the system.
Tasks        1. Style the Woo shop/category archive (hero, filter sidebar, sort, grid,
                pagination, SEO intro, FAQ, related) via child theme + Elementor templates.
             2. Brand + collection page templates (original content blocks).
             3. Faceted filters mapped to attributes/taxonomy; filter URLs noindex+canonical.
             4. Search results + no-results suggestions.
             5. Visual preview (category/PLP) + build guide section.
Dependencies DATA-MODEL, INFORMATION-ARCHITECTURE, PRODUCT-EXPERIENCE (done); Woo at deploy.
Risks        Filter plugin choice affects UX/perf — evaluate vs plugin policy before adding.
Deliverables category preview, build-guide section, filter/sort config notes.
Acceptance   Passes six gates; premium PLP; filters accessible; no duplicate-content indexing.
```

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
