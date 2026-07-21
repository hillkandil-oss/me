# BeepWear — SEO Strategy

Master Prompt Part 10. Technical + on-page + content SEO, engineered in from the start.
Owner milestone **M11**, but applied by the SEO review gate on every milestone. Principle:
**write for people first, search engines second** — never sacrifice UX for SEO.

## 1. Plugin configuration (Rank Math)

Configure: XML sitemaps, breadcrumbs, schema, Open Graph, Twitter Cards, canonicals,
redirections, 404 monitor, image SEO, robots meta. Do **not** enable anything that
duplicates metadata or conflicts with WordPress/WooCommerce. Rank Math owns schema; the
theme's JSON-LD is the fallback (`PLUGINS.md`).

## 2. Site hierarchy & URLs

Logical hierarchy (Home → Shop → categories; Brands → brand; Buying Guides; Journal; About;
Support; Contact), consistent site-wide. Clean URLs — lowercase, hyphenated, descriptive,
no parameters/IDs/symbols:
`/mens-watches/`, `/automatic-watches/`, `/brands/seiko/`, `/buying-guides/`, `/journal/`,
`/shipping-policy/`, `/returns/`, `/contact/`. (Full map: `INFORMATION-ARCHITECTURE.md §2`.)

## 3. Titles & meta

Unique per page, descriptive, no stuffing:
- Home — `BeepWear | Luxury Watches & Premium Timepieces`
- Category — `Automatic Watches | BeepWear`
- Brand — `Seiko Watches | BeepWear`
- Product — `Seiko Presage Automatic Blue Dial | BeepWear`

Unique meta description per page — natural summary, click-encouraging, never duplicated.

## 4. Headings

One H1 per page; logical H2 sections; supporting H3. No skipped levels. Headings organize
for readers first.

## 5. Keyword strategy (by intent)

- **Commercial:** luxury watches, automatic watches, chronograph watches, men's/women's watches.
- **Informational:** how to choose a luxury watch, automatic vs quartz, best watch materials,
  watch care guide.
- **Navigational:** BeepWear, BeepWear warranty, BeepWear returns.

One primary topic per page; cover related concepts naturally; never force keywords.

## 6. Page-type SEO

- **Category** — unique intro + educational content + buying advice + FAQ + internal links +
  related collections. **No thin grid-only pages.**
- **Brand** — original history, overview, signature collections, buying advice, FAQ, related
  products/articles, internal links.
- **Product** — unique title + original description (never reused across products) + specs +
  Product schema + optimized images + links to related products, buying guides, brand, category.

## 7. Image SEO

Descriptive filenames (`seiko-presage-blue-dial-watch.webp`, never `IMG12345.jpg`),
meaningful alt text, responsive sizing, compression, lazy-load, WebP/AVIF.

## 8. Internal linking & breadcrumbs

Natural cross-links: buying guide → products, brand → collections, product → related
articles, category → brand, support → policies, about → contact, journal → buying guides.
No orphan pages. Breadcrumbs on products, categories, brands, articles, support — improving
navigation and `BreadcrumbList` schema.

## 9. Schema (validate with Rich Results Test pre-launch)

Organization · WebSite · Breadcrumb · Product · Offer · Article · FAQ · Review (genuine only).

## 10. Sitemaps, canonicals, indexing, 404s

- **Sitemaps:** pages, products, categories, brands, articles → submit to Search Console.
- **Canonicals** on every page; prevent duplicates from filters/sorting/pagination/params
  (filter URLs `noindex,follow` + canonical to base archive).
- **Index:** home, products, categories, brands, articles, about, contact, appropriate
  policies. **Noindex:** cart, checkout, account, unnecessary search results, admin.
- **404:** branded page, monitor broken links, redirect removed products (no redirect chains).

## 11. Performance & mobile

CWV budget (LCP < 2.5s, INP < 200ms, CLS < 0.1) via the performance plan in `ARCHITECTURE.md`.
Mobile is the primary evaluation surface — responsive, readable, accessible, fast.

## 12. International & local (future-gated)

Multi-currency/language, country shipping, localized content are prepared-for but not built
until needed. **Do not add hreflang until multiple language versions actually exist.** If
online-only, **never fabricate a showroom**; add Local Business schema only with a real address.

## 13. Audits

- **Pre-launch SEO audit:** titles, meta, headings, image optimization, internal links,
  canonicals, schema, sitemap, robots.txt, 404s, broken links, duplicate content, speed,
  mobile usability, accessibility, structured-data validation.
- **Monthly maintenance:** broken links, refresh older articles/guides, monitor rankings +
  Search Console, fix crawl errors, optimize slow pages, review schema + internal linking +
  product accuracy, update sitemap.

## 14. Final SEO principle

Every page must answer yes: real value? original? technically optimized? easy to understand?
helps customers? strengthens authority? improves navigation? supports long-term growth?
If any answer is no, revise before publishing.
