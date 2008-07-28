package org.jldupont.rest;

import org.jldupont.system.Liste;
import org.jldupont.system.Recycle;
import org.jldupont.system.Logger;
import org.jldupont.system.IteratorEx;

/**
 * JSONRequest
 * 
 * @author Jean-Lou Dupont
 *
 */
public class JSONRequest 
	extends Liste {

	final static String thisClass = "org.jldupont.rest.JSONRequest";
	
	/*===================================================================
	 * Constructors 
	 ===================================================================*/
	public JSONRequest() {
		super( thisClass, "default_id" );
		setup();
	}

	public JSONRequest(String id) {
		super( thisClass, id );
		setup();
	}
	
	private void setup() {
	}
	
	/*===================================================================
	 * PUBLIC 
	 ===================================================================*/
	
	/**
	 * 
	 * @param key
	 * @param value
	 */
	public void setReqParam(String key, Object value) {
		
	}
	
	/**
	 * 
	 * @param key
	 * @return Object
	 */
	public Object getReqParam(String key) {
		
		return null;
	}
	

	/*===================================================================
	 * Recycle 
	 ===================================================================*/
	public void _clean() {
		super._clean();
	}
	
}//end
