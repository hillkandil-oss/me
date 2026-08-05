<?php
/* Appends the legally required shipping-cost note (PAngV) to catalog and product prices. WooCommerce's built-in price suffix only renders when tax calculation is enabled, which it is not here. */
add_filter( 'woocommerce_get_price_html', function ( $price_html, $product ) {
	if ( is_admin() && ! wp_doing_ajax() ) { return $price_html; }
	if ( strpos( $price_html, 'kc-price-note' ) !== false ) { return $price_html; }
	$note = ' <small class="kc-price-note">zzgl. <a href="/versand/">Versandkosten</a></small>';
	return $price_html . $note;
}, 20, 2 );