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
