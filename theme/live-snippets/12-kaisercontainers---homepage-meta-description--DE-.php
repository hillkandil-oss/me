<?php
/* Outputs a German meta description and og:description on the front page, and suppresses the SEO plugin's duplicate. */
add_action( 'wp_head', function () {
	if ( ! is_front_page() && ! is_home() ) { return; }
	$desc = 'Container kaufen in Duisburg: neue und gebrauchte See-, Lager- und Garagencontainer '
		. 'von 6 bis 40 Fuss. Online bestellen, deutschlandweit liefern lassen oder nach Absprache abholen.';
	echo '<meta name="description" content="' . esc_attr( $desc ) . '">' . "\n";
	echo '<meta property="og:description" content="' . esc_attr( $desc ) . '">' . "\n";
}, 3 );

// Do not let the SEO plugin emit a second description tag on the front page
add_filter( 'rank_math/frontend/description', function ( $d ) {
	return is_front_page() ? false : $d;
}, 20 );