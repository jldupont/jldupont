/*
 * 
 * @author Jean-Lou Dupont
 * 
 */

// Customization section.
// {{
var baseUri = 'http://jldupont.googlecode.com/svn/scripts';
var timeBase = 250; // in ms.
// }}

var DOMloaded = false;
var tasks = new Array;

// Grab our timer
jQuery.getScript( baseUri+'/timer/jquery.timer.js',
	function() 
	{ 
		$.timer( timeBase, schedulerTick );
	}
);

schedulerTick = function( timer )
{
	for (task in tasks)
		stop_timer = task.call( this );
		
	if (stop_timer === true)
		timer.stop();
}

// Load Chili Syntax Highlighter
// -----------------------------
var ChiliBook = {};
ChiliBook.recipesLoaded = false;
ChiliBook.loaded = false;

jQuery.getScript( baseUri+'/chili/jquery.chili-1.9.js',
	function() 
	{ 
		ChiliBook.automaticSelector = 'source';
		// don't start without having swapped 
		// the 'lang' attribute for 'class' ones! (see below)
		ChiliBook.loaded = true;
	}
);
(function(){
	var s = document.createElement ('link');
	s.type = 'text/css';
	s.rel = 'stylesheet';
	s.href = baseUri+"/chili/recipes.css";
	document.getElementsByTagName('head')[0].appendChild(s);
})(); 

jQuery.getScript( baseUri+'/chili/recipes.js',
	function()
	{
		ChiliBook.recipesLoaded = true;
	}
);

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

doChili = function()
{
	if (DOMloaded === false)
		return;
		
	if (ChiliBook.recipesLoaded === false)
		return;

	if (ChiliBook.loaded === false)
		return;
	
	$('source').chili();
	
	return true;
}

tasks[0] = doChili;

// END chili initialization

$(document).ready(
	function()
	{
	}
);
