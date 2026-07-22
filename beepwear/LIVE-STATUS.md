# BeepWear — Live Site Status (beepwear.com)

Snapshot of what has been done on the live WordPress site via the REST API.

## Done (live)

- **WooCommerce 10.9.4** + **Rank Math SEO** installed & active.
- **Store settings:** 510 Main St, Wall, SD 57790, US · currency USD.
- **Categories** (4) + **Brands** (~40 native `product_brand` terms) created.
- **269 approved products imported** (status = **draft**): name, price, description,
  category, brand, stock.
- **Product images:** all **269/269** attached — sideloaded from the owner's
  citysvending.com (owner-confirmed rights) and re-hosted on beepwear.com.
- **Brands assigned:** 267/269 (2 ambiguous names pending manual: "Platinum Vintage Pery…",
  "E. Howard Watch Co…").

## Remaining before publish + Merchant Center

1. **Theme (GUI step):** site is on default Twenty Twenty-Five. The BeepWear child theme
   (`theme/beepwear/`) must be uploaded via Appearance → Themes → Add New → Upload (or SFTP);
   the REST API can't upload a theme zip. Requires Hello Elementor parent + Elementor.
2. **Publish products:** currently draft. Publish after theme + policy pages are live.
3. **Policy/content pages:** not yet published — need remaining business facts (hours,
   return window, shipping costs, governing-law state) to clear `[confirm: …]` markers.
4. **Descriptions:** kept set is unique + non-placeholder; still spot-check for copied
   manufacturer copy (originality) before submission.
5. **GTINs:** none — add where real; never invent.
6. **Merchant Center:** connect Google for WooCommerce, map category (Watches=201),
   condition=new; submit only after audit BLOCKERs clear. Approval never guaranteed.

## Access
- Auth: WordPress Application Password (admin `tcoculick@gmail.com`). Revoke when done.
