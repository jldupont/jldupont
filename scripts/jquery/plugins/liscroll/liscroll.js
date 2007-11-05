/*
 <ul id="ticker01">
	<li><span>10/10/2007</span><a href="#">The first thing ...</a></li>
	<li><span>10/10/2007</span><a href="#">End up doing is ...</a></li>
	<li><span>10/10/2007</span><a href="#">The code that you ...</a></li>
	<!-- eccetera -->
 </ul>

	$(function(){
		$("ul#ticker01").liScroll();
	});
	
	If you want your list to scroll faster or slower than the default value, modify the travelocity param
	
	$(function(){
		$("ul#ticker02").liScroll({travelocity: 0.15});
	});
  
 */

jQuery.fn.liScroll = function(settings) {
		settings = jQuery.extend({
		travelocity: 0.07
		}, settings);		
		return this.each(function(){
				var $strip = jQuery(this);
				$strip.addClass("newsticker")
				var stripWidth = 0;
				var $mask = $strip.wrap("<div class='mask'></div>");
				var $tickercontainer = $strip.parent().wrap("<div class='tickercontainer'></div>");								
				var containerWidth = $strip.parent().parent().width();	//a.k.a. 'mask' width 	
				$strip.find("li").each(function(i){
				stripWidth += jQuery(this, i).width();
				});
				$strip.width(stripWidth);			
				var defTiming = stripWidth/settings.travelocity;
				var totalTravel = stripWidth+containerWidth;								
				function scrollnews(spazio, tempo){
				$strip.animate({left: '-='+ spazio}, tempo, "linear", function(){$strip.css("left", containerWidth); scrollnews(totalTravel, defTiming);});
				}
				scrollnews(totalTravel, defTiming);				
				$strip.hover(function(){
				jQuery(this).stop();
				},
				function(){
				var offset = jQuery(this).offset();
				var residualSpace = offset.left + stripWidth;
				var residualTime = residualSpace/settings.travelocity;
				scrollnews(residualSpace, residualTime);
				});			
		});	
};