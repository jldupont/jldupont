/**
 * @author Jean-Lou Dupont
 */
package org.jldupont.web;

import java.util.EventObject;
import com.google.gwt.core.client.JavaScriptObject;
import com.google.gwt.json.client.JSONObject;


public class CallEventObject 
	extends EventObject {

	JavaScriptObject jsObj = null;

	JSONObject jsonObj;
	
	public CallEventObject(Object source, JavaScriptObject obj) {
		super(source);
		this.jsObj = obj;
		this.jsonObj = new JSONObject( obj );
	}
	/**
	 * getJSONObject
	 * @return JSONObject
	 */
	public JSONObject getJSONObject() {
		return this.jsonObj;
	}
	/**
	 * getJSObject
	 * @return
	 */
	public JavaScriptObject getJSObject() {
		return this.jsObj;
	}
}//end
