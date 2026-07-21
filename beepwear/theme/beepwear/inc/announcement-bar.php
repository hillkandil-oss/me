<?php
/**
 * Announcement bar — admin-configurable via the Customizer.
 *
 * Rotating messages shown above the header. Staff edit messages (one per line),
 * toggle visibility, and set rotation speed without touching code.
 *
 * @package BeepWear
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Register Customizer settings under a BeepWear panel.
 *
 * @param WP_Customize_Manager $wp_customize Customizer instance.
 */
function beepwear_announcement_customize( $wp_customize ) {
	$wp_customize->add_section(
		'beepwear_announcement',
		array(
			'title'       => __( 'Announcement Bar', 'beepwear' ),
			'priority'    => 30,
			'description' => __( 'Rotating messages shown above the header.', 'beepwear' ),
		)
	);

	$wp_customize->add_setting(
		'beepwear_announcement_enabled',
		array(
			'default'           => true,
			'sanitize_callback' => 'wp_validate_boolean',
		)
	);
	$wp_customize->add_control(
		'beepwear_announcement_enabled',
		array(
			'label'   => __( 'Show announcement bar', 'beepwear' ),
			'section' => 'beepwear_announcement',
			'type'    => 'checkbox',
		)
	);

	$wp_customize->add_setting(
		'beepwear_announcement_messages',
		array(
			'default'           => "Free worldwide shipping on eligible orders\n100% secure checkout\nAuthentic luxury watches\nDedicated customer support\nHassle-free returns",
			'sanitize_callback' => 'sanitize_textarea_field',
		)
	);
	$wp_customize->add_control(
		'beepwear_announcement_messages',
		array(
			'label'       => __( 'Messages (one per line)', 'beepwear' ),
			'description' => __( 'Each line rotates in turn.', 'beepwear' ),
			'section'     => 'beepwear_announcement',
			'type'        => 'textarea',
		)
	);

	$wp_customize->add_setting(
		'beepwear_announcement_speed',
		array(
			'default'           => 4,
			'sanitize_callback' => 'absint',
		)
	);
	$wp_customize->add_control(
		'beepwear_announcement_speed',
		array(
			'label'       => __( 'Seconds per message', 'beepwear' ),
			'section'     => 'beepwear_announcement',
			'type'        => 'number',
			'input_attrs' => array(
				'min' => 2,
				'max' => 15,
			),
		)
	);
}
add_action( 'customize_register', 'beepwear_announcement_customize' );

/**
 * Render the announcement bar at the top of <body>.
 */
function beepwear_announcement_render() {
	if ( ! get_theme_mod( 'beepwear_announcement_enabled', true ) ) {
		return;
	}

	$raw   = (string) get_theme_mod( 'beepwear_announcement_messages', '' );
	$lines = array_values( array_filter( array_map( 'trim', explode( "\n", $raw ) ) ) );
	if ( empty( $lines ) ) {
		return;
	}

	$speed = absint( get_theme_mod( 'beepwear_announcement_speed', 4 ) );
	$speed = max( 2, min( 15, $speed ) );

	echo '<div class="bw-announce" data-speed="' . esc_attr( $speed ) . '" role="status" aria-live="polite">';
	foreach ( $lines as $i => $line ) {
		printf(
			'<span class="bw-announce__msg%s">%s</span>',
			0 === $i ? ' is-active' : '',
			esc_html( $line )
		);
	}
	echo '</div>';
}
add_action( 'wp_body_open', 'beepwear_announcement_render' );
