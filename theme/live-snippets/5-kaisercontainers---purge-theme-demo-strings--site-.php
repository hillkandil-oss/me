<?php
/* Replaces all Tranzix demo-content strings in the rendered HTML: the fabricated address 'House 35 R/A, Street', the Cyprus phone, dead tel:/mailto: links, placeholder names/emails, and English demo UI labels. Runs on the output buffer so the raw HTML served to crawlers is clean, not merely hidden with CSS. */
add_action( 'template_redirect', function () {
	if ( is_admin() ) { return; }
	ob_start( function ( $html ) {
		if ( ! is_string( $html ) || $html === '' ) { return $html; }
		$map = array(
			// fabricated contact data shipped with the theme demo
			'House 35 R/A,Street'  => 'Homberg/Ruhrort/Baerl, 47138 Duisburg',
			'House 35 R/A, Street' => 'Homberg/Ruhrort/Baerl, 47138 Duisburg',
			'House 35 R/A'         => 'Homberg/Ruhrort/Baerl',
			'+357 984538'          => '+49 201 49869542',
			'tel:#'                => 'tel:+4920149869542',
			'mailto:#'             => 'mailto:info@kaisercontainers.de',
			'name@beispiel.de'     => 'ihre.adresse@example.com',
			'Max Mustermann'       => 'Ihr vollstaendiger Name',
			'Mustermann'           => '',
			// English demo UI strings on a German storefront
			'Sing Up'              => 'Jetzt einkaufen',
			'sing up'              => 'jetzt einkaufen',
			'Sign Up'              => 'Jetzt einkaufen',
			'Our Address'          => 'Adresse',
			'our address'          => 'Adresse',
			'Call Us'              => 'Rufen Sie uns an',
			'call us'              => 'Rufen Sie uns an',
			'e-mail us'            => 'E-Mail',
			'E-mail Us'            => 'E-Mail',
		);
		$hit = false;
		foreach ( $map as $needle => $repl ) {
			if ( strpos( $html, $needle ) !== false ) { $hit = true; break; }
		}
		if ( ! $hit ) { return $html; }
		return str_replace( array_keys( $map ), array_values( $map ), $html );
	} );
}, 1 );