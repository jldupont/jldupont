/*
 * static_class.js
 * 
 * Example definition of a static class in Javascript.
 * 
 * @author Jean-Lou Dupont
 * http://jldupont.com
 */

	// Function declaration
	//  Serves as "class" declaration
	JLD = function() {

		// static variable		
		var var1 = 666;

	}
	// Static Function declaration
	//  under the "class" JLD
	JLD.fnc1 = function() {
		
		// can't access var1 inside function JLD
		alert( "JLD.fnc1 called. var1= " + JLD.var1 );
	}
	
	// 'field' of JLD
	JLD.var2 = 777;
	
	// Static Function declaration
	//  under the "class" JLD
	JLD.fnc2 = function() {
		
		// can access var2 though
		alert( "JLD.fnc2 called. var2= " + JLD.var2 );
	}
	
