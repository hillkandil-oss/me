<?php
/**
 * WooCommerce presentation tweaks for the luxury storefront.
 *
 * @package BeepWear
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Roomy grid: three products per row.
 */
add_filter( 'loop_shop_columns', function () {
	return 3;
}, 20 );

/**
 * Products per archive page.
 */
add_filter( 'loop_shop_per_page', function () {
	return 12;
}, 20 );

/**
 * Add the reveal class to loop items so they fade in on scroll.
 *
 * @param string[] $classes Existing post classes.
 * @return string[]
 */
add_filter( 'woocommerce_post_class', function ( $classes ) {
	$classes[] = 'bw-reveal';
	return $classes;
} );

/**
 * Buying-guide internal links shown beneath category and brand archives.
 *
 * Attacks the "thin grid-only" archive problem and the internal-linking gap: even
 * before per-term intro copy is written, every category/brand page gains unique,
 * genuinely useful content and cross-links to the editorial guides (which also
 * strengthens topical authority and AI citability). Links are real, live URLs;
 * override via the `beepwear/archive_guide_links` filter.
 *
 * @return array<string,string> label => path
 */
function beepwear_archive_guide_links() {
	return (array) apply_filters(
		'beepwear/archive_guide_links',
		array(
			'Luxury Watch Buying Guide' => '/luxury-watch-buying-guide/',
			'Automatic vs Quartz'       => '/automatic-vs-quartz/',
			'Watch Materials Guide'     => '/watch-materials-guide/',
			'Watch Care Guide'          => '/watch-care-guide/',
			'Authenticity Guarantee'    => '/authenticity-guarantee/',
		)
	);
}

/**
 * Render the guide-links block once, after the products grid on taxonomy archives.
 */
function beepwear_render_archive_guides() {
	static $done = false;
	if ( $done || ! function_exists( 'is_product_taxonomy' ) || ! is_product_taxonomy() ) {
		return;
	}
	$links = beepwear_archive_guide_links();
	if ( empty( $links ) ) {
		return;
	}
	$done = true;

	echo '<section class="bw-archive-guides" aria-label="' . esc_attr__( 'Watch buying guides', 'beepwear' ) . '">';
	echo '<h2 class="bw-archive-guides__title">' . esc_html__( 'New to collecting? Start with our guides', 'beepwear' ) . '</h2>';
	echo '<ul class="bw-archive-guides__list">';
	foreach ( $links as $label => $path ) {
		printf(
			'<li><a href="%s">%s</a></li>',
			esc_url( home_url( $path ) ),
			esc_html( $label )
		);
	}
	echo '</ul></section>';
}
add_action( 'woocommerce_after_shop_loop', 'beepwear_render_archive_guides', 30 );
