<?php
/**
 * kaisercontainers — Global product-page info (brief §17)
 * Adds a consistent "Versand, Abholung & Verfügbarkeit" section + a returns/payment
 * summary to EVERY product, so availability and policy wording stay identical across
 * all products without editing each one. Add to a CHILD theme's functions.php or a
 * code-snippets plugin. Update-safe (no parent-theme edits).
 */

// Extra product tab with the standard info.
add_filter( 'woocommerce_product_tabs', function ( $tabs ) {
	$tabs['kc_versand'] = array(
		'title'    => 'Versand, Abholung & Verfügbarkeit',
		'priority' => 25,
		'callback' => 'kc_render_versand_tab',
	);
	return $tabs;
} );

function kc_render_versand_tab() {
	echo '<h3>Verfügbarkeit</h3>';
	echo '<p><strong>Online- und Ladenverfügbarkeit können abweichen.</strong> Bitte kontaktieren '
		. 'Sie uns vor einem Besuch, um die Verfügbarkeit eines bestimmten Containers zu bestätigen.</p>';

	echo '<h3>Lieferung & Abholung</h3>';
	echo '<ul>';
	echo '<li>Bearbeitungszeit: 0–1 Werktage.</li>';
	echo '<li>Voraussichtliche Lieferzeit: 2–5 Werktage (deutschlandweit).</li>';
	echo '<li>Abholung nach Absprache an unserem Standort in Duisburg.</li>';
	echo '</ul>';
	echo '<p>Details: <a href="/versand/">Versand &amp; Lieferung</a>.</p>';

	echo '<h3>Zahlung</h3>';
	echo '<p>Zahlung per Banküberweisung. Siehe <a href="/zahlung/">Zahlung</a>.</p>';

	echo '<h3>Rückgabe</h3>';
	echo '<p>14 Tage gesetzliches Widerrufsrecht plus freiwillige 30-Tage-Rückgabe. '
		. 'Siehe <a href="/widerruf/">Widerruf &amp; Rückgabe</a>.</p>';
}

// Short trust line directly under the Add-to-cart button.
add_action( 'woocommerce_single_product_summary', function () {
	echo '<p class="kc-product-trust" style="margin-top:10px;color:#5B6670;font-size:.92rem;">'
		. 'Neu &amp; gebraucht · Lieferung deutschlandweit · Abholung in Duisburg · '
		. 'Zahlung per Überweisung. <br>Verfügbarkeit vor einem Besuch bitte telefonisch bestätigen.'
		. '</p>';
}, 35 );
