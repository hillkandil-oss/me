<?php
/* Runs once to purge the full LiteSpeed page cache so visitors receive current HTML. */
if ( defined( 'LSCWP_V' ) || class_exists( '\\LiteSpeed\\Purge' ) ) {
	do_action( 'litespeed_purge_all' );
}
if ( function_exists( 'wp_cache_flush' ) ) { wp_cache_flush(); }