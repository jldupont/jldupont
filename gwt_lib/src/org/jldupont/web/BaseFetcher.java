/**
 * @author Jean-Lou Dupont
 */
package org.jldupont.web;

import java.util.Vector;
import java.util.Iterator;

import org.jldupont.system.JLD_Object;
import org.jldupont.system.Logger;
import org.jldupont.system.Factory;

import com.google.gwt.core.client.JavaScriptObject;
import com.google.gwt.json.client.JSONObject;
import com.google.gwt.user.client.Event;
import com.google.gwt.user.client.Window;

abstract public class BaseFetcher 
	extends JLD_Object 
	implements CallEventListener, BaseCallbackEvent {

	final static int _default_timeout = 3000;
	final static int _default_operationTimeout = 5000;
	
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
	
	/**
	 * Parameter name for the callback field.
	 *  This is service-specific i.e. Delicious has one etc.
	 */
	String callbackParameterName = null;
	
	JSONObject currentJSONObj = null;
	
	/*===================================================================
	 * CONSTRUCTORS 
	 ===================================================================*/
	public BaseFetcher(String classe, String id, boolean recyclable) {
		super(classe,id, recyclable);
		setup();
	}
	private void setup() {
		this.jsonc = (JSONcall)org.jldupont.system.Factory.create("org.jldupont.web.JSONcall","attached_to_BaseFetcher");
		this.jsoncb= (JSONcallback)org.jldupont.system.Factory.create("org.jldupont.web.JSONcallback","attached_to_BaseFetcher");
		this.listeners = new Vector();
		
		this.jsoncb.setTarget(this);
		this.currentJSONObj = null;
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
	/**
	 * fetch
	 *  This is the main method.
	 * @return
	 */
	public boolean fetch() {
	
		//prepare the call
		this.jsonc.setTimeout(this.timeout);
		
		//set callback
		this.jsoncb.create();

		//set callback parameter name
		this.jsonc.addParam(this.callbackParameterName, this.getCallbackFunctionName());
		
		//start operation
		this.startOperation(this.operationTimeout);
		
		//do the call
		this.jsonc.call();
		
		return true;
	}
	/**
	 * @see org.jldupont.web.JSONcallback
	 */
	public String getCallbackFunctionName() {
		return this.jsoncb.getCallbackName();
	}
	/**
	 * 
	 * @param cbName
	 */
	public void setCallbackParameterName(String cbName) {
		this.callbackParameterName = cbName;
	}
	/*===================================================================
	 * BaseCallbackEvent 
	 ===================================================================*/
	/**
	 * This handler is called when the callback is triggered
	 * @see org.jldupont.web.JSONcallback
	 */
	public void handleCallbackEvent(int id, JavaScriptObject obj) {
		
		CallEventObject ceo = new CallEventObject(this, obj);
		this.currentJSONObj = ceo.getJSONObject();
		
		this.timerCancel();
		Logger.log("BaseFetcher::"+this.classe+".handleCallbackEvent: called.");
		this.notifyListeners( ceo );
	}
	
	public JSONObject getJSONObject() {
		return this.currentJSONObj;
	}
	
	/*===================================================================
	 * CallListener 
	 ===================================================================*/
	/**
	 * addCallListener
	 * @param CallListener
	 */
	public void addCallListener(CallListener s) {
		Logger.log(this.classe+".addCallListener: called.");
		this.listeners.add( s );
	}
	/**
	 * removeCallListener
	 * @param CallListener
	 */
	public void removeCallListener(CallListener s) {
		Logger.log(this.classe+".removeCallListener: called.");		
		this.listeners.remove( s );
	}
	
	protected void notifyListeners(CallEventObject obj) {
		
		Iterator it = this.listeners.iterator();
		while (it.hasNext()) {
			Object o = it.next ();
		    ((CallListener) o).fireCallEvent( obj );
		}
		
	}
	/**
	 * Declare here so to help derived classes 
	 */
	public void onBrowserEvent(Event event) {
		
	}
	
	/*===================================================================
	 * Operation related 
	 ===================================================================*/
	
	/**
	 * Resets 'busy' status.
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
		super._clean();
		this.jsonc._clean();
		this.jsoncb._clean();
		this.listeners.clear();
		this.timeout = _default_timeout;
		this.operationTimeout = _default_operationTimeout;
		this.currentJSONObj = null;
	}
}//end class