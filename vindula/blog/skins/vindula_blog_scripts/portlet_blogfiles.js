$j = jQuery.noConflict();

$j(document).ready(function(){

	/* GALLERY CYCLE PORTLET BLOG FILES */
	
	var height = $j("#files div").height();
	$j("#files").attr('id', 'blogfiles');
	
	$j('#blogfiles').cycle({
	    fx:     'scrollHorz',
		speed: 	100,
	    next:   '#cycle-next',
	    prev:   '#cycle-prev',
		height: height,
		timeout: 0
	});
	
});