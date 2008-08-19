/**
 * Time
 * @author Jean-Lou Dupont
 */
package org.jldupont.system;

public class Time {

	public static native long getTime() /*-{
		var currentTime = new Date();
		return currentTime.getTime();
	}-*/;

	/**
	 * Converts any number of date formats to
	 * long integer since 1/1/1970
	 * 
	 * @param input String
	 * @return
	 */
	public static native long parse(String input) /*-{
		return Date.parse( input );
	}-*/;
	
	public static native long getRFC1123Time(long ts) /*-{
		return Date.toUTCString( ts );
	}-*/;
	
	
}//end
