/**
 * @author Jean-Lou Dupont
 */
package org.jldupont.widget;

import org.jldupont.system.Logger;

public class GoogleGears 
	extends ImgAnchorLink {

	final static String installed ="gears_logo.gif";
	final static String not_installed ="gears_logo_grey.gif";
	
	public GoogleGears() {
		super();
		setup();
	}
	
	private void setup() {
		boolean status = isGearsInstalled();
		Logger.log("Gears: " + status );
		String imgUrl = status ? installed:not_installed;
		this.setImgUrl(imgUrl);
	}
	
	private static native boolean isGearsInstalled() /*-{
		try {
			return $wnd.google.gears.factory != null;
		} catch (e) {
			return false;
		}
	}-*/;
	
}//end
