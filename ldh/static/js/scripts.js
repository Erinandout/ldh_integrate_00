/**
 * Created by scottcampbell on 3/19/14.
 */

/*jScroll pane

*/
$(window).load(function(){
	$('.scroll-pane').jScrollPane({
        showArrows:	true,
		verticalGutter:			30,
		hijackInternalLinks:	true,
		animateScroll:			true
	});


});

$(window).resize(function(){
    $.each( $('.scroll-pane'), function(){
            var api = $(this).data('jsp');
            api.reinitialise();
    });
});

