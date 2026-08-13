<?php
/* Installs de_DE translation packs for plugins and themes so WooCommerce renders in German. */
// Install translation packs for plugins and themes (WooCommerce strings etc.) in de_DE.
if ( ! class_exists( 'Language_Pack_Upgrader' ) ) {
	require_once ABSPATH . 'wp-admin/includes/class-wp-upgrader.php';
}
if ( ! function_exists( 'wp_get_translation_updates' ) ) {
	require_once ABSPATH . 'wp-admin/includes/update.php';
}
wp_clean_update_cache();
wp_update_plugins();
wp_update_themes();
$updates = wp_get_translation_updates();
$skin = new Automatic_Upgrader_Skin();
$upgrader = new Language_Pack_Upgrader( $skin );
$res = $upgrader->bulk_upgrade();
update_option( 'kc_tr_result', is_array( $res ) ? count( $res ) . ' packs' : 'none' );