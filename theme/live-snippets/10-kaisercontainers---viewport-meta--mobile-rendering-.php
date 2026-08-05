<?php
/* The Tranzix theme does not output a viewport meta tag, so phones rendered the site at desktop width and scaled it down. This adds the standard responsive viewport tag. */
add_action( 'wp_head', function () {
	if ( is_admin() ) { return; }
	echo '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">' . "\n";
}, 1 );