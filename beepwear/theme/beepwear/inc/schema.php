<?php
/**
 * JSON-LD structured data (fallback when no SEO plugin emits schema).
 *
 * Set BEEPWEAR_EMIT_SCHEMA to false once Rank Math owns schema in production
 * (see docs/PLUGINS.md — schema de-duplication decision).
 *
 * @package BeepWear
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! defined( 'BEEPWEAR_EMIT_SCHEMA' ) ) {
	define( 'BEEPWEAR_EMIT_SCHEMA', true );
}

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
				'logo'  => get_stylesheet_directory_uri() . '/assets/images/beepwear-mark.svg',
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
