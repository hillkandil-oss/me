<?php
/**
 * BeepWear header — announcement bar + sticky luxury header.
 *
 * @package BeepWear
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }
?><!doctype html>
<html <?php language_attributes(); ?>>
<head>
	<meta charset="<?php bloginfo( 'charset' ); ?>">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

<header class="bw-site-header">
	<div class="bw-container bw-header-row">
		<a class="bw-logo" href="<?php echo esc_url( home_url( '/' ) ); ?>">Beep<b>Wear</b></a>

		<nav class="bw-nav" aria-label="<?php esc_attr_e( 'Primary', 'beepwear' ); ?>">
			<?php
			if ( has_nav_menu( 'primary' ) ) {
				wp_nav_menu(
					array(
						'theme_location' => 'primary',
						'container'      => false,
						'menu_class'     => 'bw-nav-list',
						'depth'          => 2,
					)
				);
			} else {
				$links = array(
					'/shop/'         => __( 'Shop', 'beepwear' ),
					'/brands/'       => __( 'Brands', 'beepwear' ),
					'/collections/'  => __( 'Collections', 'beepwear' ),
					'/journal/'      => __( 'Journal', 'beepwear' ),
					'/about/'        => __( 'About', 'beepwear' ),
					'/support/'      => __( 'Support', 'beepwear' ),
				);
				echo '<ul class="bw-nav-list">';
				foreach ( $links as $url => $label ) {
					printf( '<li><a href="%s">%s</a></li>', esc_url( home_url( $url ) ), esc_html( $label ) );
				}
				echo '</ul>';
			}
			?>
		</nav>

		<div class="bw-header-icons">
			<?php if ( class_exists( 'WooCommerce' ) ) : ?>
				<a href="<?php echo esc_url( wc_get_page_permalink( 'myaccount' ) ); ?>"><?php esc_html_e( 'Account', 'beepwear' ); ?></a>
				<a href="<?php echo esc_url( wc_get_cart_url() ); ?>"><?php esc_html_e( 'Cart', 'beepwear' ); ?> (<?php echo esc_html( WC()->cart ? WC()->cart->get_cart_contents_count() : 0 ); ?>)</a>
			<?php endif; ?>
		</div>
	</div>
</header>
