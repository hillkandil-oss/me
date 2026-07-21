# /inc — modular includes

Feature modules loaded by `functions.php`. Keep `functions.php` thin; one concern per file.

- `setup.php` — theme supports + WooCommerce declaration
- `enqueue.php` — styles, script, font preload
- `woocommerce.php` — storefront presentation tweaks (grid, per-page, reveal class)
- `schema.php` — JSON-LD (fallback; disable when Rank Math owns schema)
