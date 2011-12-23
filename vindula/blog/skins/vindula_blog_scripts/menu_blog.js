$j = jQuery.noConflict();

$j(document).ready(function(){
	
	/* MENU: BLOG CONTEXT */
	
	checkMenu();
	
	function menuInitial() {
		$j('#blog-initial').show();
		$j('#blog-abaut').hide();
		$j('#blog-authors').hide();
		checkMenu();
	}
	
	function menuAbaut() {
		$j('#blog-initial').hide();
		$j('#blog-abaut').show();
		$j('#blog-authors').hide();
		checkMenu();
	}
	
	function menuAuthors() {
		$j('#blog-initial').hide();
		$j('#blog-abaut').hide();
		$j('#blog-authors').show();
		checkMenu();
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
	
	/* MENU HOVER */
	
	function checkMenu(){
		if ($j('#context-post').val() == null) {
			if (!($j('#blog-initial').is(':hidden'))) 
				$j("li#initial").addClass('active');
			else 
				$j("li#initial").removeClass('active');
			
			if (!($j('#blog-abaut').is(':hidden'))) 
				$j("li#abaut").addClass('active');
			else 
				$j("li#abaut").removeClass('active');
			
			if (!( $j('#blog-authors').is(':hidden'))) 
				$j("li#authors").addClass('active');
			else 
				$j("li#authors").removeClass('active');
		}
	}
		
	$j("#blog-top-menu ul li").hover(
	  function () {
	    $j(this).addClass('hover');
	  },
	  function () {
	    $j(this).removeClass('hover');
	  }
	)

})