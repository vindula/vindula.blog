$j = jQuery.noConflict();

$j(document).ready(function(){
	
	/* MENU: BLOG CONTEXT */
	
	function menuInitial() {
		$j('#blog-initial').show();
		$j('#blog-abaut').hide();
		$j('#blog-authors').hide();
	}
	
	function menuAbaut() {
		$j('#blog-initial').hide();
		$j('#blog-abaut').show();
		$j('#blog-authors').hide();
	}
	
	function menuAuthors() {
		$j('#blog-initial').hide();
		$j('#blog-abaut').hide();
		$j('#blog-authors').show();
	}
	
	/* When the page loads */
	if(window.location.href.search('#abaut') != -1)
		menuAbaut();
		
	if(window.location.href.search('#authors') != -1)
		menuAuthors();


	/* When click on menu */
	$j('#blog-top-menu #initial').click(function() {
		menuInitial();
	})
	$j('#blog-top-menu #abaut').click(function() {
		menuAbaut();
	})
	$j('#blog-top-menu #authors').click(function() {
		menuAuthors();
	})
	
	
	/* MENU: POST CONTEXT */
	
	$j('#context-post').each(function() {
		var url = $j(this).val();
		$j('#blog-top-menu #initial').click(function() {
			window.location = url
		})
		$j('#blog-top-menu #abaut').click(function() {
			window.location = url + '#abaut';
		})
		$j('#blog-top-menu #authors').click(function() {
			window.location = url + '#authors';
		})
	})
	
});