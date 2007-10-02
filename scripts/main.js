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
var ChiliBook;
var DOMloaded = false;

jQuery.getScript( baseUri+'/chili/jquery.chili-1.9.js',
	function() 
	{ 
		ChiliBook.automaticSelector = 'source';
		// don't start without having swapped 
		// the 'lang' attribute for 'class' ones! (see below)

		if (DOMloaded === true)
		{
			alert('recipes loaded ?' + ChiliBook.recipesLoaded );
			ChiliBook.automatic = false;
			$( 'source' ).chili();
		}
	}
);
jQuery.getScript( baseUri+'/chili/recipes.js',
	function()
	{
		ChiliBook.recipesLoaded = true;
	}
);

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

		DOMloaded = true;
	}// document.ready
);

// END chili initialization

$(document).ready(
	function()
	{
	}
);
