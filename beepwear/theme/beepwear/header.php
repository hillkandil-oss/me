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

<div class="bw-utilitybar">
	<div class="bw-container bw-utilitybar__row">
		<a href="tel:+16053619867" aria-label="Call BeepWear"><span aria-hidden="true">&#9742;</span> +1 605-361-9867</a>
		<a href="mailto:info@beepwear.com" aria-label="Email BeepWear"><span aria-hidden="true">&#9993;</span> info@beepwear.com</a>
		<span class="bw-utilitybar__addr"><span aria-hidden="true">&#9679;</span> 510 Main St, Wall, SD 57790</span>
	</div>
</div>

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

		<button class="bw-burger" id="bw-burger" aria-label="<?php esc_attr_e( 'Open menu', 'beepwear' ); ?>" aria-controls="bw-mobile-nav" aria-expanded="false">
			<span class="bw-burger__box" aria-hidden="true"><span class="bw-burger__line"></span></span>
		</button>
	</div>
</header>

<!-- Mobile navigation -->
<div class="bw-mobile-nav" id="bw-mobile-nav" hidden>
	<div class="bw-mobile-nav__panel" role="dialog" aria-modal="true" aria-label="<?php esc_attr_e( 'Menu', 'beepwear' ); ?>">
		<?php
		$bw_mobile_links = array(
			'/shop/'        => __( 'Shop', 'beepwear' ),
			'/brands/'      => __( 'Brands', 'beepwear' ),
			'/collections/' => __( 'Collections', 'beepwear' ),
			'/journal/'     => __( 'Journal', 'beepwear' ),
			'/about/'       => __( 'About', 'beepwear' ),
			'/support/'     => __( 'Support', 'beepwear' ),
			'/contact/'     => __( 'Contact', 'beepwear' ),
		);
		echo '<nav class="bw-mobile-nav__list" aria-label="' . esc_attr__( 'Mobile', 'beepwear' ) . '">';
		if ( has_nav_menu( 'primary' ) ) {
			wp_nav_menu(
				array(
					'theme_location' => 'primary',
					'container'      => false,
					'menu_class'     => 'bw-mobile-menu',
					'depth'          => 1,
				)
			);
		} else {
			foreach ( $bw_mobile_links as $url => $label ) {
				printf( '<a href="%s">%s</a>', esc_url( home_url( $url ) ), esc_html( $label ) );
			}
		}
		echo '</nav>';
		?>
		<?php if ( class_exists( 'WooCommerce' ) ) : ?>
			<div class="bw-mobile-nav__account">
				<a href="<?php echo esc_url( wc_get_page_permalink( 'myaccount' ) ); ?>"><?php esc_html_e( 'Account', 'beepwear' ); ?></a>
				<a href="<?php echo esc_url( wc_get_cart_url() ); ?>"><?php esc_html_e( 'Cart', 'beepwear' ); ?> (<?php echo esc_html( WC()->cart ? WC()->cart->get_cart_contents_count() : 0 ); ?>)</a>
			</div>
		<?php endif; ?>
		<div class="bw-mobile-nav__contact">
			<a href="tel:+16053619867">+1 605-361-9867</a>
			<a href="mailto:info@beepwear.com">info@beepwear.com</a>
		</div>
	</div>
</div>
