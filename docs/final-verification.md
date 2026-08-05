# Final Verification Pass — kaisercontainers.de

_Run on the live site, 2026-08-05, after a full LiteSpeed purge. All checks on plain
(non-cache-busted) URLs — i.e. what a visitor actually receives._

## Availability
All 16 pages return **HTTP 200**: Startseite, Shop, Kontakt, Über uns, Impressum,
Datenschutz, AGB, Widerruf, Versand, Zahlung, FAQ, Cookie-Richtlinie, Barrierefreiheit,
Warenkorb, Kasse, Mein Konto. Product and category pages 200. Homepage responds in ~1.4s.

## Homepage
| Check | Result |
|---|---|
| Real phone `+49 201 49869542` | ✅ 6 occurrences |
| Address (Homberg / 47138 Duisburg) | ✅ 7 |
| Top contact bar | ✅ |
| Footer with NAP + policy links | ✅ |
| Hero + industrial backgrounds + motion | ✅ |
| Real product photo in the About section | ✅ |
| Contact form as the final content section | ✅ |
| Payment icons + footer logo | ✅ |
| LocalBusiness schema | ✅ |
| **Placeholder text remaining** | ✅ **0** |
| **Fabricated `+357` phone in source** | ✅ **0** |
| **Dead `tel:#` / `mailto:#` links** | ✅ **0** |

## Product page
| Check | Result |
|---|---|
| `itemCondition` in Product schema | ✅ (fixed via PHP snippet after the WAF blocked the JS route) |
| Availability in schema | ✅ |
| Shipping / pickup / returns info block (§17) | ✅ |
| `Zustand` (Neu/Gebraucht) attribute | ✅ |
| `Abmessungen` dimensions attribute | ✅ |
| Price in German format (`2.450,00 €`) | ✅ |
| `zzgl. Versandkosten` note (PAngV) | ✅ (added by snippet; Woo's built-in suffix only renders when tax calc is on) |

## Policy / legal pages
Kontakt, Impressum, Über uns, AGB: all 200, real phone present, **zero placeholders**,
**zero fabricated data**.

## Media
- 9/9 product categories now have real category images taken from actual product photography.
- Homepage About section uses a real container photo from the catalogue, captioned
  "Beispiel aus unserem Sortiment" so it is not presented as a photograph of the premises.
- No stock or AI imagery was introduced. Genuine photographs of the physical location are
  still worth adding when available.

## Live PHP snippets (Code Snippets plugin)
| id | Purpose |
|---|---|
| 5 | Replace the theme's fabricated demo contact data in the rendered HTML |
| 6 | Add `itemCondition` to WooCommerce / Rank Math product schema |
| 7 | One-time LiteSpeed purge (single-use) |
| 8 | Append the `zzgl. Versandkosten` price note |

Sources kept in `theme/snippets/`.

## Operational notes
- The site is slow while the cache is cold: a burst of concurrent requests immediately after a
  purge can time out. It recovers as the cache refills. Do not purge by deactivating LiteSpeed.
- Remaining owner items: run the Complianz cookie wizard, and supply genuine photographs of the
  premises if you want them shown.
