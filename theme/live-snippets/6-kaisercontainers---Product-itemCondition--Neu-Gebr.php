<?php
/* Adds schema.org itemCondition to WooCommerce and Rank Math product structured data, derived from the Gebrauchtcontainer category / Zustand attribute. Required for Merchant Center condition consistency. */
function kc_product_condition_url( $product ) {
	$used  = false;
	$slugs = wp_get_post_terms( $product->get_id(), 'product_cat', array( 'fields' => 'slugs' ) );
	if ( is_array( $slugs ) && in_array( 'gebrauchtcontainer', $slugs, true ) ) { $used = true; }
	$attr = $product->get_attribute( 'Zustand' );
	if ( $attr && stripos( $attr, 'gebraucht' ) !== false ) { $used = true; }
	if ( stripos( $product->get_name(), 'gebraucht' ) !== false ) { $used = true; }
	return $used ? 'https://schema.org/UsedCondition' : 'https://schema.org/NewCondition';
}

add_filter( 'woocommerce_structured_data_product', function ( $markup, $product ) {
	if ( ! is_object( $product ) || ! method_exists( $product, 'get_id' ) ) { return $markup; }
	$cond = kc_product_condition_url( $product );
	$markup['itemCondition'] = $cond;
	if ( isset( $markup['offers'] ) && is_array( $markup['offers'] ) ) {
		foreach ( $markup['offers'] as $i => $offer ) {
			if ( is_array( $offer ) ) { $markup['offers'][ $i ]['itemCondition'] = $cond; }
		}
	}
	return $markup;
}, 20, 2 );

add_filter( 'rank_math/snippet/rich_snippet_product_entity', function ( $entity ) {
	if ( ! function_exists( 'wc_get_product' ) ) { return $entity; }
	$product = wc_get_product( get_the_ID() );
	if ( ! $product ) { return $entity; }
	$cond = kc_product_condition_url( $product );
	$entity['itemCondition'] = $cond;
	if ( isset( $entity['offers'] ) && is_array( $entity['offers'] ) ) {
		if ( isset( $entity['offers']['@type'] ) ) {
			$entity['offers']['itemCondition'] = $cond;
		} else {
			foreach ( $entity['offers'] as $i => $offer ) {
				if ( is_array( $offer ) ) { $entity['offers'][ $i ]['itemCondition'] = $cond; }
			}
		}
	}
	return $entity;
}, 20 );