<?php
/* Configures Complianz for a German/EU webshop: EU region, business contact details, no statistics/ads/social cookies, prior opt-in with visible categories, and no duplicate legal pages (ours already exist). */
if ( function_exists( 'cmplz_update_option' ) ) {
	// Wizard: who and where
	cmplz_update_option( 'wizard', 'organisation_name', 'kaisercontainers' );
	cmplz_update_option( 'wizard', 'country', 'DE' );
	cmplz_update_option( 'wizard', 'regions', array( 'eu' => 1 ) );
	cmplz_update_option( 'wizard', 'purpose_of_processing', 'webshop' );
	// Contact details used in the generated documents
	cmplz_update_option( 'wizard', 'email', 'info@kaisercontainers.de' );
	cmplz_update_option( 'wizard', 'telephone', '+49 201 49869542' );
	cmplz_update_option( 'wizard', 'address_company', 'Homberg/Ruhrort/Baerl, 47138 Duisburg, Deutschland' );
	// No analytics, advertising or social-media tracking is installed on this site
	cmplz_update_option( 'wizard', 'compile_statistics', 'no' );
	cmplz_update_option( 'wizard', 'uses_ad_cookies', 'no' );
	cmplz_update_option( 'wizard', 'uses_social_media', 'no' );
	cmplz_update_option( 'wizard', 'uses_cookies', 'yes' );      // functional: cart, session
	// Consent behaviour: prior opt-in, no pre-ticked non-essential categories
	cmplz_update_option( 'settings', 'consenttype', 'optin' );
	cmplz_update_option( 'settings', 'use_categories', 'visible' );
	cmplz_update_option( 'settings', 'respect_dnt', 'yes' );
	// Do not let Complianz publish its own duplicate legal pages; ours already exist
	cmplz_update_option( 'wizard', 'create_cookiepolicy', 'no' );
	cmplz_update_option( 'wizard', 'create_privacy_statement', 'no' );
	if ( function_exists( 'cmplz_wizard_completed_first_step' ) ) { update_option( 'cmplz_wizard_completed_once', true ); }
	update_option( 'cmplz_configuration_by_config', true );
}