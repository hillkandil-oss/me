# Editorial, professional & technical requirements + product-data spec

These are the "is this a real, functioning, professional store and is the feed
clean" checks. They cause disapprovals and, in aggregate, contribute to account
suspensions. The AI-led reviewer reads the rendered landing pages, so polish and
functionality on the *public* site matter.

## Landing-page & editorial requirements

The destination (landing) page for every product must be:

- **Live and complete** — no "under construction", no coming-soon, no empty
  category pages.
- **Free of broken pages / dead links / missing images.**
- **Mobile-friendly and fast** — reviewers and shoppers are mobile-first.
- **Purchasable** — each advertised product can actually be bought on the page.
- **Placeholder-free** — no "Lorem ipsum", sample text, or leftover template
  copy (`[confirm: …]`, `TODO`, `TBD`, empty `** **`).

Editorial style (avoid "gimmicky" attention-grabbing):

- No gratuitous **ALL CAPS** in titles/descriptions.
- No gimmicky symbols, excessive punctuation, or emoji spam (`$$$`, `!!!`,
  `★★★` used as decoration).
- No raw HTML tags or broken encoding in visible product text.
- No promotional text stuffed into the **title** or **description** attribute
  (e.g. "FREE SHIPPING!!!", "BUY NOW", price/discount, phone numbers, your
  store name jammed in). Promotions belong in promotion features, not the title.
- Correct spelling and grammar; write for a shopper, not for keyword stuffing.

## Product-data specification (feed) — required & recommended

Send fresh data at least every **30 days**; data must meet Google's quality bar.

**Required (per product):**
- `id` — unique, stable.
- `title` — accurate, specific; brand + product + key attributes; no promo text.
- `description` — original, accurate, describes the actual item.
- `link` — direct, working product URL (HTTPS).
- `image_link` — see image rules below.
- `price` — matches landing page and checkout exactly, correct currency.
- `availability` — `in stock` / `out of stock` / `preorder`, matching the page.
- `brand` — required for most categories (incl. watches, apparel, electronics).
- `condition` — `new` / `refurbished` / `used`; must match reality.
- **Identifiers:** `gtin` (UPC/EAN/ISBN) and/or `mpn`. If a product genuinely
  has no GTIN, set `identifier_exists = no`. **Never invent a GTIN** — fabricated
  identifiers are their own violation.
- `google_product_category` where relevant (e.g. Apparel & Accessories >
  Jewelry > Watches = 201).

**Data-quality rules:**
- Titles/descriptions must be **unique and original** per product — reusing one
  generic blurb across many products is treated as low-quality/duplicate content
  and is a common reason large catalogs get thinned or disapproved.
- Feed values must match the landing page (price, availability, condition,
  title, image). Mismatch = misrepresentation.
- AI-generated titles/descriptions must go in the **`structured_title` /
  `structured_description`** attributes (2026 requirement), not silently in the
  normal fields.

## 2026 image & attribute updates (watch these deadlines)

- **Image minimum size is rising to 500×500 px** for non-apparel (apparel
  higher). Sub-spec images get disapproved — re-export product imagery at or
  above the new minimum. Confirm the current exact threshold at audit time.
- Images must show the **actual product** on a clean background, no promotional
  overlays, watermarks, borders, or added text/logos.
- No placeholder/"image coming soon" graphics.
- Richer media and clearer shipping attributes are increasingly expected —
  populate structured shipping data rather than burying it in prose.

Because these thresholds shift, when the exact current number matters, verify
against Google's live product-data specification rather than trusting a cached
figure.

## Audit checklist — editorial & technical

- [ ] Every landing page live, complete, mobile-friendly, fast, purchasable.
- [ ] No broken links / missing images / under-construction / placeholder text.
- [ ] No ALL-CAPS, symbol spam, HTML tags, or promo text in titles/descriptions.
- [ ] Titles/descriptions original and unique per product.
- [ ] Required feed attributes present (id, title, description, link, image,
      price, availability, brand, condition, identifiers or identifier_exists=no).
- [ ] Feed values match landing pages exactly.
- [ ] Images meet current minimum size, show the real product, no overlays.
- [ ] AI-written copy placed in structured_title / structured_description.
- [ ] Feed refreshed within the last 30 days.
