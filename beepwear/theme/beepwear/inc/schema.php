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
				'@type'        => 'Organization',
				'@id'          => home_url( '/#organization' ),
				'name'         => 'BeepWear',
				'url'          => home_url( '/' ),
				'logo'         => get_stylesheet_directory_uri() . '/assets/images/beepwear-mark.svg',
				'email'        => 'info@beepwear.com',
				'telephone'    => '+1-605-361-9867',
				'address'      => array(
					'@type'           => 'PostalAddress',
					'streetAddress'   => '510 Main St',
					'addressLocality' => 'Wall',
					'addressRegion'   => 'SD',
					'postalCode'      => '57790',
					'addressCountry'  => 'US',
				),
				'contactPoint' => array(
					'@type'       => 'ContactPoint',
					'contactType' => 'customer service',
					'email'       => 'info@beepwear.com',
					'telephone'   => '+1-605-361-9867',
				),
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
		'itemCondition' => 'https://schema.org/UsedCondition',
		'offers'      => array(
			'@type'         => 'Offer',
			'price'         => $product->get_price(),
			'priceCurrency' => get_woocommerce_currency(),
			'itemCondition' => 'https://schema.org/UsedCondition',
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
 * Declare "used" condition on Rank Math's Product rich snippet.
 *
 * Rank Math owns the authoritative Product schema in production, but does not
 * emit itemCondition. Every BeepWear timepiece is pre-owned, so we add it here
 * (both on the Product entity and its Offer) to match the product feed's
 * condition:used and keep Merchant Center's page↔feed comparison clean.
 *
 * @param array $entity Rank Math product schema entity.
 * @return array
 */
function beepwear_rankmath_product_condition( $entity ) {
	if ( ! is_array( $entity ) ) {
		return $entity;
	}
	$used = 'https://schema.org/UsedCondition';
	if ( empty( $entity['itemCondition'] ) ) {
		$entity['itemCondition'] = $used;
	}
	if ( isset( $entity['offers'] ) && is_array( $entity['offers'] ) ) {
		// Offers may be a single Offer or a list.
		if ( isset( $entity['offers']['@type'] ) ) {
			$entity['offers']['itemCondition'] = $used;
		} else {
			foreach ( $entity['offers'] as $k => $offer ) {
				if ( is_array( $offer ) ) {
					$entity['offers'][ $k ]['itemCondition'] = $used;
				}
			}
		}
	}
	return $entity;
}
add_filter( 'rank_math/snippet/rich_snippet_product_entity', 'beepwear_rankmath_product_condition' );
