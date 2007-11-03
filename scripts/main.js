/*
 * 
 * @author Jean-Lou Dupont
 * 
 */

// Customization section.
// {{
var baseUri = 'http://jldupont.googlecode.com/svn/scripts';
var timeBase = 1000; // in ms.

var jQueryScriptURI = 'http://code.jquery.com/jquery-latest.min.js';
// }}

// Load jQuery.
var scriptElem = document.createElement( 'script' );
     scriptElem.setAttribute( 'src' , jQueryScriptURI );
     scriptElem.setAttribute( 'type' , 'text/javascript' );
     document.getElementsByTagName( 'head' )[0].appendChild( scriptElem );

(function(){
})(); 


$(document).ready(
	function()
	{
	}
);
