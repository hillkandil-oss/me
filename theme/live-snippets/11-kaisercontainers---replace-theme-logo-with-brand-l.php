<?php
/* Swaps the Tranzix demo logo image URL for the uploaded kaisercontainers wordmark in the rendered HTML. */
add_action( 'template_redirect', function () {
	if ( is_admin() ) { return; }
	ob_start( function ( $html ) {
		if ( ! is_string( $html ) || strpos( $html, 'themes/tranzix/assets/images/logo' ) === false ) { return $html; }
		$new = 'https://kaisercontainers.de/wp-content/uploads/2026/08/kaisercontainers-logo.svg';
		$html = preg_replace( '#https?://[^"\']*themes/tranzix/assets/images/logo[^"\']*#i', $new, $html );
		return $html;
	} );
}, 2 );