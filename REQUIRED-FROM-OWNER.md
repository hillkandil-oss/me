# Required From Store Owner — kaisercontainers

Nothing below will be published, guessed, or fabricated. Each item blocks the pages/features
listed until you confirm a verified value. Send answers and I'll fill them in.

Legend: 🔴 blocks publication · 🟠 blocks a specific page/feature · 🟡 improves trust/SEO

## 🔴 Legal & identity (German law — Impressum, §5 DDG/TMG)
| # | Item | Needed for | Status |
|---|---|---|---|
| 1 | **Store phone number** | Header, footer, contact, schema, feed | ✅ **+49 201 49869542** applied site-wide (note: 0201 is the *Essen* code, store is in Duisburg/0203 — confirm if wrong) |
| 2 | **Responsible person / owner full name** | Impressum | ✅ **Kaiser Williams** applied |
| 3 | **Exact street + house number** (currently only "Homberg/Ruhrort/Baerl") | Address everywhere, Maps pin, schema | ⏳ |
| 4 | **USt-IdNr.** (VAT ID) | Impressum, invoices, feed tax | ⏳ |
| 5 | **Handelsregisternummer + registry court** (if registered) | Impressum | ⏳ |
| 6 | **Legal form** (e.g. Einzelunternehmen, GmbH) | Impressum, AGB | ⏳ |

## 🔴 Commerce facts
| # | Item | Needed for | Status |
|---|---|---|---|
| 7 | **Container condition** — confirmed **new + used both sold** | Product labels, feed `condition` | ✅ confirmed |
| 8 | **Prices net or gross?** (B2B container sales are often net + 19% VAT) | Price display, checkout, feed | ⏳ |
| 9 | **Real shipping costs** for containers (heavy freight — flat, by zone, or on request?) | Cart, checkout, Versand policy, feed | ⏳ |
| 10 | **Warranty / Gewährleistung terms** | Warranty policy, product pages | ⏳ |
| 11 | **Store-pickup details** — address/hours/prep/ID/holding period for collection | Pickup section, checkout | ⏳ (pickup = YES confirmed; details needed) |

## 🟠 Location & contact detail
| # | Item | Needed for | Status |
|---|---|---|---|
| 12 | **Geo coordinates** (lat/long of the real premises) | LocalBusiness schema, map | ⏳ (derive from confirmed street address) |
| 13 | **Nearby landmark** | Contact page (optional) | ⏳ |
| 14 | **Parking / public transport / accessibility** | Store-visit section | ⏳ |

## 🟡 Brand & media
| # | Item | Needed for | Status |
|---|---|---|---|
| 15 | **Real logo** (or approve the proposed placeholder wordmark) | Header, footer, schema | ⏳ |
| 16 | **Brand colors** (or approve proposed industrial palette) | Design system | ⏳ proposed, awaiting approval |
| 17 | **Real photos** of store premises + actual containers | Hero, product pages, About | 🔴 must be real; no AI misrepresentation |
| 18 | **Verified social-media profile links** | Header/footer | ⏳ (omit until verified) |

## 🟡 Product data (per product, for the feed)
| # | Item | Status |
|---|---|---|
| 19 | **Condition (Neu/Gebraucht)** | ✅ applied to all 20 products (17 neu, 3 gebraucht) |
| 20 | **Dimensions + weight** — confirm standard ISO figures in `docs/product-dimensions-reference.md` (or send actual) | ⏳ all 20 products currently blank |
| 21 | **GTIN/EAN** — only if real (containers usually have none → feed uses `identifier_exists=no`) | ⏳ optional |
| 22 | **Material / colour / what's included** per product (optional, improves feed) | ⏳ |

_Feed generated: `data/merchant-center-feed.csv` (20 real rows) · gaps: `data/product-feed-audit.csv`._

---
_Last updated: 2026-08-04 · maintained during the build._

## ⚠️ Theme demo data found in template (needs a permanent fix)
The Tranzix theme header hardcodes **fake contact data**: phone `+357 984538` (Cyprus)
and a dead `mailto:#` link, in `.header-top-two`. It is now removed from the rendered
page (CSS hide + JS DOM removal), but the string still exists in the theme's PHP
template, so it remains in the raw HTML source.

**Permanent fix (recommended before Merchant Center submission):** edit the theme
header template in a child theme (or via Hostinger File Manager) to delete that block,
or replace the values with the real store phone once confirmed. Fabricated contact
details are a Merchant Center misrepresentation risk.

## ⚠️ Contact form must be configured in wp-admin (CF7 REST does not persist)
Contact Form 7's REST endpoint returns success but discards writes, and its post type is
not in the WP REST API. The form is therefore still CF7's **English default**, and it emails
the **site-admin address instead of info@kaisercontainers.de**.

Styling + German labels are applied automatically; the fields, recipient and confirmation
mail must be pasted in once. Full copy-paste instructions: `docs/contact-form-setup.md`.
