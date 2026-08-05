# Google Merchant Center — Readiness Report

_kaisercontainers.de · 2026-08-04 · Approval can never be guaranteed; this reduces avoidable risk._

## Overall readiness status
**NOT READY — major issues remain.** The store has real products, correct currency/country,
and a full set of German pages and policies staged. It is **blocked from submission** by missing
verified legal/contact facts, unpublished (draft) pages, and theme-layer application steps.
Path: once the owner facts are filled and the go-live checklist is run, status moves to
**"Ready after minor corrections."**

## Critical blockers (must clear before submission)
1. **Impressum incomplete** — responsible person, legal form, USt-IdNr., (Handelsregister)
   missing. A valid Impressum is legally required for a German store and checked by reviewers.
2. **Store phone unverified** — brief's number is a Hamburg code; store is in Duisburg. NAP
   (name/address/phone) must be identical across site, schema, and Google Business Profile.
3. **Exact street address missing** — only district known; map pin and schema need the real street.
4. **Pages are drafts** — Startseite, Kontakt, policies not yet published; front page not set.
5. **Placeholders present** — 〔BITTE BESTÄTIGEN〕 markers must all be removed before anything public.
6. **Price basis undefined** — net vs. gross (inkl./zzgl. USt.) must be stated (Merchant Center
   requires the displayed price to include VAT for consumers in DE).

## High-priority (before submission)
- Publish the German legal pages after owner review; repoint WooCommerce privacy → Datenschutz,
  terms → AGB; trash old English stubs (Privacy Policy id 3, Refund/Returns id 13).
- Apply `brand.css` + fonts; add header top bar + footer; assign Main Menu to `main_menu`.
- Install an **SEO plugin** (Rank Math / Yoast) — none present → needed for meta titles,
  descriptions, XML sitemap, breadcrumbs, and **automatic Product/Offer schema** (required for feed↔page price/availability match).
- Inject LocalBusiness schema (`schema-jsonld.php`) with verified data; validate.
- **Cookie consent**: no consent tool detected. If any analytics/marketing runs, a TTDSG/DSGVO
  consent banner (e.g. Complianz / Borlabs) with prior opt-in is required.
- Confirm **shipping cost** handling for heavy freight (flat / by distance / on request) and make
  it consistent across product pages, cart, checkout, Versand policy, and feed.

## Medium-priority (trust / UX / SEO / a11y)
- Real store/yard + product photography (replace homepage photo slot; no fabricated images).
- Product dimensions + weight on all 20 products (see dimensions reference).
- Test checkout end-to-end in a sandbox; verify order + confirmation emails (German).
- Accessibility pass (focus states, contrast, alt text, keyboard nav) — brand.css sets AA
  focus rings and reduced-motion; verify on the live theme.
- Performance: LiteSpeed present; verify image sizes/lazy-load and Core Web Vitals.

## Product-feed risks
- **All 20 products lack dimensions + weight** — confirm and apply.
- **No GTIN** — correct for containers; feed uses `identifier_exists=no` + brand + MPN(SKU). Do not invent GTINs.
- **google_product_category** set broadly to "Business & Industrial"; refine if a better node fits.
- **Price↔schema sync** — install SEO/Woo Product schema so the feed price/availability matches
  the product page exactly (a common disapproval cause).
- Availability currently all `in_stock`; keep accurate as stock changes.

## Required information from owner
See `REQUIRED-FROM-OWNER.md` (single source of truth). Blocking items: phone, street, Impressum
identity + USt-IdNr. (+ HRB), price net/gross, real photos, shipping cost basis, dimensions/weight.

## Final recommendation
**Hold for verification, then correct before submitting.** Do not submit to Merchant Center until
(a) the blocking owner facts are provided, (b) the go-live checklist is executed, (c) checkout and
the contact form are tested, and (d) LocalBusiness + Product schema validate with data matching the
visible pages. Submit only on the live custom domain, never a preview URL, and only with the
owner's explicit authorization.


---

## Update — live verification pass (2026-08-05)

**Progress since the first report**
- All 16 pages **published and returning 200** (home, shop, cart, checkout, account, contact,
  about, FAQ and all eight policy/legal pages).
- Homepage is the front page; navigation live; brand design, logo, footer with full NAP and
  policy links applied site-wide.
- **Product pages now carry the §17 block**: availability-may-differ notice, processing and
  delivery times, pickup, payment method, returns, and policy links.
- Condition (`Neu`/`Gebraucht`) visible on all 20 products; feed CSV carries `condition`.
- Product schema present with `availability` + `priceCurrency`; LocalBusiness + Organization
  schema injected site-wide with verified data only.
- Sitemap live at `/sitemap.xml`.
- Fake theme demo contact bar (Cyprus `+357` number, dead `mailto:#`) removed from the
  rendered page — a direct misrepresentation risk retired.

**Status: still NOT READY for submission.** Remaining blockers are unchanged and all require
owner-verified facts or one-time admin actions:
1. Impressum incomplete (responsible person, street, USt-IdNr.) — legally required in Germany.
2. `wird ergänzt` placeholders for phone and street are publicly visible.
3. Contact form is CF7's English default and delivers to the **site-admin address**, not
   `info@kaisercontainers.de` — a broken support path is a Merchant Center risk.
4. Price basis (net vs. gross) still undeclared.
5. Fake `+357` phone still present in the raw theme template source.
6. Cookie consent installed but not activated.

**Recommendation unchanged:** hold for verification, correct, then submit only with explicit
authorization. Approval is never guaranteed.


---

## Update 2 — Merchant Center readiness pass (2026-08-05)

### Blockers cleared in this pass
| Was | Now |
|---|---|
| 🔴 Contact form delivered to the site-admin gmail, not the business inbox | ✅ WordPress site admin email changed to `info@kaisercontainers.de`; CF7's `[_site_admin_email]` recipient now resolves there. Enquiries reach the business without replacing the form plugin. |
| 🔴 Price basis undeclared (hidden-cost risk) | ✅ Prices display **"zzgl. Versandkosten"** linked to the shipping policy (German PAngV). Tax calculation is off, so displayed prices are final prices — consistent with holding no VAT ID. No false "inkl. MwSt." claim was added. |
| 🔴 Impressum incomplete | ✅ Responsible person, address, phone published; VAT and Handelsregister sections removed as not applicable and stated explicitly. |
| 🔴 Placeholder text public | ✅ Zero placeholders remain on any public page. |
| 🟡 All 20 products missing dimensions | ✅ ISO nominal external dimensions applied to 20/20, plus a readable `Abmessungen` attribute. These are the definitional specs of each named size, not estimates. |
| 🟠 No cookie consent | ✅ Complianz activated (GDPR/TTDSG). Its wizard should still be run to tune categories. |
| 🟡 Feed lacked dimensions | ✅ Feed regenerated with `product_length/width/height` and `shipping_label`. |

### Still open
1. **Fake `+357` phone in the raw theme template.** Hidden by CSS and stripped from the DOM by
   JS, so visitors never see it, but the string remains in the served HTML source. Requires a
   theme-file edit (instructions supplied to the owner).
2. **`itemCondition` absent from Product JSON-LD.** The host WAF rejects any payload resembling
   schema manipulation. Condition is present on-page and in the feed, which is Merchant
   Center's primary source.
3. **Delivery pricing.** Only store pickup is configured; freight cost is quoted individually.
   Keep the Versand policy, checkout and Merchant Center shipping settings consistent with that.
4. **Business registration.** Owner has stated the business is not yet registered and has
   decided to keep checkout active. Recorded here once as an accepted business decision.
5. **Real store photography** for the About/store sections.
6. **LiteSpeed → Toolbox → Purge All** so visitors receive the current HTML.

### Status
**Ready after minor corrections** for the technical/on-site criteria: business identity, contact
routes, policies, price transparency, availability, condition, product data and structured data
are in place and mutually consistent. Item 4 above is a business-side matter outside the
website build. Submit only with explicit authorization; approval is never guaranteed.
