<?php
/**
 * BeepWear front page (homepage) — native render of the approved design.
 *
 * @package BeepWear
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }
get_header();
?>

<main class="bw-home">

	<!-- Hero -->
	<section class="bw-hero">
		<div class="bw-hero-mark" aria-hidden="true"></div>
		<div class="bw-container bw-hero-inner">
			<p class="bw-eyebrow bw-hero-eyebrow"><?php esc_html_e( 'The BeepWear Boutique', 'beepwear' ); ?></p>
			<h1 class="bw-hero-title"><?php esc_html_e( 'Timeless Luxury. Exceptional Timepieces.', 'beepwear' ); ?></h1>
			<p class="bw-hero-lead"><?php esc_html_e( 'Discover an expertly curated collection of luxury watches for those who value precision, craftsmanship, and enduring style. From iconic classics to modern masterpieces, BeepWear helps you find the watch that marks every occasion.', 'beepwear' ); ?></p>
			<div class="bw-hero-cta">
				<a class="bw-btn" href="<?php echo esc_url( home_url( '/shop/' ) ); ?>"><?php esc_html_e( 'Shop Watches', 'beepwear' ); ?></a>
				<a class="bw-btn bw-btn--ghost" href="<?php echo esc_url( home_url( '/collections/' ) ); ?>"><?php esc_html_e( 'Explore Collections', 'beepwear' ); ?></a>
			</div>
			<div class="bw-hero-trust">
				<span><?php esc_html_e( 'Secure Checkout', 'beepwear' ); ?></span>
				<span><?php esc_html_e( 'Worldwide Shipping', 'beepwear' ); ?></span>
				<span><?php esc_html_e( 'Dedicated Support', 'beepwear' ); ?></span>
				<span><?php esc_html_e( 'Authentic Products', 'beepwear' ); ?></span>
			</div>
		</div>
	</section>

	<!-- Featured products -->
	<section class="bw-section">
		<div class="bw-container">
			<div class="bw-shead">
				<div><p class="bw-eyebrow"><?php esc_html_e( 'Handpicked', 'beepwear' ); ?></p><h2><?php esc_html_e( 'Featured Timepieces', 'beepwear' ); ?></h2></div>
				<a class="bw-link-more" href="<?php echo esc_url( home_url( '/shop/' ) ); ?>"><?php esc_html_e( 'Shop All', 'beepwear' ); ?></a>
			</div>
			<?php echo do_shortcode( '[products limit="8" columns="4" orderby="date" visibility="visible"]' ); ?>
		</div>
	</section>

	<!-- Lifestyle band -->
	<section class="bw-life bw-onDark">
		<div class="bw-life-art" aria-hidden="true"></div>
		<div class="bw-life-txt">
			<p class="bw-eyebrow" style="color:var(--bw-champagne)"><?php esc_html_e( 'Crafted for Every Moment', 'beepwear' ); ?></p>
			<h2><?php esc_html_e( 'More Than a Way to Tell Time', 'beepwear' ); ?></h2>
			<p><?php esc_html_e( "A luxury watch reflects personal style, celebrates milestones, and accompanies life's most meaningful moments. At BeepWear, every timepiece is selected with an emphasis on quality, craftsmanship, and enduring design.", 'beepwear' ); ?></p>
			<a class="bw-btn bw-btn--ghost" href="<?php echo esc_url( home_url( '/collections/' ) ); ?>"><?php esc_html_e( 'Explore the Collection', 'beepwear' ); ?></a>
		</div>
	</section>

	<!-- Why choose -->
	<section class="bw-section bw-section--soft">
		<div class="bw-container">
			<div class="bw-shead"><div><p class="bw-eyebrow"><?php esc_html_e( 'The BeepWear Difference', 'beepwear' ); ?></p><h2><?php esc_html_e( 'Why Choose BeepWear', 'beepwear' ); ?></h2></div></div>
			<div class="bw-why">
				<?php
				$why = array(
					array( 'Authentic Selection', 'Every product is sourced through legitimate channels and presented with accurate information, so you can shop with confidence.' ),
					array( 'Curated Collection', 'Our catalogue is thoughtfully organized to help you discover watches that suit your lifestyle, preferences, and budget.' ),
					array( 'Secure Shopping', 'Your privacy and payment security are protected with modern encryption and trusted payment gateways.' ),
					array( 'Worldwide Delivery', 'We provide reliable shipping options to customers across supported regions.' ),
					array( 'Dedicated Support', 'Our team is available to help with product questions, orders, and after-sales support during published business hours.' ),
					array( 'Easy Shopping Experience', 'From browsing to checkout, every step is clear, intuitive, and considered.' ),
				);
				$i = 1;
				foreach ( $why as $w ) {
					printf(
						'<div class="bw-why-cell"><div class="bw-why-n">%02d</div><h3>%s</h3><p>%s</p></div>',
						$i++, esc_html( $w[0] ), esc_html( $w[1] )
					);
				}
				?>
			</div>
		</div>
	</section>

	<!-- Newsletter -->
	<section class="bw-news bw-onDark">
		<div class="bw-container">
			<h2><?php esc_html_e( 'Stay Connected With BeepWear', 'beepwear' ); ?></h2>
			<p><?php esc_html_e( 'Subscribe for new arrivals, featured collections, educational articles, and occasional offers.', 'beepwear' ); ?></p>
			<?php echo do_shortcode( '[newsletter_form]' ); ?>
			<p class="bw-news-note"><?php esc_html_e( 'We use your details only to send BeepWear updates. Unsubscribe anytime.', 'beepwear' ); ?></p>
		</div>
	</section>

</main>

<?php
get_footer();
