$j = jQuery.noConflict();

$j(document).ready(function(){

	/* GALLERY CYCLE PORTLET BLOG FILES */
	
	var length = $j("#files div").length;
	$j("#cycle-len").text('/'+length);
	
	var height = 0;
	$j("#files div").each(function() {
		if ($j(this).height() > height)
    		height = $j(this).height();
	});

	$j("#files").attr('id', 'blogfiles');
	
	$j('#blogfiles').cycle({
	    fx:     'scrollHorz',
	    next:   '#cycle-next',
	    prev:   '#cycle-prev',
		pager:  '#cycle-nav',
		height: height,
		speed: 	100,
		timeout: 0,
	});

	$j('#blogfiles li a').click(function() {	
		year = $j(this).parent().parent().parent().find('span').text();
		month = $j(this).attr('id');
		$j('#getposts input[name=blog_year]').val(year);
		$j('#getposts input[name=blog_month]').val(month);
		$j('#getposts').submit();
	});

});