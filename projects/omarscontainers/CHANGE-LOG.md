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

## Verified during this session, no change required

- **Sale pricing is genuine.** 9 of 116 products are discounted, 6.8%–38.7%, no uniform
  pattern, and **zero** cases of `sale_price == regular_price` (fake strikethrough). No
  misleading-discount exposure.
  *Note:* German PAngV §11 requires that an advertised reduction also state the lowest price
  charged in the preceding 30 days. Needs handling before these discounts run publicly.

---

## Not yet done — still blocking submission

1. **Bank account details (IBAN/BIC) not set** — orders can be placed but not paid
2. No legal pages (Impressum, Datenschutz, Widerruf, AGB, Versand, Zahlung, Kontakt)
3. 110 descriptions still copied from third-party sites
4. Business identity (email, phone, address) not visible on the homepage
