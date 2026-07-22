# BeepWear — SEO Implementation Checklist (Milestone 11)

The executable version of `SEO-STRATEGY.md`: the exact settings to apply on the live
WordPress install. Owner **M11**; runs on Hostinger. Tick each item; record verdicts in
`REVIEW-LOG.md`.

## 1. Permalinks & base slugs

- [ ] Settings → Permalinks → **Post name** (`/%postname%/`).
- [ ] WooCommerce product base `/product/`; category base handled so dedicated landing URLs
      resolve (`/mens-watches/`, `/automatic-watches/`, …) per `INFORMATION-ARCHITECTURE.md §2`.
- [ ] Lowercase, hyphenated slugs; no IDs/params on canonical pages.

## 2. Rank Math configuration

- [ ] Modules on: Sitemap, Breadcrumbs, Schema, Open Graph/Twitter, Redirections, 404 Monitor,
      Image SEO (auto-alt as fallback), Robots meta.
- [ ] **Schema ownership:** Rank Math emits Organization, Breadcrumb, Product, FAQ. Set
      `BEEPWEAR_EMIT_SCHEMA` = `false` so the theme's JSON-LD (`inc/schema.php`) stays a
      dormant fallback (no duplicate schema). Confirm with Rich Results Test after.
- [ ] Open Graph default image + per-page overrides; Twitter card = summary_large_image.

## 3. Title & meta templates (per page type)

Set these in Rank Math's Titles & Meta (variables in braces resolve dynamically). Keep
titles ≤ ~60 chars, descriptions ≤ ~155, each unique.

| Type | Title template | Meta description |
|------|----------------|------------------|
| Home | `BeepWear | Luxury Watches & Premium Timepieces` | From `content/homepage.md` |
| Product | `{Brand} {Product Title} | BeepWear` | Product short description (unique per product) |
| Category | `{Category} Watches | BeepWear` | Unique category intro (term description) |
| Brand | `{Brand} Watches | BeepWear` | Unique brand overview |
| Collection | `{Collection} Collection | BeepWear` | Collection overview |
| Journal post | `{Title} | BeepWear Journal` | Article excerpt |
| Page | `{Title} | BeepWear` | Page summary |

- [ ] No promo text in titles (no SALE!!!, 100% ORIGINAL) — feed/SEO rule.
- [ ] One H1 per page (template enforces); H2/H3 hierarchy, no skips.

## 4. Robots & indexing

- [ ] `robots.txt` per `config/robots.txt` (Rank Math serves it; paste the rules there).
- [ ] **Index:** home, products, categories, brands, collections, journal, about, contact,
      appropriate policies.
- [ ] **Noindex:** cart, checkout, my-account, internal search results, thank-you/order-received.
- [ ] **Filter/facet URLs:** `noindex,follow` + canonical to the base archive (duplicate-content guard).
- [ ] Canonical self-reference on all indexable pages; paginated archives canonical per page.

## 5. Sitemaps

- [ ] Rank Math XML sitemaps enabled for: pages, products, product categories, brands,
      collections, journal posts. Exclude noindex types.
- [ ] Submit `sitemap_index.xml` in Google Search Console after launch.

## 6. Structured data — validate before launch

- [ ] Organization + WebSite (home), Product + Offer (PDP), BreadcrumbList (all), FAQPage
      (PDP/category/FAQ), Article (journal), Review **only** when genuine.
- [ ] Run each template through Google's **Rich Results Test**; resolve all errors/warnings.
- [ ] Product schema: `brand`, `sku`, `gtin`/`mpn` **only when real**, `offers`
      (price/priceCurrency/availability/url) matching the page and feed.

## 7. Image SEO

- [ ] Descriptive filenames (`{brand}-{model}-{feature}.webp`), never `IMG1234.jpg`.
- [ ] Meaningful alt text on meaningful images; empty alt on decorative.
- [ ] WebP/AVIF via LiteSpeed; responsive `srcset`; lazy-load; hero sized to avoid CLS.

## 8. Internal linking

- [ ] Product → brand, category, relevant buying guide. Category → buying guide + related
      collections. Journal → collections/products. About → contact. Support → policies.
- [ ] No orphan pages; every public page ≤ 3 clicks from home. Breadcrumbs everywhere.

## 9. Google Search Console & analytics (post-launch)

- [ ] Verify ownership (Site Kit or DNS/HTML).
- [ ] Submit sitemap; monitor Coverage, Enhancements (Products, Breadcrumbs, FAQ), Core Web Vitals.
- [ ] GA4 via Site Kit; ecommerce events (view_item, add_to_cart, begin_checkout, purchase),
      search, newsletter, contact — consent-gated (Complianz). GTM only if needed, no dupes.

## 10. Pre-launch SEO audit (M13/M15)

Titles · meta · headings · image opt · internal links · canonicals · schema · sitemap ·
robots.txt · 404s · broken links · duplicate content · page speed · mobile usability ·
accessibility · structured-data validation — each PASS/WARNING/BLOCKER in `REVIEW-LOG.md`.
