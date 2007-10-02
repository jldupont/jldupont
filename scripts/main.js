/*
 * 
 * @author Jean-Lou Dupont
 * 
 */

// Customization section.
// {{
var baseUri = 'http://jldupont.googlecode.com/svn/scripts';
// }}

// Load Chili Syntax Highlighter
// -----------------------------
jQuery.getScript( baseUri+'/chili/jquery.chili.pack.js' );
/*

jQuery.getScript( baseUri+'/chili/jquery.chili.pack.js',
	function(){
		ChiliBook.elementPath = 'source';
		// don't start without having swapped 
		// the 'lang' attribute for 'class' ones! (see below)
		ChiliBook.automatic = false;		
	} 
);
*/
//jQuery.getScript( baseUri+'/chili/recipes.js' );
/*
(function(){
	var s = document.createElement ('link');
	s.type = 'text/css';
	s.rel = 'stylesheet';
	s.href = baseUri+"/chili/recipes.css";
	document.getElementsByTagName('head')[0].appendChild(s);
})(); 

$(document).ready(
	function()
	{
		$("source[lang]").
			each( function()
			{
				a = this.getAttributeNode('lang').nodeValue; 
				this.setAttribute("class", a);

			}
		);

		//alert( ChiliBook );

		//$("source").chili();

	}// document.ready
);
*/
// END chili initialization
