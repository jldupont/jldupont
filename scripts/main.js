/*
 * 
 * @author Jean-Lou Dupont
 * 
 */

// Customization section.
// {{
var baseUri = 'http://jldupont.googlecode.com/svn/scripts/';
// }}

// Chili Syntax Highlighter
// ------------------------
jQuery.getScript( baseUri+'chili/jquery.chili.pack.js',
	function(){
		ChiliBook.elementPath = 'source';
		// don't start without having swapped 
		// the 'lang' attribute for 'class' ones!
		ChiliBook.automatic = false;		
	} 
);
jQuery.getScript( baseUri+'chili/recipes.js' );

(function(){
	var s = document.createElement ('link');
	s.type = 'text/css';
	s.rel = 'stylesheet';
	s.href = baseUri+"chili/recipes.css";
	document.getElementsByTagName('head')[0].appendChild(s);
})(); 

$(document).ready(
	function()
	{
		arr = $("source").attr('lang');
		for (el in arr )
		{
			alert( el );
		}
		
		ChiliBook.chili();
	}
);