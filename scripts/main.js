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
		arr = $("source").attr("lang");
		for ( el in arr )
		{
			alert( el );
/*
			el.each(	function( obj, index ){
						old_value = obj.attr(obj, 'class');
						obj.attr(obj, 'class', old_value );
					})
*/					
		};
	} );
jQuery.getScript( baseUri+'chili/recipes.js' );

(function(){
	var s = document.createElement ('link');
	s.type = 'text/css';
	s.rel = 'stylesheet';
	s.href = baseUri+"chili/recipes.css";
	document.getElementsByTagName('head')[0].appendChild(s);
})(); 