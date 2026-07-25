# BeepWear — GEO & AI Visibility Upgrade

Optimizing the site to be **cited and surfaced by AI answer engines** (ChatGPT, Perplexity,
Google AI Overviews, Gemini) alongside classic search. Companion to `SEO-STRATEGY.md` and
`SEO-IMPLEMENTATION.md`; this file covers the **generative-engine (GEO/AEO)** axis.

## Audit baseline (live beepwear.com)

Two independent scores from a live crawl of the homepage, a product page, the FAQ, and all six
journal guides:

| Axis | Score | Notes |
|------|-------|-------|
| Search SEO | ~78 / B+ | Strong technical base: HTTPS, HTTP/3, LiteSpeed cache, valid sitemap, canonical, clean titles/meta, `Product`+`Offer`+`Breadcrumb` schema on products. |
| AI Visibility (GEO) | ~61 / C+ | Good entity + product data, but the most citation-friendly content (guides, FAQ) was not machine-readable. |

### Gaps found
- **FAQ page** (`/faq/`) had **no `FAQPage` schema** — forfeited FAQ rich results and AI Q&A citations.
- **Journal guides** had **no `Article`/`FAQPage`/`HowTo` schema**, no author/E-E-A-T signals, and no meta descriptions.
- **No tables** across 12,000+ words of guides — four topics (water resistance, sizing, materials, movements) are table-shaped and tables are preferentially extracted by AI engines.
- **Headings were editorial, not interrogative** — they didn't match how users/models phrase queries.
- **`og:image` / `twitter:image` were an SVG** (`beepwear-mark.svg`) — SVGs do not render as social/AI share cards; `twitter:image` was missing entirely.
- Default WordPress **`hello-world` post** still live and indexable (thin-content trust signal).

## Changes in this repo

### Content — `content/guides/*.md` (all six guides)
Each guide now has, in the BeepWear voice:
- A **metadata block**: meta description, author (BeepWear Editorial Team), category, primary question.
- A **Quick Answer** block (40–60 words) directly after the intro — the passage AI engines quote first.
- **Question-form H2 headings** that match real search/AI queries.
- **Data tables** where the topic is table-shaped:
  - Water resistance → rating × safe-use × avoid
  - Automatic vs Quartz → side-by-side comparison
  - Watch Size → wrist-circumference × case-diameter chart
  - Materials → case-material and crystal comparison tables
  - Buying Guide → movement comparison + a 7-step summary
  - Care → maintenance schedule table
- A **Frequently Asked Questions** section (4 Q&As each) at the end.
- Additional **contextual internal links** between guides and to categories.

### Schema — `theme/beepwear/inc/schema.php` + `inc/journal-schema-data.php`
- New `beepwear_journal_schema()` emits, for single journal posts, a `@graph` of:
  - **`BlogPosting`** — headline, description, image, `datePublished`/`dateModified` (**from the live post — nothing fabricated**), author, publisher with logo, `mainEntityOfPage`.
  - **`FAQPage`** — from the per-slug FAQ map in `inc/journal-schema-data.php` (mirrors the guide bodies).
  - **`HowTo`** — for the watch-care guide (6 steps).
- Guarded by `BEEPWEAR_EMIT_SCHEMA`, consistent with the existing fallback model.
- **`og:image` fixed** to a raster `beepwear-share.png` (1200×630) + `og:image:width/height`; added the missing **`twitter:image`**; Organization `logo` now a 512×512 raster `ImageObject`.

### Assets — `theme/beepwear/assets/images/`
- `beepwear-share.png` (1200×630) — social/AI share card.
- `beepwear-logo.png` (512×512) — raster mark for Organization schema (per `BRAND.md §Logo`).

## Live status — applied 2026-07-25 (via WordPress REST API)

Applied directly to beepwear.com (REST cannot deploy theme files, so guide schema was
shipped as **inline JSON-LD inside each post** rather than via the theme fallback):

- ✅ **All 6 journal post bodies** updated from `content/guides/*.md` — Quick Answer callouts, data tables, question-form headings, FAQ sections.
- ✅ **Inline JSON-LD** on every guide: `BlogPosting` + `FAQPage` (4 Q&As each) + `HowTo` (care guide). Validated as parseable; real post `datePublished`, current `dateModified`.
- ✅ **Meta descriptions** set via each post's **excerpt** (Rank Math uses it as the description) — confirmed rendering in `<meta name="description">`.
- ✅ **Share/logo rasters uploaded** to the media library (`/wp-content/uploads/2026/07/beepwear-share.png`, `…/beepwear-logo.png`); schema `image`/`publisher.logo` point to them (resolve 200).
- ✅ **`hello-world` default post deleted** (force) — now 404, dropped from the post set.

Backups of each post's pre-edit content are in the working session (`backup-<id>.json`).

### Still requires a theme redeploy (SFTP / hosting — not possible over REST)

1. **Deploy `theme/beepwear/`** so `inc/schema.php` + `inc/journal-schema-data.php` and the two PNGs under `assets/images/` ship. When you do, **keep `BEEPWEAR_EMIT_SCHEMA = false`** in production so the theme's journal schema does not duplicate the inline JSON-LD already in the post bodies (per `SEO-IMPLEMENTATION.md §2`).
2. **Homepage social card:** the raster `og:image`/`twitter:image` + Organization logo fixes live in `inc/schema.php` and only take effect after deploy. Until then, either deploy, or set Rank Math's **default OG image** to the uploaded `beepwear-share.png` (Rank Math → Titles & Meta → Global).
3. *(Optional)* Per-guide `og:image`: set the uploaded share card as each guide's featured image, or a Rank Math per-post OG image.

### Verify
Google Rich Results Test + Schema.org validator on the homepage, a product, and each guide; Facebook Sharing Debugger + X Card validator for social cards.

## Optional next (higher GEO ceiling)
- Add a real named horologist byline + author bio page to strengthen E-E-A-T beyond the team attribution.
- Add buyer reviews with `Review`/`AggregateRating` on products.
- Publish an `llms.txt` mapping key pages for AI crawlers.
