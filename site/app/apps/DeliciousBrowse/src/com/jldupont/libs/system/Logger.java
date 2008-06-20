/**
 * @author Jean-Lou Dupont
 *
 */
package com.jldupont.libs.system;

public class Logger {

	public static void log( String msg ) {
		
		if ( isAvailable() == false )
			return;
		
		logToFirebug( msg );
	}
	
	/**
	 * Returns the availability status
	 * of Firebug console
	 * 
	 * @return boolean
	 */
	protected static native boolean isAvailable() /*-{
	
		return ( typeof console.log != "undefined" );
		
	}-*/;
	
	protected static native void logToFirebug( String msg ) /*-{
	
		console.log( msg );
		
	}-*/;
}
