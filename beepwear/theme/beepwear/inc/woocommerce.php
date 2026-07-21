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
