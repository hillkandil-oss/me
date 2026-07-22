<?php
/**
 * BeepWear child theme — bootstrap.
 *
 * Loads modular includes from /inc. Keep this file thin; feature code lives in
 * its own module for maintainability (WordPress Coding Standards).
 *
 * @package BeepWear
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit; // No direct access.
}

define( 'BEEPWEAR_VERSION', '0.8.0' );
define( 'BEEPWEAR_DIR', get_stylesheet_directory() );

/**
 * Load a module from /inc.
 *
 * @param string $module File name without extension.
 */
function beepwear_require( $module ) {
	$path = BEEPWEAR_DIR . '/inc/' . $module . '.php';
	if ( is_readable( $path ) ) {
		require_once $path;
	}
}

array_map(
	'beepwear_require',
	array(
		'setup',            // Theme supports + WooCommerce declaration.
		'enqueue',          // Styles, script, font preload.
		'announcement-bar', // Admin-configurable announcement bar.
		'woocommerce',      // Storefront presentation tweaks.
		'schema',           // JSON-LD structured data (fallback).
	)
);
