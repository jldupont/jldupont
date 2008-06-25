/**
 * @author Jean-Lou Dupont
 */
package org.jldupont.web;

import java.util.Vector;
import java.util.Iterator;

import org.jldupont.system.JLD_Object;
import org.jldupont.system.Logger;

import com.google.gwt.core.client.JavaScriptObject;
import com.google.gwt.user.client.Event;

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
	
	
	/*===================================================================
	 * CONSTRUCTORS 
	 ===================================================================*/
	public BaseFetcher(String classe, String id, boolean recyclable) {
		super(classe,id, recyclable);
		setup();
	}
	private void setup() {
		this.jsonc = new JSONcall();
		this.jsoncb= new JSONcallback();
		this.listeners = new Vector();
		
		this.jsoncb.setTarget(this);
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
	 * BaseCallbackEvent 
	 ===================================================================*/
	/**
	 * This handler is called when the callback is triggered
	 * @see org.jldupont.web.JSONcallback
	 */
	public void handleCallbackEvent() {
		Logger.log(this.classe+".handleCallbackEvent: called.");
		this.notifyListeners();
	}
	/*===================================================================
	 * CallListener 
	 ===================================================================*/
	
	public void addCallListener(CallListener s) {
		this.listeners.add( s );
	}
	
	public void removeCallListener(CallListener s) {
		this.listeners.remove( s );
	}
	
	protected void notifyListeners() {
		
		Iterator it = this.listeners.iterator();
		while (it.hasNext()) {
			Object o = it.next ();
		    ((CallListener) o).fireCallEvent( new CallEventObject(this));
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
		
	}
}//end class