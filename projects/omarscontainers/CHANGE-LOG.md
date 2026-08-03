# omarscontainers.de — Change Log

Every write made to the live site, with the authorisation behind it. Read-only inspection
is not logged; only changes.

---

## 2026-08-03 — Store identity, region, B2C tax, sender address

**Authorised by owner:** *"set address to Essen an support email to info@omarscontainers.de
is a B2C"*

### WooCommerce → General

| Setting | Before | After |
|---|---|---|
| `store_address` | *(empty)* | `Karnaper Str. 177 A` |
| `store_city` | *(empty)* | `Essen` |
| `store_postcode` | *(empty)* | `45329` |
| `default_country` | `DE:DE-HH` (Hamburg) | `DE:DE-NW` (North Rhine-Westphalia) |
| `currency` | `EUR` | `EUR` (unchanged, confirmed) |
| `calc_taxes` | `no` | `yes` |
| `allowed_countries` | `all` | `specific` → `[DE]` |
| `ship_to_countries` | *(empty)* | `specific` → `[DE]` |

Region was wrong: the store was configured for Hamburg while the business operates from
Essen. Corrected — NAP consistency across site, schema, GBP and Merchant Center depends on it.

Selling and shipping scope narrowed to Germany per intake ("Shipping countries: Germany").
Previously the store offered worldwide sale with no rates configured.

### WooCommerce → Tax (B2C configuration)

| Setting | Before | After |
|---|---|---|
| `prices_include_tax` | `no` | `yes` |
| `tax_display_shop` | `excl` | `incl` |
| `tax_display_cart` | `excl` | `incl` |
| `price_display_suffix` | *(empty)* | `inkl. 19 % MwSt. zzgl. Versandkosten` |
| `tax_based_on` | `shipping` | `shipping` (unchanged) |

Created tax rate: **DE · 19.0000% · "MwSt." · standard class · shipping taxed**.

**Pricing impact — no change to what customers pay.** Existing prices are now treated as
gross (VAT-inclusive), so a €4,660 product still displays €4,660, composed of €3,915.97 net
+ €744.03 VAT.

> **Owner confirmation still needed:** if those figures were intended as *net* supplier
> prices, the store is now absorbing the 19% rather than adding it, and prices need raising
> (€4,660 net → €5,545.40 gross). Say the word and this can be bulk-adjusted.

### WooCommerce → Emails

| Setting | Before | After |
|---|---|---|
| `email_from_address` | `hillkandil@gmail.com` | `info@omarscontainers.de` |
| `email_from_name` | `omarscontainers.de` | `omarscontainers` |

Transactional email previously sent from a personal Gmail address — poor trust signal and
inconsistent with the business identity.

> **Unverified:** that `info@omarscontainers.de` exists and receives mail. The intake gave
> the support address as `info@omarscontainers.com` (.com); the owner then specified `.de`.
> Deliverability must be tested before launch — transactional email that bounces is a
> checkout failure.

---

## 2026-08-03 (cont.) — Duplicate removal + brand assignment

**Authorised by owner:** *"continue"*

### Duplicate products removed

Six SKUs each existed twice — verified byte-identical (same name, description, price and
image count) before removal. The older copy of each pair was kept; the newer duplicate was
moved to **trash**, not permanently deleted, so all six are restorable from
Products → Trash.

| SKU | Kept | Trashed |
|---|---|---|
| CL3ST2660 | 2974 | 4197 |
| CL3ST2661 | 2980 | 4172 |
| CL3ST2662 | 2994 | 4165 |
| CL3ST2663 | 2999 | 4148 |
| CL3ST2664 | 3011 | 4115 |
| CL3ST2665 | 3029 | 4103 |

Live catalogue: **116 → 110**. Duplicate SKUs remaining: **0**.

> *Correction to the earlier audit:* finding B5 said "twelve duplicate products". Twelve
> products were *involved* in duplication, but only **six** were redundant. Six were removed.

### Brands assigned — 58 of 110

Created 18 `product_brand` terms and assigned them. **Every brand was taken from the
product's own title** — none inferred, none invented.

Aiper · Anssems · Beatbot · Cheval Liberté · Daikin · EcoFlow · Eduard · Fendt · FOCO ·
Franc · Gree · Humbaur · Ifor Williams · Mitsubishi · Remko · Stahlworks · TPV · Variant

The remaining **52 products were deliberately left without a brand** — unbranded containers,
sanitary units and pools where no manufacturer is evidenced. These should carry
`identifier_exists: no` in the feed rather than a fabricated brand.

### Still open on product data

- **Two Remko pairs share a title but have different SKUs** (ids 3602/3631 and 3613/3638,
  identical prices, 7 vs 6 images). Not touched — needs an owner decision on whether these
  are genuinely distinct stock or a second duplicate import.
- Condition attribute still unset on all 110 (blocked on MI-10: new or used?).
- Descriptions still copied from third-party sources.

---

## 2026-08-03 (cont.) — Payment, shipping, condition

**Authorised by owner:** *"payment is through bank transfer freighted is a flat rate of
170euros an its new stock"*

### Payment — checkout now functions

| Setting | Before | After |
|---|---|---|
| `bacs` (Direct bank transfer) | disabled | **enabled** |
| Title | "Direct bank transfer" | "Überweisung (Vorkasse)" |

> ### ⚠ BANK ACCOUNT DETAILS ARE NOT SET — customers cannot actually pay
> BACS is enabled, but no account details are configured. A customer completing checkout
> is shown payment instructions with **no IBAN to transfer to**. Orders will be placed and
> never paid.
>
> Needed: **account holder · IBAN · BIC · bank name**.
> WooCommerce → Settings → Payments → Direct bank transfer → Account details.
> This is a launch blocker, not a nicety.

### Shipping — Deutschland zone

| Item | Value |
|---|---|
| Zone | Deutschland (id 1), country `DE` |
| Method | Flat rate — "Speditionsversand (Pauschale)" |
| Cost entered | `142.86` net |
| **Customer pays** | **€170.00** (142.86 net + 27.14 VAT) |
| Tax status | taxable |

First set to `170`, which WooCommerce treated as **net** — customers would have been charged
**€202.30**. Corrected to 142.86 net so the gross charge is exactly the €170 specified.

> If €170 was meant as a *net* figure with VAT on top (customer pays €202.30), set the cost
> back to `170`.

### Condition — new stock

Created global attribute **Zustand** (id 1) with term **Neu**, applied to **110/110**
products, visible on the product page. Feeds `condition: new` and schema `itemCondition:
NewCondition`.

### End-to-end checkout test — PASSED

Real cart via the public Store API, unauthenticated:

```
product          €4,660.00  (gross, incl. 19% MwSt)
shipping         €  170.00  (gross, incl. 19% MwSt)
ORDER TOTAL      €4,830.00
```

Shipping rates resolve, tax calculates correctly, and `bacs` is offered as a payment method.
**A customer can now complete checkout** — subject to the bank details warning above.

### Re-audit after these changes

Blockers cleared: no-payment-gateway, no-shipping. Remaining 6 blocking findings are all
**missing legal/policy pages** plus business identity not visible on the homepage — the
next work package.

---

## 2026-08-03 (cont.) — Legal pages, footer, business identity

**Authorised by owner:** *"start the website building"*

### Ten pages created and published

| URL | Purpose |
|---|---|
| `/impressum/` | §5 DDG legal notice |
| `/datenschutz/` | GDPR privacy policy (Art. 13) |
| `/widerrufsrecht/` | 14-day withdrawal + Muster-Widerrufsformular |
| `/agb/` | Terms of business |
| `/versand-und-lieferung/` | Shipping, freight, collection |
| `/zahlungsarten/` | Payment methods and process |
| `/rueckgabe-erstattung/` | Returns and refunds |
| `/kontakt/` | Contact |
| `/standort/` | Visit us — address, hours, viewing, collection |
| `/ueber-uns/` | About |

All content uses **only owner-confirmed facts**. Every unknown is a visible
`[BESTÄTIGEN: …]` marker on an amber background — it cannot be mistaken for real
content and cannot silently ship. Nothing was invented.

Outstanding markers: legal entity name and Rechtsform · managing director · telephone ·
Handelsregister number · USt-IdNr. · bank details · cookie inventory · delivery-access
requirements · excluded return categories · storefront photos · company history.

### Wiring

- AGB set as the WooCommerce checkout terms page (id 22941)
- WordPress boilerplate drafts `privacy-policy` and `refund_returns` moved to trash
- Footer template part extended with a business-identity block (name, address, email,
  opening hours) and two link columns (Service, Rechtliches)
- VAT/shipping notice added site-wide per PAngV
- LiteSpeed cache purged and public rendering verified

The theme is a **block theme**, so classic menu locations do not exist; the footer was
edited as a template part rather than via a nav menu.

### Re-audit — all blockers cleared

| | Before | After |
|---|---|---|
| BLOCKER | 5 | **0** |
| CRITICAL | 6 | **0** |
| HIGH | 6 | 3 |

Remaining: 52 unbranded products (correct — no brand evidenced), Product schema lacking
`itemCondition`, no telephone, and the two Remko title duplicates.

### Auditor bugs found and fixed while doing this

1. **English-only policy slugs** reported all German pages as missing — 5 false CRITICALs.
   Added DE slugs (`impressum`, `datenschutz`, `agb`, `widerruf…`, `versand…`, `kontakt`,
   `ueber-uns`).
2. **Address heuristic** matched only English street words, so `Karnaper Str. 177 A` read
   as "no physical address" — 1 false CRITICAL. Added German forms
   (`str.`, `straße`, `weg`, `platz`, `allee`, `gasse`, `ring`, `damm`).
3. **No Impressum check at all** despite it being legally mandatory. Added, gated on the
   site looking German, at BLOCKER severity.
4. **Non-ASCII URLs crashed the auditor** (`UnicodeEncodeError` on `über-uns`) — introduced
   by fix 1. Request URLs are now percent-encoded with IDNA host handling, which also makes
   umlaut product URLs work.

Fixture regression re-run after all four: 24 findings, unchanged distribution.

---

## 2026-08-03 (cont.) — Removed inherited false and unsubstantiated claims

**Authorised by owner:** *"continue"*

Scanned all 110 descriptions for claims inherited from the copied supplier text that are
untrue of this business, unenforceable, or unsubstantiated.

### Removed — pre-acceptance damage clause (1 product, id 2615)

> *"Trotz sorgfältiger Verladung können minimale Dellen oder Kratzer entstehen — mit der
> Auftragsannahme gilt dieser Hinweis als gelesen und akzeptiert."*

Copied text attempting to make the buyer waive damage claims simply by ordering. Two
problems: a liability waiver buried in a product description is very unlikely to be
enforceable against a consumer under German law, and it carries Abmahnung risk. The
factual part (walls ship with protective film) was **kept**; only the waiver was removed.

### Removed — market-comparative claims (3 products, ids 3411, 3435, 3663)

*"10 Jahre Garantie (einzigartig am Markt)"* · *"(einzigartig auf dem Markt)"* ·
*"einzigartig auf dem Markt"*

"Unique on the market" is a factual claim about competitors that cannot be substantiated,
and is exactly the unsupported-claim category Merchant Center treats as misrepresentation.
The **warranty term itself was kept** — only the comparative boast was cut. Ordinary
marketing language such as *"einzigartiges Design"* was deliberately left alone.

### Verified clear afterwards

| Claim category | Remaining |
|---|---|
| Market-comparative claims | **0** |
| Pre-acceptance waiver | **0** |
| "aus unserem Hause/Werk" (own factory) | **0** |

> A first pass matched only `(einzigartig am Markt)` and missed
> `(einzigartig auf dem Markt)`. Caught on verification and re-run against freshly fetched
> data rather than the stale local copy.

---

## ⚠ OWNER DECISION — delivery times contradict the shipping policy

Six products state their own delivery time inside the description, and it disagrees with
`/versand-und-lieferung/`:

| Product id | Description says | Shipping policy says |
|---|---|---|
| 21736, 21741, 21743 | 15 bis 20 Tage | 2 bis 5 Werktage |
| 21749, 21757 | 15–20 Tage | 2 bis 5 Werktage |
| 22870 | 07 – 15 Tage | 2 bis 5 Werktage |

**Not changed, deliberately.** Either figure could be the true one and guessing would put a
false delivery promise on the site — which is both a Merchant Center contradiction and, under
German consumer law, an inaccurate delivery date.

Most likely explanation: 2–5 days is right for stocked goods, while container pools are
manufactured to order and genuinely take 15–20 days. If so the fix is a per-product
delivery time plus a shipping policy that explains both cases — not deleting either number.

**Needed:** confirm the real lead time for made-to-order pools, and whether 2–5 working days
applies only to in-stock items.

### Warranty claims — also needs confirmation

Three trailer products advertise **10 Jahre Garantie**. The AGB currently carries a
`[BESTÄTIGEN]` marker for warranties. Confirm whether this is the manufacturer's guarantee
(state whose, and link the terms) or one you grant yourself — an advertised guarantee you
cannot honour is a misrepresentation.

---

## 2026-08-03 (cont.) — Agent 8: homepage and site identity

**Authorised by owner:** *"continue with the building of the website"*

### The site had no homepage

`show_on_front` was `posts` — the front page was a **blog feed**, not a storefront. That is
why the homepage read as thin in every earlier audit. Created `/startseite/` (id 22958) and
set it as the static front page.

### Homepage content

| Section | Content |
|---|---|
| Hero | H1, plain-language summary of what is sold, "Alle Artikel sind Neuware", two CTAs (Shop, Standort) |
| Trust row | Physical location + hours · shipping €170 incl. VAT · 30-day returns with return postage paid |
| Categories | All 10 categories with live product counts, linked |
| Buying info | Payment process, gross-price/VAT statement, collection discount |
| Pre-sales | Contact route with a stated response time |

Every figure matches the policy pages — shipping €170, 30 days, 0–1 working day processing,
19% VAT. Nothing invented.

**Deliberately excluded:** countdown timers, stock-scarcity messages, visitor counters,
fabricated reviews, trust badges, awards, press mentions, and any "best/cheapest/number one"
claim. Those are §40 automatic failure conditions and the fastest route to a
misrepresentation flag.

### Site identity

| Setting | Before | After |
|---|---|---|
| Site title | `omarscontainers.de` | `omarscontainers` |
| Tagline | *(empty)* | `Container, Poolcontainer und Anhänger — Neuware aus Essen` |
| `show_on_front` | `posts` | `page` |

### Verified on the rendered page

H1 present · 10 category links · "Neuware" · €170 · 30 Tage · address · opening hours ·
Impressum link · **0 unresolved `[BESTÄTIGEN]` markers** · no placeholder text.

### Audit

Still **0 blocking findings**. Remaining: 3 HIGH, 2 MEDIUM.

### Not done — needs assets or owner input

- **All 10 categories have no image.** Category cards are text-only. Needs real photographs
  of actual stock — stock photography of containers the business does not own would be
  misrepresentation.
- Telephone number still absent (HIGH).

---

## 2026-08-03 (cont.) — Agent 5: navigation

**Authorised by owner:** *"yes"*

### The header had no navigation

The header's `wp:navigation` block referenced menu **6493**, and the footer's referenced
**320**. Both IDs return `rest_post_invalid_id` — **neither menu exists**. The rendered
header therefore contained exactly one link: the site title. No shop, no categories, no
cart. Customers had no way to browse the catalogue except by guessing URLs.

This is why the store looked empty despite holding 110 published products.

### Built

Created navigation **Hauptnavigation** (id 22959) and repointed both the header and footer
blocks at it.

```
Shop ▾
  Klimaanlage (21) · Anhänger (15) · Wohncontainer (15) · Pferdeanhänger (10)
  Poolcontainer (10) · Sanitärcontainer (10) · Bootsanhänger (9)
  Poolroboter (8) · Lagercontainer (6) · Werkstattcontainer (6)
Standort · Kontakt · Warenkorb
```

### Verified

Header renders **15 links**, including all **10 category links**. Every destination checked
individually — **14/14 return HTTP 200**, no 404s or redirects.

---

## Verified during this session, no change required

- **Sale pricing is genuine.** 9 of 116 products are discounted, 6.8%–38.7%, no uniform
  pattern, and **zero** cases of `sale_price == regular_price` (fake strikethrough). No
  misleading-discount exposure.
  *Note:* German PAngV §11 requires that an advertised reduction also state the lowest price
  charged in the preceding 30 days. Needs handling before these discounts run publicly.

---

## Not yet done — still blocking submission

1. **Bank account details (IBAN/BIC) not set** — orders can be placed but not paid
3. 110 descriptions still copied from third-party sites (claims cleaned; wholesale rewrite outstanding)
6. Delivery times on 6 products contradict the shipping policy — owner decision
4. Telephone number not published
5. Product schema missing itemCondition
