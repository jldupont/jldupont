/**
 * @author Jean-Lou Dupont
 */
package org.jldupont.web;

import java.util.Vector;

import org.jldupont.system.JLD_Object;

import com.google.gwt.core.client.JavaScriptObject;

abstract public class BaseFetcher implements Listener
	extends JLD_Object {

	/**
	 * Call object
	 */
	JSONcall     jsonc;
	/**
	 * Callback object
	 */
	JSONcallback jsoncb;
	
	/**
	 * Timeout for HTTP call
	 */
	int timeout = 3000;
	/**
	 * Operation level timeout
	 */
	int operationTimeout = 5000;
	
	/**
	 * Listeners
	 */
	Vector listeners = null;
	
	
	/*===================================================================
	 * CONSTRUCTORS 
	 ===================================================================*/
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
	/**
	 * Operation level timeout
	 */
	public void setOperationTimeout( int timeout ) {
		this.operationTimeout = timeout;
	}
	/**
	 * Used in the HTTP call made
	 *  from JSONcall
	 */
	public void setTimeout(int timeout) {
		this.timeout = timeout;
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
	
		//prepare the call
		this.jsonc.setTimeout(this.timeout);
		
		//set callback
		this.jsoncb.create();
		
		//start operation
		this.startOperation(this.operationTimeout);
		
		//do the call
		this.jsonc.call();
		
		return true;
	}
	/*===================================================================
	 * Operation related 
	 ===================================================================*/
	
	/**
	 * @see org.jldupont.system.JLD_Object
	 */
	public void timerExpiredEvent() {
		super.timerExpiredEvent();
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