# BeepWear — Page Inventory & Build Checklist

Master Prompt Part 5. The complete set of pages the production site must ship — every one
with a purpose, real content, and internal links. No placeholder or "Coming Soon" pages go
live. This is the build checklist for milestones M4–M15 and the pre-launch structure review.

Status legend: ⬜ planned · 🟡 in progress · ✅ built & gate-passed.
Content source: **Woo** (dynamic WooCommerce) · **Elementor** (page build) · **Content**
(original copy in `content/`) · **Theme** (child-theme template/partial).

---

## A. Global chrome — owner M5

| Element | Contents | Source | Status |
|---------|----------|--------|--------|
| Announcement bar | Rotating, admin-configurable messages (free worldwide shipping on eligible orders, secure checkout, authentic watches, support, easy returns, warranty) | Theme + admin setting | ⬜ |
| Header (sticky) | Logo, primary nav, mega menu, search, wishlist, account, cart; solid on scroll | Elementor Theme Builder | ⬜ |
| Footer | Quick links, shop categories, brands, customer service, policies, newsletter, payment methods, social, business info, copyright, cookie settings, accessibility statement, contact | Elementor Theme Builder | ⬜ |
| Primary nav | Home · Shop · Brands · Collections · Accessories · New Arrivals · Best Sellers · Limited Editions · Journal · About · Support · Contact | — | ⬜ |

The announcement bar is a theme feature with a settings panel (Customizer/options page) so
staff edit messages without code.

## B. Homepage — owner M4 (sections in order, per Part 5)

1. Announcement bar · 2. Header · **3. Hero** (editorial image, headline, supporting copy,
*Shop Now* + *Explore Collections*, minimal overlay, trust indicators) · **4. Featured
Collections** (Men's, Women's, Automatic, Chronograph, Dress, Sports, Limited Edition,
Luxury Gifts) · **5. Featured Brands** (grid/carousel — only brands actually sold) ·
**6. Best Sellers** (Woo) · **7. New Arrivals** (Woo, auto) · **8. Staff Picks** (curated) ·
**9. Why Choose BeepWear** (authentic, secure payments, worldwide shipping, easy returns,
expert support, premium experience) · **10. Editorial Banner** (Higgsfield lifestyle) ·
**11. Testimonials** (genuine reviews only) · **12. Latest Articles** (Journal, auto) ·
**13. Newsletter** · 14. Instagram gallery (if integrated) · 15. Footer.

## C. Commerce — owners M6 (browse) / M7 (PDP) / M8 (cart-checkout) / M10 (account)

| Page / template | Key sections | Source | Owner |
|-----------------|--------------|--------|-------|
| Shop | Hero, filters, sort, grid/list toggle, pagination, breadcrumbs, category description, SEO intro, recently viewed | Woo + Theme | M6 |
| Category (template) | Hero, description, product grid, filters, buying-guide link, related collections, FAQ, SEO content, internal links | Woo + Elementor | M6 |
| Brand directory (`/brands/`) | Brand index (only brands sold), search/filter | Woo `brand` + Elementor | M6 |
| Brand (template) | History, overview, brand image, collections, featured models, philosophy, FAQ, related articles, products, internal links | Content + Woo | M6 |
| Collection (template) | Luxury hero, description, product grid, buying guide, filters, related collections, FAQ, SEO content, internal links | Content + Woo | M6 |
| Product (PDP) | Gallery + zoom (360°/video optional), brand, model, SKU, price, availability, variants, quantity, add-to-cart, wishlist, compare, highlights, description, specifications, what's included, warranty, shipping/returns, est. delivery, payment methods, legitimate trust badges only, related, recently viewed, genuine reviews, schema, breadcrumbs, social share, FAQ | Woo + Theme | M7 |
| Cart | Images, qty, price, coupons, shipping estimate, subtotal, taxes, total, continue shopping, checkout, trust info | Woo | M8 |
| Checkout | Guest/login, billing, shipping, shipping method, payment, order summary, coupon, terms, privacy notice, secure-checkout messaging | Woo | M8 |
| Order confirmation | Order number, products, billing, shipping, est. delivery, support info, continue shopping | Woo | M8 |
| Account | Login, register, dashboard, orders, downloads (if any), addresses, wishlist, details, password, logout | Woo | M10 |
| Wishlist | Saved products, move to cart, remove, share (optional) | Plugin | M10 |
| Search results | Results, suggested products/categories/articles, popular searches | Woo + Theme | M6 |

### Product specification fields (PDP) → see `DATA-MODEL.md §8`

## D. Content pages — owner: Content workstream (with M9)

| Page | Contents | Status |
|------|----------|--------|
| About | About BeepWear, story, mission, vision, values, quality commitment, authenticity promise, customer experience, luxury philosophy | ⬜ |
| Support hub | Help center, order tracking, returns, shipping, warranty, payment methods, FAQs, watch care, buying guides, contact | ⬜ |
| Contact | Form, email, phone, address (if available), hours, map (if applicable), customer-service info, response-time expectations, social | ⬜ |
| Journal (blog) | Article listing; categories: Buying Guides, Watch Education, Luxury Lifestyle, Brand Stories, Maintenance, Gift Guides, Industry News, Fashion, Collector Insights | ⬜ |
| Article (template) | Hero, author, date, reading time, table of contents, content, images, related products, related articles, newsletter, comments (optional) | ⬜ |

## E. Legal, policy & trust pages — owner M9 (content-complete, no placeholders)

**Legal:** Privacy Policy · Cookie Policy · Terms & Conditions · Accessibility Statement ·
Disclaimer · Intellectual Property Notice.
**Customer policies:** Shipping · Return · Refund · Warranty · Payment · Pre-Order (if
applicable) · Cancellation · Authenticity Guarantee · Price Match (only if actually offered).
**Trust pages:** Why Buy From BeepWear · Authenticity · Quality Assurance · Watch Inspection
Process · Packaging · Shipping Protection · Customer Satisfaction · Secure Payments.

> Claims must be true and backed by real operations. No fabricated guarantees, awards, or
> badges. Policies must be easy to find (footer + support hub) — a Merchant Center essential.

## F. Buying guides — owner: Content workstream

How to Choose a Luxury Watch · Automatic vs Quartz · Watch Size Guide · Water Resistance
Guide · Watch Materials · Luxury Watch Terminology · Watch Movements Explained · How to Care
for Your Watch · How to Store Watches · Investment Guide (educational — no financial promises)
· Buying Your First Luxury Watch · Choosing the Perfect Gift Watch.

## G. FAQ — owner M9 / Content

Categorized: Products · Orders · Payments · Shipping · Returns · Warranty · Accounts · Care ·
Support. FAQ content also feeds `FAQPage` schema where appropriate.

## H. Error & empty states — owner M5 (detail in `INFORMATION-ARCHITECTURE.md §5`)

404 · 500 · Maintenance · Search-no-results · Empty cart · Empty wishlist · Order failure.
All on-brand, all route the user back into browsing. "Coming Soon" is dev-only, removed
before launch.

## I. Internal linking rules

Product → Brand · Product → Collection · Product → Buying Guide · Buying Guide → Products ·
Journal → Collections · About → Contact · Support → Policies. Every public page reachable
within three clicks of Home; no orphaned pages.

## J. Pre-launch site-structure review (M13/M15 gate)

- [ ] Every menu item resolves to a complete page.
- [ ] Every page has original, useful content — no placeholders.
- [ ] All legal + customer-policy pages complete and linked in footer.
- [ ] Support info and policies easy to find.
- [ ] PDPs show accurate specs, price, availability.
- [ ] Navigation consistent across the site.
- [ ] Internal links resolve; no broken or orphaned pages.
- [ ] XML sitemap includes all public pages; robots.txt correct.
- [ ] Site presents transparently as a legitimate retailer (contact, policies, business info).
