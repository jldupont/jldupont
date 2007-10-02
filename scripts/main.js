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
		arr = $("source[lang]");
		alert( "Element?"+(arr instanceof Element) );
		alert( "Array?"+(arr instanceof Array) );		
		
		function dump(arr,level) 
		{
			var dumped_text = "";
			if(!level) level = 0;
			
			//The padding given at the beginning of the line.
			var level_padding = "";
			for(var j=0;j<level+1;j++) level_padding += "    ";
			
			if(typeof(arr) == 'object') { //Array/Hashes/Objects
			 for(var item in arr) {
			  var value = arr[item];
			 
			  if(typeof(value) == 'object') { //If it is an array,
			   dumped_text += level_padding + "'" + item + "' ...\n";
			   dumped_text += dump(value,level+1);
			  } else {
			   dumped_text += level_padding + "'" + item + "' => \"" + value + "\"\n";
			  }
			 }
			} else { //Stings/Chars/Numbers etc.
			 dumped_text = "===>"+arr+"<===("+typeof(arr)+")";
			}
			return dumped_text;
		} 
		
		
//		alert( var_dump( arr ) );
//		alert( "is array?"+arr instanceof Array );
		
		for (el in arr )
		{
			alert( dump( el ) );
			
			a = el.getAttributeNode('lang').nodeValue; 
			el.setAttribute("class", a);
		}
		
		ChiliBook.chili();
	}
);