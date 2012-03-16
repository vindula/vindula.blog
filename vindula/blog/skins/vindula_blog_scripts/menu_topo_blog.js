$j = jQuery.noConflict();

$j(document).ready(function(){

	$j("#blog-top-menu ul li").hover(
	  function () {
	    $j(this).addClass('hover');
	  },
	  function () {
	    $j(this).removeClass('hover');
	  }
	)

})