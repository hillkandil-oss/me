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
 * Homepage SEO meta (description, canonical, Open Graph, Twitter).
 *
 * Rank Math does not emit these on a "latest posts" front page, so the theme
 * fills the gap. Guarded to the front page and skipped if an SEO plugin has
 * already printed a description this request (avoids duplicates).
 */
function beepwear_front_meta() {
	if ( ! is_front_page() ) {
		return;
	}
	// If Rank Math (or another SEO plugin) is emitting front-page meta, defer to it.
	if ( function_exists( 'rank_math' ) && apply_filters( 'rank_math/frontend/description', false ) ) {
		return;
	}
	$desc  = 'Shop an expertly curated collection of luxury and pre-owned watches at BeepWear — authentic timepieces, honest descriptions, secure checkout, and dedicated support.';
	$url   = home_url( '/' );
	$title = get_bloginfo( 'name' ) . ' — ' . get_bloginfo( 'description' );
	// Social unfurlers (Facebook, LinkedIn, X) and most AI crawlers do not render
	// SVG. Use a real 1200x630 raster share image.
	$image = beepwear_share_image();

	printf( '<meta name="description" content="%s">' . "\n", esc_attr( $desc ) );
	printf( '<link rel="canonical" href="%s">' . "\n", esc_url( $url ) );
	printf( '<meta property="og:type" content="website">' . "\n" );
	printf( '<meta property="og:site_name" content="%s">' . "\n", esc_attr( get_bloginfo( 'name' ) ) );
	printf( '<meta property="og:title" content="%s">' . "\n", esc_attr( $title ) );
	printf( '<meta property="og:description" content="%s">' . "\n", esc_attr( $desc ) );
	printf( '<meta property="og:url" content="%s">' . "\n", esc_url( $url ) );
	printf( '<meta property="og:image" content="%s">' . "\n", esc_url( $image ) );
	printf( '<meta property="og:image:width" content="1200">' . "\n" );
	printf( '<meta property="og:image:height" content="630">' . "\n" );
	printf( '<meta name="twitter:card" content="summary_large_image">' . "\n" );
	printf( '<meta name="twitter:title" content="%s">' . "\n", esc_attr( $title ) );
	printf( '<meta name="twitter:description" content="%s">' . "\n", esc_attr( $desc ) );
	printf( '<meta name="twitter:image" content="%s">' . "\n", esc_url( $image ) );
}

/**
 * Resolve the default 1200x630 raster social share image.
 *
 * Falls back to the vector mark only if the raster asset is absent, so the site
 * never emits a broken og:image reference.
 *
 * @return string Absolute URL to the share image.
 */
function beepwear_share_image() {
	$dir = get_stylesheet_directory();
	$uri = get_stylesheet_directory_uri();
	if ( is_readable( $dir . '/assets/images/og-default.png' ) ) {
		return $uri . '/assets/images/og-default.png';
	}
	return $uri . '/assets/images/beepwear-mark.svg';
}
add_action( 'wp_head', 'beepwear_front_meta', 2 );

/**
 * Organization + WebSite schema on the front page.
 */
function beepwear_org_schema() {
	if ( ! BEEPWEAR_EMIT_SCHEMA || ! is_front_page() ) {
		return;
	}
	$organization = array(
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
	);

	// Entity-disambiguation signal for Google's Knowledge Graph and AI answer
	// engines. Populate with REAL, verified profile URLs only — never fabricate.
	// Filter usage:
	//   add_filter( 'beepwear/organization_sameas', function () {
	//       return array( 'https://www.instagram.com/…', 'https://www.facebook.com/…' );
	//   } );
	$same_as = array_values( array_filter( array_map( 'esc_url_raw', (array) apply_filters( 'beepwear/organization_sameas', array() ) ) ) );
	if ( ! empty( $same_as ) ) {
		$organization['sameAs'] = $same_as;
	}

	$data = array(
		'@context' => 'https://schema.org',
		'@graph'   => array(
			$organization,
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
 * Declare "used" condition (and MPN) on Rank Math's Product rich snippet.
 *
 * Rank Math owns the authoritative Product schema in production. Every BeepWear
 * timepiece is pre-owned, so itemCondition must be UsedCondition to match the
 * product feed's condition:used and keep Merchant Center's page↔feed comparison
 * clean. The override is UNCONDITIONAL: some Rank Math versions default
 * itemCondition to NewCondition, so an "only if empty" guard would silently
 * leave the wrong value in place.
 *
 * @param array $entity Rank Math product schema entity.
 * @return array
 */
function beepwear_rankmath_product_condition( $entity ) {
	if ( ! is_array( $entity ) ) {
		return $entity;
	}
	$used = 'https://schema.org/UsedCondition';

	$entity['itemCondition'] = $used;

	// Reference numbers are the manufacturer part number for watches; surface the
	// SKU as mpn when Rank Math has not already set an mpn/gtin.
	if ( empty( $entity['mpn'] ) && empty( $entity['gtin'] ) && function_exists( 'is_product' ) && is_product() ) {
		global $product;
		if ( $product instanceof WC_Product && $product->get_sku() ) {
			$entity['mpn'] = $product->get_sku();
		}
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

/**
 * Final safety net: force UsedCondition onto every Product/Offer node in the
 * assembled Rank Math JSON-LD graph.
 *
 * The per-entity filter above depends on Rank Math's product-entity hook firing
 * with the shape we expect. This pass runs on the fully-built graph
 * (`rank_math/json_ld`), so the condition lands even when the graph is composed
 * differently across Rank Math versions. Only touches product pages.
 *
 * @param array  $data    Assembled JSON-LD nodes, keyed by entity name.
 * @param object $jsonld  Rank Math JsonLD instance (unused).
 * @return array
 */
function beepwear_rankmath_force_used_condition( $data, $jsonld = null ) {
	if ( ! is_array( $data ) || ! function_exists( 'is_product' ) || ! is_product() ) {
		return $data;
	}
	$used = 'https://schema.org/UsedCondition';

	$apply = function ( &$node ) use ( $used, &$apply ) {
		if ( ! is_array( $node ) ) {
			return;
		}
		$type = isset( $node['@type'] ) ? (array) $node['@type'] : array();
		if ( in_array( 'Product', $type, true ) || in_array( 'Offer', $type, true ) ) {
			$node['itemCondition'] = $used;
		}
		foreach ( $node as $key => &$value ) {
			if ( is_array( $value ) ) {
				$apply( $value );
			}
		}
		unset( $value );
	};

	foreach ( $data as &$node ) {
		$apply( $node );
	}
	unset( $node );

	return $data;
}
add_filter( 'rank_math/json_ld', 'beepwear_rankmath_force_used_condition', 99, 2 );
