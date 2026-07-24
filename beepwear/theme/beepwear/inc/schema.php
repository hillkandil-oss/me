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
	// Social cards must use a raster image at 1200x630 — an SVG does not render
	// as an og:image/twitter:image on Facebook, X, LinkedIn, iMessage or Slack.
	$image = get_stylesheet_directory_uri() . '/assets/images/beepwear-share.png';

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
add_action( 'wp_head', 'beepwear_front_meta', 2 );

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
				'logo'         => array(
					'@type'  => 'ImageObject',
					'url'    => get_stylesheet_directory_uri() . '/assets/images/beepwear-logo.png',
					'width'  => 512,
					'height' => 512,
				),
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

/**
 * Journal (blog post) structured data: BlogPosting + optional FAQPage / HowTo.
 *
 * Rank Math is intended to own article/FAQ schema in production; this is the
 * theme fallback so journal guides are never left without structured data
 * (Article, FAQ and HowTo are prime rich-result and AI-citation surfaces).
 * Dates and titles come from the live post — nothing is fabricated. FAQ/HowTo
 * copy comes from inc/journal-schema-data.php, mirrored from the guide bodies.
 *
 * Set BEEPWEAR_EMIT_SCHEMA = false once Rank Math emits these blocks to avoid
 * duplicate schema.
 */
function beepwear_journal_schema() {
	if ( ! BEEPWEAR_EMIT_SCHEMA || ! is_singular( 'post' ) ) {
		return;
	}

	$post_id   = get_queried_object_id();
	$permalink = get_permalink( $post_id );
	$image     = get_the_post_thumbnail_url( $post_id, 'large' );
	if ( ! $image ) {
		$image = get_stylesheet_directory_uri() . '/assets/images/beepwear-share.png';
	}
	$excerpt = has_excerpt( $post_id )
		? get_the_excerpt( $post_id )
		: wp_trim_words( wp_strip_all_tags( get_post_field( 'post_content', $post_id ) ), 40 );

	$graph = array();

	// BlogPosting — always emitted for single posts.
	$graph[] = array(
		'@type'            => 'BlogPosting',
		'@id'              => $permalink . '#article',
		'headline'         => get_the_title( $post_id ),
		'description'      => $excerpt,
		'image'            => $image,
		'datePublished'    => get_the_date( DATE_W3C, $post_id ),
		'dateModified'     => get_the_modified_date( DATE_W3C, $post_id ),
		'author'           => array(
			'@type' => 'Organization',
			'name'  => 'BeepWear Editorial Team',
			'url'   => home_url( '/about/' ),
		),
		'publisher'        => array(
			'@type' => 'Organization',
			'name'  => 'BeepWear',
			'logo'  => array(
				'@type'  => 'ImageObject',
				'url'    => get_stylesheet_directory_uri() . '/assets/images/beepwear-logo.png',
				'width'  => 512,
				'height' => 512,
			),
		),
		'mainEntityOfPage' => $permalink,
	);

	// Per-guide FAQ / HowTo, matched by slug.
	$slug = get_post_field( 'post_name', $post_id );
	$data = function_exists( 'beepwear_journal_schema_data' ) ? beepwear_journal_schema_data() : array();

	if ( isset( $data[ $slug ]['faq'] ) && is_array( $data[ $slug ]['faq'] ) ) {
		$questions = array();
		foreach ( $data[ $slug ]['faq'] as $qa ) {
			$questions[] = array(
				'@type'          => 'Question',
				'name'           => $qa['q'],
				'acceptedAnswer' => array(
					'@type' => 'Answer',
					'text'  => $qa['a'],
				),
			);
		}
		if ( $questions ) {
			$graph[] = array(
				'@type'      => 'FAQPage',
				'@id'        => $permalink . '#faq',
				'mainEntity' => $questions,
			);
		}
	}

	if ( isset( $data[ $slug ]['howto'] ) && is_array( $data[ $slug ]['howto'] ) ) {
		$steps = array();
		$pos   = 1;
		foreach ( $data[ $slug ]['howto']['steps'] as $step ) {
			$steps[] = array(
				'@type'    => 'HowToStep',
				'position' => $pos++,
				'name'     => $step[0],
				'text'     => $step[1],
			);
		}
		if ( $steps ) {
			$graph[] = array(
				'@type' => 'HowTo',
				'@id'   => $permalink . '#howto',
				'name'  => $data[ $slug ]['howto']['name'],
				'step'  => $steps,
			);
		}
	}

	beepwear_print_jsonld(
		array(
			'@context' => 'https://schema.org',
			'@graph'   => $graph,
		)
	);
}
add_action( 'wp_head', 'beepwear_journal_schema' );
