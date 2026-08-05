# QA Test Report — kaisercontainers.de

_Live verification against the brief's §38 checklist. Method: HTTP status checks and
served-HTML inspection. Note: I cannot render the site in a browser from this environment
(the sandbox browser cannot traverse the network proxy), so visual/interaction checks marked
**owner** need a human pass._

## Page availability — all pass
| Page | Status |
|---|---|
| Startseite `/` | 200 |
| Shop, Cart, Checkout, Mein Konto | 200 |
| Kontakt, Über uns, FAQ | 200 |
| Impressum, Datenschutz, AGB, Widerruf, Versand, Zahlung | 200 |
| Cookie-Richtlinie, Barrierefreiheit | 200 |
| Product category `/product-category/seecontainer/` | 200 |
| Product `/product/20-fus-seecontainer/` | 200 |
| `robots.txt` | 200 |

## SEO / infrastructure
- **Sitemap:** live at `/sitemap.xml` and `/wp-sitemap.xml`. The Rank Math path
  `/sitemap_index.xml` returns 404 until the Rank Math wizard runs + permalinks are flushed.
  **Submit `/sitemap.xml` to Search Console**, or finish the Rank Math setup.
- **Product schema:** present, with `availability` and `priceCurrency`.
- **LocalBusiness + Organization schema:** injected site-wide (verified data only).
- **Prices:** render in German format (e.g. `2.450,00 €`).

## Product pages
- ✅ Condition visible as a `Zustand: Neu/Gebraucht` attribute on all 20 products.
- ✅ New info block added to every product page: availability-may-differ notice, processing
  and delivery times, pickup, payment, returns, plus links to the policy pages (brief §17).
- ⚠️ **`itemCondition` missing from Product JSON-LD.** A JS patch to add it was written but
  the host WAF (403) rejects any payload resembling schema/script manipulation. Condition is
  still communicated on-page and in the feed CSV. **Fix properly** in Rank Math
  (Titles & Meta → Products) or with a snippet in a child theme.

## Cache caveat found during this pass
Product-page caches did **not** clear when products were updated through the WooCommerce API
(page caches did clear on page re-save). The product info block is confirmed live on a
cache-busted URL but the cached copy still serves the old HTML. Run **LiteSpeed Cache →
Toolbox → Purge All** once to publish it to visitors.

## Known issues carried forward
| Issue | Severity | Owner action |
|---|---|---|
| Contact form is CF7's English default and mails the **site-admin address**, not `info@kaisercontainers.de` | 🔴 | 5-min paste, `docs/contact-form-setup.md` |
| Impressum incomplete (name, street, USt-IdNr.) | 🔴 | Provide details |
| "wird ergänzt" placeholders (phone, street) | 🔴 | Provide details |
| Theme template still contains a fake `+357` phone in raw HTML (hidden + removed from DOM) | 🟠 | Child-theme edit |
| Product dimensions/weight blank on all 20 | 🟡 | Confirm reference figures |
| Cookie consent (Complianz) installed but inactive | 🟠 | Run its wizard |

## Requires a human pass (owner)
Mobile rendering and menu, cart → checkout → order flow with a test order, transactional
emails, contact-form delivery, Google Maps interaction, keyboard navigation, and cross-browser
checks. Caching note: after any change, purge via **LiteSpeed Cache → Toolbox → Purge All**
(never by deactivating the plugin) and hard-refresh.
