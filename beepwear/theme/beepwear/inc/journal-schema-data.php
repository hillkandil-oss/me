<?php
/**
 * Journal structured-data source (FAQ + HowTo), keyed by post slug.
 *
 * This mirrors the FAQ / step content published in the guide bodies
 * (see repo `content/guides/*.md`). It powers the theme's JSON-LD fallback
 * in inc/schema.php. In production, when Rank Math's FAQ/HowTo blocks own the
 * schema, set BEEPWEAR_EMIT_SCHEMA to false so this stays a dormant fallback
 * and no duplicate schema is emitted.
 *
 * Keep answers truthful to real BeepWear operations and in sync with the
 * guide bodies when either changes.
 *
 * @package BeepWear
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * FAQ + HowTo data for journal guides, keyed by post slug.
 *
 * @return array<string,array>
 */
function beepwear_journal_schema_data() {
	return array(
		'water-resistance-guide' => array(
			'faq' => array(
				array(
					'q' => 'Can I shower with a 50m water-resistant watch?',
					'a' => "It's best avoided. 50m survives a brief, shallow splash, but hot water and steam degrade the seals over time. Treat 100m as the sensible minimum for regular water contact.",
				),
				array(
					'q' => 'What does 100m water resistance really mean?',
					'a' => '100m (10 ATM) is safe for swimming and snorkelling in normal conditions. It is the practical everyday threshold at which most people can stop worrying about incidental water.',
				),
				array(
					'q' => 'Is a 30m watch waterproof?',
					'a' => 'No watch is truly "waterproof." A 30m rating means splash-resistant only — fine for rain and hand-washing, but not for swimming or submersion.',
				),
				array(
					'q' => 'How often should watch seals be checked?',
					'a' => 'Have the gaskets pressure-tested every couple of years, and always before you rely on the watch in water. Seals age whether or not the watch gets wet.',
				),
			),
		),
		'automatic-vs-quartz'    => array(
			'faq' => array(
				array(
					'q' => 'Is automatic or quartz better?',
					'a' => 'Neither is universally better. Quartz is more accurate and lower-maintenance; automatic offers mechanical craft and heirloom appeal. The right choice depends on whether you value precision and convenience or tradition and character.',
				),
				array(
					'q' => 'Do automatic watches need a battery?',
					'a' => "No. Automatic watches are powered by a mainspring wound by your wrist's motion, not a battery. They stop if left unworn for a day or two and simply need winding and resetting.",
				),
				array(
					'q' => 'How long do automatic and quartz watches last?',
					'a' => 'Both can last decades with care. A serviced mechanical watch can run for generations; a quartz watch keeps going reliably as long as the battery is replaced and the case is resealed properly.',
				),
				array(
					'q' => 'Is quartz less prestigious than automatic?',
					'a' => 'Not inherently. There are exceptional and highly collectible watches of both types. Prestige comes from the watch\'s quality, finishing, and heritage — not the movement type alone.',
				),
			),
		),
		'watch-size-guide'       => array(
			'faq' => array(
				array(
					'q' => 'What size watch is best for a 7-inch (18 cm) wrist?',
					'a' => 'An 18 cm wrist comfortably carries cases from about 40 mm up, though 38–42 mm remains the most versatile range. Check the lug-to-lug measurement to be sure the watch does not overhang.',
				),
				array(
					'q' => 'Is a 40 mm watch too big?',
					'a' => 'Not usually — 40 mm is a mainstream, versatile size for medium and larger wrists. On smaller wrists (under 16 cm), a shorter lug-to-lug matters more than the diameter itself.',
				),
				array(
					'q' => 'What is lug-to-lug and where do I find it?',
					'a' => 'Lug-to-lug is the total length of the case from the top lug tips to the bottom lug tips. It is listed on most detailed spec sheets and is the best single predictor of fit.',
				),
				array(
					'q' => 'Should I size a watch by diameter or lug-to-lug?',
					'a' => 'Use both, but let lug-to-lug lead. A watch whose lugs extend past the edges of your wrist will feel too large regardless of its diameter.',
				),
			),
		),
		'watch-materials-guide'  => array(
			'faq' => array(
				array(
					'q' => 'What is the best material for a watch case?',
					'a' => 'For an everyday watch, stainless steel is the best all-round choice — strong, corrosion-resistant, and repolishable. Titanium is better for lightness and sensitive skin; gold suits dressy wear.',
				),
				array(
					'q' => 'Is sapphire crystal worth it?',
					'a' => 'Yes. Sapphire is one of the hardest materials used in watches and resists scratches far better than mineral or acrylic. It is the detail that keeps a watch looking new the longest.',
				),
				array(
					'q' => 'Is titanium better than stainless steel?',
					'a' => 'Titanium is lighter and hypoallergenic but scratches more easily. Steel is more scratch-resistant and repolishable. Choose titanium for comfort and sensitive skin, steel for durability and versatility.',
				),
				array(
					'q' => 'Does ceramic scratch?',
					'a' => 'Ceramic resists scratches exceptionally well and never fades in colour, but it is more brittle than metal and can chip or crack under a hard, direct impact.',
				),
			),
		),
		'luxury-watch-buying-guide' => array(
			'faq' => array(
				array(
					'q' => 'How much should I spend on a luxury watch?',
					'a' => "Set a firm ceiling you're comfortable with and find the best-executed watch beneath it, rather than stretching for the most prestigious name. Leave room for servicing, a spare strap, and other ownership costs.",
				),
				array(
					'q' => 'What is the best first luxury watch?',
					'a' => 'A versatile one: a stainless-steel case, sapphire crystal, and a size that fits your wrist, in a movement that matches how involved you want to be. Versatility matters more than prestige for a single watch.',
				),
				array(
					'q' => 'Should my first watch be automatic or quartz?',
					'a' => 'Choose automatic for mechanical craft and tradition, or quartz for precision and low maintenance. Neither is "better" — it depends on your temperament.',
				),
				array(
					'q' => 'How do I know a watch is authentic?',
					'a' => 'Buy from a seller with a clear authenticity guarantee, accurate specifications, honest imagery, and transparent warranty and returns terms. Vague listings and pressure to "buy now" are warning signs.',
				),
			),
		),
		'watch-care-guide'       => array(
			'faq'   => array(
				array(
					'q' => 'How often should I service my watch?',
					'a' => "A mechanical watch typically benefits from servicing every three to five years, though intervals vary — follow the manufacturer's guidance. A quartz watch mainly needs a battery every one to two years.",
				),
				array(
					'q' => 'Can I wear my watch in the shower?',
					'a' => "It's best not to. Hot water and steam degrade the seals over time, even on water-resistant watches. Keep watches out of showers and saunas regardless of rating.",
				),
				array(
					'q' => 'How do I stop my watch from getting magnetised?',
					'a' => 'Keep it a hand\'s width from strong magnets like laptops, speakers and magnetic clasps. If it starts running fast, a watchmaker can demagnetise it in seconds.',
				),
				array(
					'q' => 'How do I clean a metal watch bracelet?',
					'a' => 'Use a soft brush with mild soapy water while the crown is closed, then rinse and dry thoroughly. A soft dry cloth after each wear keeps it bright between deeper cleans.',
				),
			),
			'howto' => array(
				'name'  => 'How to Care for Your Watch',
				'steps' => array(
					array( 'Everyday wear', 'Wipe the watch with a soft, dry cloth after wear to remove oils, dust and sweat. Take it off before heavy work, contact sports, and chemicals.' ),
					array( 'Storage', 'Store the watch somewhere dry, stable and padded — a box or soft pouch away from heat and humidity. Use a winder for a rotation of automatics.' ),
					array( 'Avoid magnetism', 'Keep the watch a hand\'s width from strong magnets such as laptops, speakers and magnetic clasps to protect mechanical accuracy.' ),
					array( 'Protect from moisture', 'Keep the crown pushed in or screwed down before any water contact, and never operate the crown while the watch is wet.' ),
					array( 'Service periodically', 'Have a mechanical watch serviced by a qualified watchmaker every few years; replace a quartz battery every one to two years and reseal the case.' ),
					array( 'Care for straps', 'Rotate leather straps to extend their life, rinse and dry rubber and fabric straps, and replace straps as they wear.' ),
				),
			),
		),
	);
}
