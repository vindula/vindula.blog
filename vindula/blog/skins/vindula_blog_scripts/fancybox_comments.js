$j = jQuery.noConflict();

$j(document).ready(function() {
	$j('.fancy-comment').fancybox({
		'autoDimensions':false,
		'scrolling': false,
		'onStart': function() {
			$j('#fancybox-outer').contents().filter('.fancybox-bg').addClass('fancy-laranja-hack');
			if ($j.browser.msie) {
				$j('#banner').hide();
			}
		},
		'onClosed': function() {
			$j('#fancybox-outer').contents().filter('.fancybox-bg').removeClass('fancy-laranja-hack');
			if ($j.browser.msie) {
				$j('#banner').show();
			}
		}
	});
})