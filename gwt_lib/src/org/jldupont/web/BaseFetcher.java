/**
 * @author Jean-Lou Dupont
 */
package org.jldupont.web;

import org.jldupont.system.JLD_Object;

import com.google.gwt.core.client.JavaScriptObject;

abstract public class BaseFetcher 
	extends JLD_Object {

	/**
	 * 
	 */
	JSONcall     jsonc;
	/**
	 * 
	 */
	JSONcallback jsoncb;
	
	/**
	 * Timeout
	 */
	int timeout = 3000;
	
	public BaseFetcher(String classe, String id) {
		super(classe,id);
		setup();
	}
	private void setup() {
		this.jsonc = new JSONcall();
		this.jsoncb= new JSONcallback();
	}
	/*===================================================================
	 * PUBLIC 
	 ===================================================================*/
	public void setTimeout() {
		this.jsoncb.setTimeout();
	}
	/**
	 * @see org.jldupont.web.BaseCall#setUrl(String)
	 */
	public void setUrl(String url) {
		this.jsonc.setUrl(url);
	}
	/**
	 * @see org.jldupont.web.BaseCall#addParam(String, String)
	 */
	public void addParam(String key, String value) {
		this.jsonc.addParam(key, value);
	}
	
	public boolean fetch() {
	
		//set callback
		
		//start operation
		this.startOperation(timeout);
		
		return true;
	}
	
	/*===================================================================
	 * ObjectPool related 
	 ===================================================================*/
	/**
	 * @see org.jldupont.system.ObjectPool 
	 */
	public void _clean() {
		this.jsonc._clean();
		this.jsoncb._clean();
	}
}//end class
