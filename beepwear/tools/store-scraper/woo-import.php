<?php
/**
 * woo-import.php — Drop-in WooCommerce product importer.
 *
 * Use this when the built-in Products → Import screen fails with
 * "File path provided for import is invalid" (a host temp-upload problem).
 * This reads a CSV already on the server and creates products via WooCommerce's
 * own API, so no browser upload / temp file is involved.
 *
 * ─── HOW TO USE ────────────────────────────────────────────────────────────
 * 1. Edit the SECRET_TOKEN below to any private value (e.g. a long random word).
 * 2. Upload BOTH files into your site root (the folder with wp-load.php) using
 *    your host's File Manager:
 *        - this file:  woo-import.php
 *        - the data:   containersolutionscs-mc-import.csv
 * 3. In your browser open:
 *        https://YOUR-STORE.com/woo-import.php?token=YOUR_SECRET
 *    It imports in batches of 20 and shows a "continue" link after each batch —
 *    keep clicking it until it says "ALL DONE".
 * 4. IMPORTANT: DELETE woo-import.php (and the CSV) from the server afterwards.
 *
 * Options (add to the URL):
 *    &images=0   skip image import (much faster; add images later)
 *    &file=name.csv   use a different CSV filename
 *    &limit=10   change batch size
 * ───────────────────────────────────────────────────────────────────────────
 */

// ===== EDIT THIS =====
const SECRET_TOKEN = 'change-me-to-something-private';
// =====================

const DEFAULT_CSV   = 'containersolutionscs-mc-import.csv';
const BATCH_DEFAULT = 20;

// --- Guards -----------------------------------------------------------------
if (!isset($_GET['token']) || !hash_equals(SECRET_TOKEN, (string) $_GET['token'])) {
    http_response_code(403);
    exit('Forbidden: missing or wrong token.');
}

// Boot WordPress.
$wp_load = __DIR__ . '/wp-load.php';
if (!file_exists($wp_load)) {
    exit('wp-load.php not found. Put this file in your WordPress root folder.');
}
require_once $wp_load;

if (!current_user_can('manage_woocommerce') && !defined('WOO_IMPORT_ALLOW_TOKEN_ONLY')) {
    // Token alone is allowed, but warn: prefer being logged in as an admin too.
}
if (!class_exists('WC_Product_Simple')) {
    exit('WooCommerce is not active on this site.');
}

require_once ABSPATH . 'wp-admin/includes/media.php';
require_once ABSPATH . 'wp-admin/includes/file.php';
require_once ABSPATH . 'wp-admin/includes/image.php';

header('Content-Type: text/html; charset=utf-8');
echo "<pre style='font:14px/1.5 monospace;padding:16px'>";

$csv_name = isset($_GET['file']) ? basename($_GET['file']) : DEFAULT_CSV;
$csv_path = __DIR__ . '/' . $csv_name;
if (!file_exists($csv_path)) {
    exit("CSV not found: $csv_name (upload it next to this script).\n");
}

$do_images = !isset($_GET['images']) || $_GET['images'] !== '0';
$offset    = isset($_GET['offset']) ? max(0, (int) $_GET['offset']) : 0;
$limit     = isset($_GET['limit'])  ? max(1, (int) $_GET['limit'])  : BATCH_DEFAULT;

// --- Read CSV ---------------------------------------------------------------
$rows = [];
if (($fh = fopen($csv_path, 'r')) !== false) {
    $header = fgetcsv($fh);
    while (($data = fgetcsv($fh)) !== false) {
        if (count(array_filter($data, fn($c) => $c !== '')) === 0) continue;
        $rows[] = array_combine($header, array_pad($data, count($header), ''));
    }
    fclose($fh);
}
$total = count($rows);
echo "CSV: $csv_name — $total products. Batch: $offset.." . min($total, $offset + $limit)
   . " (images: " . ($do_images ? "on" : "off") . ")\n\n";

// --- Helpers ----------------------------------------------------------------
function term_id_for(string $name, string $taxonomy): int {
    $name = trim($name);
    if ($name === '') return 0;
    $term = term_exists($name, $taxonomy);
    if (!$term) $term = wp_insert_term($name, $taxonomy);
    if (is_wp_error($term)) return 0;
    return (int) ($term['term_id'] ?? 0);
}

function attach_images(WC_Product $product, array $urls): void {
    $ids = [];
    foreach ($urls as $url) {
        $url = trim($url);
        if ($url === '') continue;
        $id = media_sideload_image($url, $product->get_id(), null, 'id');
        if (!is_wp_error($id)) $ids[] = (int) $id;
    }
    if ($ids) {
        $product->set_image_id(array_shift($ids));
        if ($ids) $product->set_gallery_image_ids($ids);
    }
}

// --- Import batch -----------------------------------------------------------
$created = $updated = $failed = 0;
$slice = array_slice($rows, $offset, $limit);
foreach ($slice as $i => $r) {
    $n = $offset + $i + 1;
    $name = trim($r['Name'] ?? '');
    if ($name === '') { continue; }
    $sku  = trim($r['SKU'] ?? '');

    try {
        $id = $sku !== '' ? wc_get_product_id_by_sku($sku) : 0;
        $product = $id ? wc_get_product($id) : new WC_Product_Simple();

        $product->set_name($name);
        $product->set_status('publish');
        $product->set_description((string) ($r['Description'] ?? ''));
        $product->set_short_description((string) ($r['Short description'] ?? ''));
        if ($sku !== '') $product->set_sku($sku);

        $regular = trim((string) ($r['Regular price'] ?? ''));
        $sale    = trim((string) ($r['Sale price'] ?? ''));
        if ($regular !== '') $product->set_regular_price($regular);
        if ($sale !== '')    $product->set_sale_price($sale);

        $in_stock = (string) ($r['In stock?'] ?? '1');
        $product->set_stock_status($in_stock === '0' ? 'outofstock' : 'instock');

        // Categories
        $cat_ids = [];
        foreach (explode(',', (string) ($r['Categories'] ?? '')) as $c) {
            $tid = term_id_for($c, 'product_cat');
            if ($tid) $cat_ids[] = $tid;
        }
        if ($cat_ids) $product->set_category_ids($cat_ids);

        $product->save();

        // Brand — native WooCommerce Brands taxonomy (WC 9.6+), if present.
        $brand = trim((string) ($r['Brands'] ?? ''));
        if ($brand !== '' && taxonomy_exists('product_brand')) {
            $tid = term_id_for($brand, 'product_brand');
            if ($tid) wp_set_object_terms($product->get_id(), [$tid], 'product_brand');
        }

        // Images (only for freshly created products, unless forced)
        if ($do_images && !$id) {
            $imgs = array_filter(array_map('trim', explode(',', (string) ($r['Images'] ?? ''))));
            if ($imgs) { attach_images($product, $imgs); $product->save(); }
        }

        if ($id) { $updated++; $tag = 'updated'; } else { $created++; $tag = 'created'; }
        echo sprintf("[%3d/%3d] %-8s %s\n", $n, $total, $tag, mb_substr($name, 0, 60));
    } catch (Throwable $e) {
        $failed++;
        echo sprintf("[%3d/%3d] FAILED   %s — %s\n", $n, $total, mb_substr($name, 0, 45), $e->getMessage());
    }
    flush();
}

echo "\nBatch done: created=$created updated=$updated failed=$failed\n";

$next = $offset + $limit;
if ($next < $total) {
    $q = http_build_query([
        'token'  => $_GET['token'], 'offset' => $next, 'limit' => $limit,
        'images' => $do_images ? '1' : '0', 'file' => $csv_name,
    ]);
    $url = htmlspecialchars(strtok($_SERVER['REQUEST_URI'], '?') . '?' . $q);
    echo "\n>>> CONTINUE: <a href=\"$url\">import next $limit products ($next.." . min($total, $next + $limit) . ")</a>\n";
} else {
    echo "\n✅ ALL DONE — $total products processed. Now DELETE woo-import.php and the CSV from the server.\n";
}
echo "</pre>";
