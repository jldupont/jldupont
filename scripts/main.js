/*
 * 
 * @author Jean-Lou Dupont
 * 
 */

// Customization section.
// {{
var baseUri = 'http://jldupont.googlecode.com/svn/scripts/';

var scripts = new Array(
	'http://o.aolcdn.com/dojo/0.9.0/dojo/dojo.xd.js',
	'http://code.jquery.com/jquery-latest.pack.js'
);
// }}

(function(){
	for (script in scripts)
	{
		var s = document.createElement ('link');
		s.type = 'text/css';
		s.rel = 'stylesheet';
		s.href = script;
		document.getElementsByTagName('head')[0].appendChild(s);
	}
})();

// Chili Syntax Highlighter
// ------------------------
jQuery.getScript( baseUri+'chili/jquery.chili.pack.js' );
jQuery.getScript( baseUri+'chili/recipes.js' );

(function(){
	var s = document.createElement ('link');
	s.type = 'text/css';
	s.rel = 'stylesheet';
	s.href = baseUri+"chili/recipes.css";
	document.getElementsByTagName('head')[0].appendChild(s);
})(); 