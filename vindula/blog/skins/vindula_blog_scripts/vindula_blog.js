$j = jQuery.noConflict();

$j(document).ready(function(){
	
	$j('#blog-top-menu #initial').click(function() {
		$j('#blog-initial').show();
		$j('#blog-abaut').hide();
		$j('#blog-authors').hide();
	})
	
	$j('#blog-top-menu #abaut').click(function() {
		$j('#blog-initial').hide();
		$j('#blog-abaut').show();
		$j('#blog-authors').hide();
	})
	
	$j('#blog-top-menu #authors').click(function() {
		$j('#blog-initial').hide();
		$j('#blog-abaut').hide();
		$j('#blog-authors').show();
	})

});