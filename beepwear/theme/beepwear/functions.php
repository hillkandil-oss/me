<?php
/**
 * BeepWear child theme functions.
 *
 * Implements the BeepWear design system, WooCommerce support, JSON-LD
 * structured data, and small performance/accessibility helpers.
 *
 * @package BeepWear
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit; // No direct access.
}

define( 'BEEPWEAR_VERSION', '0.1.0' );

/**
 * Enqueue parent + child styles and the front-end script.
 */
function beepwear_enqueue_assets() {
	// Hello Elementor parent stylesheet.
	wp_enqueue_style(
		'hello-elementor',
		get_template_directory_uri() . '/style.css',
		array(),
		BEEPWEAR_VERSION
	);

	// BeepWear design system.
	wp_enqueue_style(
		'beepwear',
		get_stylesheet_uri(),
		array( 'hello-elementor' ),
		BEEPWEAR_VERSION
	);

	wp_enqueue_script(
		'beepwear',
		get_stylesheet_directory_uri() . '/assets/js/beepwear.js',
		array(),
		BEEPWEAR_VERSION,
		true
	);
}
add_action( 'wp_enqueue_scripts', 'beepwear_enqueue_assets', 20 );

/**
 * Preload self-hosted fonts to avoid a flash of fallback type.
 */
function beepwear_preload_fonts() {
	$base = get_stylesheet_directory_uri() . '/assets/fonts/';
	foreach ( array( 'cormorant-garamond.woff2', 'jost.woff2' ) as $font ) {
		printf(
			'<link rel="preload" href="%s" as="font" type="font/woff2" crossorigin>' . "\n",
			esc_url( $base . $font )
		);
	}
}
add_action( 'wp_head', 'beepwear_preload_fonts', 1 );

/**
 * Theme supports. WooCommerce declared here; product gallery features enabled.
 */
function beepwear_theme_supports() {
	add_theme_support( 'woocommerce' );
	add_theme_support( 'wc-product-gallery-zoom' );
	add_theme_support( 'wc-product-gallery-lightbox' );
	add_theme_support( 'wc-product-gallery-slider' );
	add_theme_support( 'title-tag' );
	add_theme_support( 'html5', array( 'search-form', 'gallery', 'caption', 'style', 'script' ) );
}
add_action( 'after_setup_theme', 'beepwear_theme_supports' );

/**
 * Products per row / per page for the luxury grid (roomy).
 */
add_filter( 'loop_shop_columns', function () { return 3; }, 20 );
add_filter( 'loop_shop_per_page', function () { return 12; }, 20 );

/**
 * Add the BeepWear reveal class to WooCommerce loop items so they fade in.
 */
add_filter( 'woocommerce_post_class', function ( $classes ) {
	$classes[] = 'bw-reveal';
	return $classes;
} );

/* ------------------------------------------------------------------ *
 *  Structured data (JSON-LD) — Organization, WebSite, and Product.
 *  Only emitted when no dedicated SEO plugin already outputs schema.
 *  Set BEEPWEAR_EMIT_SCHEMA to false if Rank Math / Yoast handles it.
 * ------------------------------------------------------------------ */
if ( ! defined( 'BEEPWEAR_EMIT_SCHEMA' ) ) {
	define( 'BEEPWEAR_EMIT_SCHEMA', true );
}

/**
 * Organization + WebSite schema on the front page.
 */
function beepwear_org_schema() {
	if ( ! BEEPWEAR_EMIT_SCHEMA || ! is_front_page() ) {
		return;
	}
	$data = array(
		'@context' => 'https://schema.org',
		'@graph'   => array(
			array(
				'@type' => 'Organization',
				'@id'   => home_url( '/#organization' ),
				'name'  => 'BeepWear',
				'url'   => home_url( '/' ),
				'logo'  => get_stylesheet_directory_uri() . '/assets/images/beepwear-logo.png',
			),
			array(
				'@type'           => 'WebSite',
				'@id'             => home_url( '/#website' ),
				'url'             => home_url( '/' ),
				'name'            => 'BeepWear',
				'publisher'       => array( '@id' => home_url( '/#organization' ) ),
				'potentialAction' => array(
					'@type'       => 'SearchAction',
					'target'      => home_url( '/?s={search_term_string}' ),
					'query-input' => 'required name=search_term_string',
				),
			),
		),
	);
	beepwear_print_jsonld( $data );
}
add_action( 'wp_head', 'beepwear_org_schema' );

/**
 * Product schema on single product pages (guarded for WooCommerce).
 */
function beepwear_product_schema() {
	if ( ! BEEPWEAR_EMIT_SCHEMA || ! function_exists( 'is_product' ) || ! is_product() ) {
		return;
	}
	global $product;
	if ( ! $product instanceof WC_Product ) {
		return;
	}
	$data = array(
		'@context'    => 'https://schema.org',
		'@type'       => 'Product',
		'name'        => $product->get_name(),
		'sku'         => $product->get_sku(),
		'description' => wp_strip_all_tags( $product->get_short_description() ?: $product->get_description() ),
		'image'       => wp_get_attachment_image_url( $product->get_image_id(), 'large' ),
		'offers'      => array(
			'@type'         => 'Offer',
			'price'         => $product->get_price(),
			'priceCurrency' => get_woocommerce_currency(),
			'availability'  => $product->is_in_stock()
				? 'https://schema.org/InStock'
				: 'https://schema.org/OutOfStock',
			'url'           => get_permalink( $product->get_id() ),
		),
	);
	beepwear_print_jsonld( $data );
}
add_action( 'wp_head', 'beepwear_product_schema' );

/**
 * Print a JSON-LD block safely.
 *
 * @param array $data Structured-data array.
 */
function beepwear_print_jsonld( $data ) {
	echo '<script type="application/ld+json">'
		. wp_json_encode( $data, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE )
		. '</script>' . "\n";
}
