# BeepWear — Changelog

Significant changes, newest first. Per `docs/OPERATIONS.md §5`, notable changes record
objective, impact, and status. Development branch: `claude/hello-lz33xo`.

## Unreleased (pre-launch build)

- **GEO & AI visibility upgrade:** restructured all six journal guides for AI citability
  (Quick Answer blocks, data tables, question-form headings, per-guide FAQs, meta
  descriptions, internal links). Added theme JSON-LD fallback for journal posts —
  `BlogPosting` + `FAQPage` + `HowTo` (`inc/schema.php`, `inc/journal-schema-data.php`),
  using real post dates. Fixed social cards: raster `og:image`/`twitter:image`
  (1200×630) + 512×512 Organization logo, replacing non-rendering SVGs. See
  `docs/GEO-CITABILITY.md`. Impact: FAQ/Article/HowTo rich-result eligibility + AI-answer
  citability; status: in repo, pending live apply.
- **Ops & governance (Parts 12–14):** deploy runbook, operations/QA/maintenance model,
  multi-agent workflow, master execution blueprint with acceptance criteria + launch gate.
- **Component library (Part 11):** shadow tokens, `.bw-badge` / `.bw-alert`; theme v0.4.0.
- **Content/SEO/Merchant Center (Parts 8–10):** content strategy, About page copy,
  Merchant Center audit spec, SEO strategy.
- **M5 Navigation:** header, mega menu, mobile drawer (`preview/nav.html`).
- **M4 Homepage:** 15-section homepage (`preview/homepage.html`), copy, announcement-bar
  feature, real self-hosted variable fonts (Cormorant Garamond + Manrope).
- **M3 Architecture:** stack decisions, data model, plugin stack, information architecture,
  product-experience spec.
- **M2 Brand:** design system realigned to Black/White/Gold + Manrope (Part 4).
- **M1 Planning:** governance operating model, 15-milestone plan, six review gates.
