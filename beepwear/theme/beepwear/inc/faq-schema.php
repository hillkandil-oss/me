<?php
/**
 * FAQPage JSON-LD for the support FAQ page.
 *
 * Rich-result eligibility + a strong passage-citation signal for AI answer
 * engines (GEO). Seeded from content/faq.md with the ANSWER TEXT KEPT TRUTHFUL.
 *
 * Safety rails:
 * - Any answer still containing a "[confirm" placeholder is skipped, so unverified
 *   facts (shipping/refund windows, support hours) never leak into structured data.
 * - Emission is filterable and can be turned off if Rank Math's FAQ block already
 *   owns FAQPage schema on this page (avoid duplicate FAQPage entities).
 *
 * @package BeepWear
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! defined( 'BEEPWEAR_EMIT_FAQ' ) ) {
	define( 'BEEPWEAR_EMIT_FAQ', true );
}

/**
 * The FAQ question/answer pairs.
 *
 * Answers are plain text (schema-safe). Keep in sync with content/faq.md and the
 * live FAQ page. Extend or override via the `beepwear/faq_items` filter. Replace
 * any "[confirm: …]" text with a verified answer to make that item eligible.
 *
 * @return array<int,array{q:string,a:string}>
 */
function beepwear_faq_items() {
	$items = array(
		array( 'q' => 'Are the watches authentic?', 'a' => 'Yes. Every timepiece is sourced through legitimate channels and presented with accurate specifications and honest imagery. See our Authenticity Guarantee.' ),
		array( 'q' => 'What is included with my purchase?', 'a' => 'Each watch ships with its presentation box and warranty card; any additional items are listed under "What\'s Included" on the product page.' ),
		array( 'q' => 'How do I choose the right watch?', 'a' => 'Our buying guides cover movements, materials, sizing, and features to help you decide.' ),
		array( 'q' => 'How do I place an order?', 'a' => 'Add items to your bag and follow the secure checkout. Guest checkout is available.' ),
		array( 'q' => 'Can I cancel or modify my order?', 'a' => 'Contact us as soon as possible — we can usually update or cancel before dispatch, not after.' ),
		array( 'q' => 'Which payment methods are accepted?', 'a' => 'See the Payment Policy. We show all available methods at checkout.' ),
		array( 'q' => 'Is my payment secure?', 'a' => 'Yes — payments are encrypted and processed by a PCI-compliant gateway; we do not store your card details.' ),
		array( 'q' => 'How long does shipping take?', 'a' => 'Typically [confirm: 3–6] business days after dispatch, depending on destination. See the Shipping Policy.' ),
		array( 'q' => 'Do you ship internationally?', 'a' => 'Yes, to our supported regions. Import duties may apply on international orders.' ),
		array( 'q' => 'Can I track my order?', 'a' => 'Yes — you will receive a tracking link by email, and it is available in your account.' ),
		array( 'q' => 'How do I return a product?', 'a' => 'Contact us within the return window with your order number; see Returns & Refunds.' ),
		array( 'q' => 'When will I receive my refund?', 'a' => 'Within [confirm: 5–10] business days after we receive and inspect your return.' ),
		array( 'q' => 'What does the warranty cover?', 'a' => 'Manufacturing defects under normal use — see the Warranty Policy.' ),
		array( 'q' => 'How do I submit a warranty claim?', 'a' => 'Contact us with your order number and details; we will guide you through it.' ),
		array( 'q' => 'How do I create an account?', 'a' => 'Register during checkout or from the account page.' ),
		array( 'q' => 'How do I reset my password?', 'a' => 'Use "Forgot password" on the login page to receive a reset link.' ),
		array( 'q' => 'How do I contact BeepWear?', 'a' => 'See the Contact page for email, hours, and response times.' ),
		array( 'q' => 'What are your customer service hours?', 'a' => '[confirm: business hours and time zone.]' ),
	);

	return (array) apply_filters( 'beepwear/faq_items', $items );
}

/**
 * Is the current request the FAQ page?
 *
 * Matches a page whose slug is in the filterable list (default: faq, support-faq).
 *
 * @return bool
 */
function beepwear_is_faq_page() {
	if ( ! is_page() ) {
		return false;
	}
	$slugs = (array) apply_filters( 'beepwear/faq_page_slugs', array( 'faq', 'support-faq' ) );
	$post  = get_queried_object();
	return $post && isset( $post->post_name ) && in_array( $post->post_name, $slugs, true );
}

/**
 * Emit FAQPage JSON-LD on the FAQ page, skipping unconfirmed answers.
 */
function beepwear_faq_schema() {
	if ( ! BEEPWEAR_EMIT_SCHEMA || ! BEEPWEAR_EMIT_FAQ || ! beepwear_is_faq_page() ) {
		return;
	}

	$questions = array();
	foreach ( beepwear_faq_items() as $item ) {
		if ( empty( $item['q'] ) || empty( $item['a'] ) ) {
			continue;
		}
		// Never publish placeholder answers into structured data.
		if ( false !== stripos( $item['a'], '[confirm' ) ) {
			continue;
		}
		$questions[] = array(
			'@type'          => 'Question',
			'name'           => wp_strip_all_tags( $item['q'] ),
			'acceptedAnswer' => array(
				'@type' => 'Answer',
				'text'  => wp_strip_all_tags( $item['a'] ),
			),
		);
	}

	if ( count( $questions ) < 2 ) {
		return; // Not enough verified Q&A to be worth a FAQPage entity.
	}

	beepwear_print_jsonld(
		array(
			'@context'   => 'https://schema.org',
			'@type'      => 'FAQPage',
			'@id'        => trailingslashit( get_permalink() ) . '#faq',
			'mainEntity' => $questions,
		)
	);
}
add_action( 'wp_head', 'beepwear_faq_schema' );
