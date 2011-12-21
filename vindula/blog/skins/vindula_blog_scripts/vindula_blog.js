$j = jQuery.noConflict();

$j(document).ready(function(){

	/* SEVERAL FOR VINDULA BLOG */
	
	/* Portlet Blog Files */
	$j('#blogsearch input[name=search-word]').focus(function() {
  		$j(this).val("");
		$j(this).removeClass();
	});
	
	
	/* Search for subject */
	$j('.post-subject').click(function() {
		$j('#search-subject input[name=search-subject]').val($j(this).text());
		$j('#search-subject').submit();
	});
});