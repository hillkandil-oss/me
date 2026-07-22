<?php
/**
 * BeepWear footer.
 *
 * @package BeepWear
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }
?>
<footer class="bw-site-footer bw-onDark">
	<div class="bw-container">
		<div class="bw-footer-cols">
			<div class="bw-footer-brand">
				<div class="bw-logo">Beep<b>Wear</b></div>
				<p>An international boutique for precision timepieces — curated, authenticated, and delivered with care.</p>
				<p class="bw-footer-contact">
					510 Main St, Wall, SD 57790<br>
					<a href="mailto:info@beepwear.com">info@beepwear.com</a><br>
					<a href="tel:+16053619867">+1 605-361-9867</a>
				</p>
			</div>
			<div>
				<h4><?php esc_html_e( 'Shop', 'beepwear' ); ?></h4>
				<ul>
					<li><a href="<?php echo esc_url( home_url( '/shop/' ) ); ?>"><?php esc_html_e( 'All Watches', 'beepwear' ); ?></a></li>
					<li><a href="<?php echo esc_url( home_url( '/new-arrivals/' ) ); ?>"><?php esc_html_e( 'New Arrivals', 'beepwear' ); ?></a></li>
					<li><a href="<?php echo esc_url( home_url( '/best-sellers/' ) ); ?>"><?php esc_html_e( 'Best Sellers', 'beepwear' ); ?></a></li>
					<li><a href="<?php echo esc_url( home_url( '/brands/' ) ); ?>"><?php esc_html_e( 'Brands', 'beepwear' ); ?></a></li>
				</ul>
			</div>
			<div>
				<h4><?php esc_html_e( 'Customer Service', 'beepwear' ); ?></h4>
				<ul>
					<li><a href="<?php echo esc_url( home_url( '/contact/' ) ); ?>"><?php esc_html_e( 'Contact Us', 'beepwear' ); ?></a></li>
					<li><a href="<?php echo esc_url( home_url( '/shipping-policy/' ) ); ?>"><?php esc_html_e( 'Shipping', 'beepwear' ); ?></a></li>
					<li><a href="<?php echo esc_url( home_url( '/returns/' ) ); ?>"><?php esc_html_e( 'Returns & Refunds', 'beepwear' ); ?></a></li>
					<li><a href="<?php echo esc_url( home_url( '/warranty-policy/' ) ); ?>"><?php esc_html_e( 'Warranty', 'beepwear' ); ?></a></li>
				</ul>
			</div>
			<div>
				<h4><?php esc_html_e( 'Company', 'beepwear' ); ?></h4>
				<ul>
					<li><a href="<?php echo esc_url( home_url( '/about/' ) ); ?>"><?php esc_html_e( 'About BeepWear', 'beepwear' ); ?></a></li>
					<li><a href="<?php echo esc_url( home_url( '/journal/' ) ); ?>"><?php esc_html_e( 'Journal', 'beepwear' ); ?></a></li>
					<li><a href="<?php echo esc_url( home_url( '/authenticity-guarantee/' ) ); ?>"><?php esc_html_e( 'Authenticity', 'beepwear' ); ?></a></li>
					<li><a href="<?php echo esc_url( home_url( '/privacy-policy/' ) ); ?>"><?php esc_html_e( 'Privacy Policy', 'beepwear' ); ?></a></li>
				</ul>
			</div>
		</div>
		<hr class="bw-hr">
		<div class="bw-footer-bottom">
			<span>&copy; <?php echo esc_html( gmdate( 'Y' ) ); ?> BeepWear. All rights reserved.</span>
			<span><?php esc_html_e( 'Secure checkout · Worldwide shipping · Authentic timepieces', 'beepwear' ); ?></span>
		</div>
	</div>
</footer>
<?php wp_footer(); ?>
</body>
</html>
