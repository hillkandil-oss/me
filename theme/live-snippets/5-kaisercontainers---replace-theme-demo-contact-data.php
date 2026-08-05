<?php
/* Replaces the Tranzix theme's hardcoded demo phone (+357 984538) and dead tel:#/mailto:# links in the rendered HTML with the real business contact details. Prevents fabricated contact data appearing in the page source. */
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