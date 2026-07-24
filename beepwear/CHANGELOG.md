# BeepWear — Changelog

Significant changes, newest first. Per `docs/OPERATIONS.md §5`, notable changes record
objective, impact, and status. Development branch: `claude/hello-lz33xo`.

## Unreleased (pre-launch build)

- **SEO/GEO audit fixes (theme v0.9.5):** post-launch audit of the live site.
  - Product schema: force `itemCondition: UsedCondition` on the Rank Math Product
    entity (unconditional override — some Rank Math versions default to
    NewCondition) plus a `rank_math/json_ld` graph-level safety net so the used
    condition lands regardless of graph shape; map SKU → `mpn` when no mpn/gtin.
  - Homepage share image: emit a real 1200×630 raster `og:image`/`twitter:image`
    (`assets/images/og-default.png`) instead of the non-rendering SVG; add
    `og:image:width/height`.
  - Organization schema: add filterable `sameAs` (`beepwear/organization_sameas`),
    empty by default — populate with real verified profile URLs only.
  - `config/robots.txt`: explicit AI-crawler directives (GPTBot, OAI-SearchBot,
    ClaudeBot, PerplexityBot, Google-Extended, CCBot, …) welcoming citation while
    keeping transactional paths out.
  - `config/llms.txt`: new GEO map of buying guides, shop, and policies for AI
    answer engines.
  - FAQ: new `inc/faq-schema.php` emits `FAQPage` JSON-LD on the support FAQ page
    (rich results + AI passage citation), seeded from `content/faq.md`. Answers
    still carrying a `[confirm: …]` placeholder are auto-skipped so unverified
    facts never enter structured data (15 of 18 Q&A currently eligible);
    filterable via `beepwear/faq_items` and `beepwear/faq_page_slugs`.

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
