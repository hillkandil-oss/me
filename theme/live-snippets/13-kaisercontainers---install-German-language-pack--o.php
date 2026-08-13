<?php
/* Downloads the de_DE translation files and switches the site language, which the REST API cannot do. */
// Download and activate the German language pack, then switch the site to de_DE.
if ( ! function_exists( 'wp_download_language_pack' ) ) {
	require_once ABSPATH . 'wp-admin/includes/translation-install.php';
}
if ( ! function_exists( 'request_filesystem_credentials' ) ) {
	require_once ABSPATH . 'wp-admin/includes/file.php';
}
$installed = wp_download_language_pack( 'de_DE' );
if ( $installed ) {
	update_option( 'WPLANG', 'de_DE' );
	if ( function_exists( 'switch_to_locale' ) ) { switch_to_locale( 'de_DE' ); }
	update_option( 'kc_lang_result', 'installed: ' . $installed );
} else {
	update_option( 'kc_lang_result', 'download failed' );
}