<?php
/**
 * Theme setup: supports and WooCommerce declaration.
 *
 * @package BeepWear
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Theme supports. WooCommerce and product-gallery features enabled.
 */
function beepwear_theme_supports() {
	add_theme_support( 'woocommerce' );
	add_theme_support( 'wc-product-gallery-zoom' );
	add_theme_support( 'wc-product-gallery-lightbox' );
	add_theme_support( 'wc-product-gallery-slider' );
	add_theme_support( 'title-tag' );
	add_theme_support( 'html5', array( 'search-form', 'gallery', 'caption', 'style', 'script' ) );
	add_theme_support( 'custom-logo' );
	register_nav_menus(
		array(
			'primary' => __( 'Primary Menu', 'beepwear' ),
			'footer'  => __( 'Footer Menu', 'beepwear' ),
		)
	);
}
add_action( 'after_setup_theme', 'beepwear_theme_supports' );
