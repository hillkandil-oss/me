<?php
/**
 * Asset loading: styles, script, and font preload.
 *
 * @package BeepWear
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Enqueue parent + child styles and the front-end script.
 */
function beepwear_enqueue_assets() {
	wp_enqueue_style(
		'hello-elementor',
		get_template_directory_uri() . '/style.css',
		array(),
		BEEPWEAR_VERSION
	);

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
