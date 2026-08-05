<?php
/**
 * kaisercontainers — replace the Tranzix theme's hardcoded demo contact data.
 *
 * The theme header hardcodes a fabricated phone (+357 984538, Cyprus) and dead
 * tel:# / mailto:# links. They cannot be edited through any API and the owner does
 * not edit theme files, so this filters the rendered HTML instead and swaps in the
 * real business details. Fabricated contact data is a Merchant Center
 * misrepresentation risk even when hidden with CSS.
 *
 * INSTALLED LIVE via the Code Snippets plugin (snippet id 5, scope: front-end).
 * Kept here as the source of truth.
 */
add_action( 'template_redirect', function () {
	if ( is_admin() ) { return; }
	ob_start( function ( $html ) {
		if ( ! is_string( $html ) || $html === '' ) { return $html; }
		if ( strpos( $html, '984538' ) === false && strpos( $html, 'tel:#' ) === false && strpos( $html, 'mailto:#' ) === false ) {
			return $html;
		}
		$html = str_replace( '+357 984538', '+49 201 49869542', $html );
		$html = str_replace( 'tel:#', 'tel:+4920149869542', $html );
		$html = str_replace( 'mailto:#', 'mailto:info@kaisercontainers.de', $html );
		return $html;
	} );
}, 1 );
