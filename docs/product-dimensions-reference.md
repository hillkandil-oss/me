# Standard Container Dimensions — for owner confirmation

All 20 products currently have **no dimensions/weight** in WooCommerce. These matter for
buyers, product pages, and the Merchant Center feed. Below are the **standard ISO nominal
external dimensions** for each container type. They are industry-standard specs, **not
measured values** — please confirm (especially for used units, which vary), then I'll apply
them to the products and feed.

| Type | Length | Width | Height | Typical tare weight |
|---|---|---|---|---|
| 6 ft | 1.98 m | 2.00 m | 2.26 m | ~1,300 kg (varies) |
| 8 ft | 2.44 m | 2.20 m | 2.26 m | ~1,400 kg |
| 10 ft | 2.99 m | 2.44 m | 2.59 m | ~1,300 kg |
| 10 ft High Cube | 2.99 m | 2.44 m | 2.90 m | ~1,400 kg |
| 12 ft | 3.65 m | 2.44 m | 2.59 m | ~1,600 kg |
| 20 ft | 6.06 m | 2.44 m | 2.59 m | ~2,300 kg |
| 20 ft High Cube | 6.06 m | 2.44 m | 2.90 m | ~2,400 kg |
| 40 ft | 12.19 m | 2.44 m | 2.59 m | ~3,700 kg |
| 40 ft High Cube | 12.19 m | 2.44 m | 2.90 m | ~3,900 kg |

**Notes**
- Doppeltür / Open-Side / Garagencontainer share the external dimensions of their base size;
  the difference is the door configuration.
- Internal dimensions and door openings are slightly smaller — provide if you want them shown.
- Weights above are approximate tare weights and vary by build and condition; confirm before
  publishing, since weight can affect shipping calculation.

Once you confirm (or send corrected figures), I will write dimensions + weight to all products
and regenerate the feed with `shipping_weight` and product `Abmessungen` attributes.
