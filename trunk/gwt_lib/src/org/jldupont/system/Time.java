/**
 * Time
 * @author Jean-Lou Dupont
 */
package org.jldupont.system;

public class Time {

	public static native int getTime() /*-{
		var currentTime = new Date();
		return currentTime.getTime();
	}-*/;

	
}//end
