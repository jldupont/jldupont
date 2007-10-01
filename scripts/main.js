/*
 * 
 * @author Jean-Lou Dupont
 * 
 */

var baseUri = 'http://jldupont.googlecode.com/svn/scripts/';

// Chili Syntax Highlighter
jQuery.getScript( baseUri+'chili/jquery.chili.pack.js' );
jQuery.getScript( baseUri+'chili/recipes.js' );

(function(){
var s = document.createElement ('link');
s.type = 'text/css';
s.rel = 'stylesheet';
s.href = baseUri+"chili/recipes.css";
document.getElementsByTagName('head')[0].appendChild(s);
})(); 