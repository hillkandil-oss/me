# QA Test Report — kaisercontainers.de

_Verified against the live public URLs (not API responses), after a full cache purge.
Last run: 2026-08-06._

## Page availability — all pass
All 16 pages return **HTTP 200**: Startseite, Shop, Kontakt, Über uns, FAQ, Impressum,
Datenschutz, AGB, Widerruf, Versand, Zahlung, Cookie-Richtlinie, Barrierefreiheit, Warenkorb,
Kasse, Mein Konto. Product and category pages 200. Homepage responds in ~1.4s.

## Identity & contact
| Check | Result |
|---|---|
| Real phone `+49 201 49869542` | ✅ present, clickable `tel:` |
| Real address (Homberg/Ruhrort/Baerl, 47138 Duisburg) | ✅ present, matches Impressum |
| Impressum: responsible person, address, phone | ✅ complete for the facts held |
| Fabricated `+357 984538` phone | ✅ **0 occurrences in raw HTML** |
| Fabricated `House 35 R/A, Street` address | ✅ **0 occurrences in raw HTML** |
| Dead `tel:#` / `mailto:#` links | ✅ 0 |
| Placeholder text (`wird ergänzt`, `Mustermann`, `beispiel.de`) | ✅ 0 |
| English demo UI (`Sing Up`, `Our Address`, `Call Us`, `e-mail us`) | ✅ 0 |
| Contact form recipient | ✅ `info@kaisercontainers.de` |

## Product pages
| Check | Result |
|---|---|
| `itemCondition` in Product schema | ✅ (PHP snippet; the JS route was WAF-blocked) |
| Availability + `priceCurrency` in schema | ✅ |
| Shipping / pickup / returns block (brief §17) | ✅ on every product |
| `Zustand` Neu/Gebraucht | ✅ all 20 |
| `Abmessungen` (ISO dimensions) | ✅ all 20 |
| Price in German format + `zzgl. Versandkosten` | ✅ (7 hits product page, 18 shop) |

## Front-end & infrastructure
| Check | Result |
|---|---|
| Viewport meta (was missing entirely) | ✅ added — phones no longer render at desktop width |
| Brand logo (replaced Tranzix demo) | ✅ |
| Favicon (replaced red placeholder) | ✅ |
| Header: contact bar, search, cart with live count | ✅ |
| Footer: full-bleed, NAP, policy links, payment icons | ✅ |
| Cookie consent (Complianz, prior opt-in) | ✅ |
| Homepage meta description (DE) | ✅ |
| Sitemap | ✅ `/sitemap.xml` (Rank Math's `/sitemap_index.xml` still 404 pending its wizard) |
| LocalBusiness + Organization schema | ✅ |

## Open items
| Item | Severity | Owner action |
|---|---|---|
| Business not registered (no Gewerbeanmeldung, no VAT ID) | 🔴 | Business-side; can fail Google's merchant verification regardless of site quality |
| No street + house number | 🟠 | District address used consistently and matches the Impressum |
| Genuine reviews / trust badge | 🟡 | Only via a real provider (Google Customer Reviews, Trustpilot). Never fabricated |
| Real photographs of the premises | 🟡 | Product photography is real and in use; no premises photo exists yet |
| Delivery pricing | 🟡 | Pickup configured; freight quoted individually. Keep policy, checkout and Merchant Center consistent |
| Rank Math wizard + permalink flush | 🟡 | Enables `/sitemap_index.xml` and per-page SEO titles |

## Requires a human pass
Cart → checkout → order with a test payment, transactional emails, contact-form delivery,
Google Maps interaction, keyboard navigation and cross-browser checks.

## Operational notes
- After any change, purge via **LiteSpeed Cache → Toolbox → Purge All**, then hard-refresh.
  **Never** purge by deactivating the plugin: the site times out without its cache.
- Verify from the public URL. Several fixes that appeared applied via the API were still
  serving stale HTML, and CSS/JS-only fixes do not change what a crawler reads.
