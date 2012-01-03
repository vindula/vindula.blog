$j = jQuery.noConflict();

$j(document).ready(function() {
	$j('.fancy-comment').fancybox({
		'autoDimensions':true,
		'scrolling': false,
		'onStart': function() {
			$j('#fancybox-outer').contents().filter('.fancy-bg').addClass('fancy-laranja-hack');
			if ($j.browser.msie) {
				$j('#banner').hide();
			}
		},
		'onClosed': function() {
			$j('#fancybox-outer').contents().filter('.fancy-bg').removeClass('fancy-laranja-hack');
			if ($j.browser.msie) {
				$j('#banner').show();
			}
		}
	});
})