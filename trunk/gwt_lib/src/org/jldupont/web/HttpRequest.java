/**
 * @author Jean-Lou Dupont
 */
package org.jldupont.web;

import org.jldupont.system.JLD_Object;

/**
 * HttpRequest
 *
 * Handles both origin and !origin fetches
 * 
 * Origin based:   XHR
 * !Origin based:  iframe
 * 
 */
public class HttpRequest 
	extends JLD_Object {

	public HttpRequest(String id) {
		super("org.jldupont.web.HttpRequest", id );
		setRecyclable();
	}
	
	/**
	 * Fetches the specified resource
	 * 
	 * @return boolean
	 */
	public boolean fetch(String url ) {
	
		return false;
	}
	
	
}//endclass
