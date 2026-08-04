<?php
/**
 * kaisercontainers — LocalBusiness / Organization JSON-LD
 * Add to a CHILD theme's functions.php (never edit the parent theme directly),
 * or a code-snippets plugin. Fill the CONSTANTS with verified data before publishing.
 * Product schema: install an SEO plugin (Rank Math / Yoast WooCommerce SEO) to emit
 * Product + Offer + Breadcrumb schema automatically, or extend this file per product.
 */

add_action( 'wp_head', function () {

	// ---- Verified data — REPLACE before go-live -------------------------
	$phone   = '';                 // e.g. '+492031234567' (E.164). Leave '' to omit.
	$street  = '';                 // e.g. 'Musterstraße 1'
	$lat     = '';                 // e.g. '51.4700'
	$lng     = '';                 // e.g. '6.7100'
	$logo    = home_url( '/wp-content/uploads/kaisercontainers-logo.png' );
	$image   = '';                 // URL of a real store/yard photo
	$sameAs  = array();            // verified social profile URLs only
	// ---------------------------------------------------------------------

	$org = array(
		'@type'     => 'Organization',
		'@id'       => home_url( '/#organization' ),
		'name'      => 'kaisercontainers',
		'url'       => home_url( '/' ),
		'logo'      => $logo,
		'email'     => 'info@kaisercontainers.de',
		'sameAs'    => $sameAs,
	);
	if ( $phone ) { $org['telephone'] = $phone; }

	$store = array(
		'@type'              => 'Store',
		'@id'                => home_url( '/#localbusiness' ),
		'name'               => 'kaisercontainers',
		'url'                => home_url( '/' ),
		'email'              => 'info@kaisercontainers.de',
		'priceRange'         => '€€',
		'currenciesAccepted' => 'EUR',
		'paymentAccepted'    => 'Banküberweisung',
		'parentOrganization' => array( '@id' => home_url( '/#organization' ) ),
		'hasMap'             => 'https://maps.app.goo.gl/k4JZCaARe1ZPu5WUA',
		'areaServed'         => array( '@type' => 'Country', 'name' => 'Deutschland' ),
		'address'            => array(
			'@type'           => 'PostalAddress',
			'streetAddress'   => $street,
			'addressLocality' => 'Duisburg',
			'addressRegion'   => 'Nordrhein-Westfalen',
			'postalCode'      => '47138',
			'addressCountry'  => 'DE',
		),
		'openingHoursSpecification' => array( array(
			'@type'     => 'OpeningHoursSpecification',
			'dayOfWeek' => array( 'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday' ),
			'opens'     => '08:00',
			'closes'    => '18:30',
		) ),
	);
	if ( $phone ) { $store['telephone'] = $phone; }
	if ( $image ) { $store['image'] = $image; }
	if ( $lat && $lng ) {
		$store['geo'] = array( '@type' => 'GeoCoordinates', 'latitude' => $lat, 'longitude' => $lng );
	}

	$graph = array( '@context' => 'https://schema.org', '@graph' => array( $org, $store ) );

	echo "\n<script type=\"application/ld+json\">" .
		wp_json_encode( $graph, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) .
		"</script>\n";

}, 20 );
