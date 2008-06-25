/**
 * @author Jean-Lou Dupont
 */
package org.jldupont.web;

import com.google.gwt.core.client.JavaScriptObject;

import org.jldupont.system.JLD_Object;
import org.jldupont.system.Logger;

public class BaseCallback 
	extends JLD_Object {

	/**
	 * Instance Counter
	 */
	static int instanceCounter = 0;
	
	/**
	 * 
	 */
	boolean callbackFired = false;

	/**
	 * 
	 */
	BaseCallbackEvent target=null;
	
	/**
	 * 
	 */
	int currentCallback = -1;
	
	/*===================================================================
	 * CONSTRUCTORS
	 ===================================================================*/
	public BaseCallback(String classe, String id) {
		super(classe, id);
		setup();
	}
	private void setup() {
		_clean();
	}
	/*===================================================================
	 * PUBLIC
	 ===================================================================*/
	/**
	 * create
	 * @return void
	 */
	public void create() {

		if ( this.target == null ) {
			throw new RuntimeException( this.classe + ".create: target is null" );
		}
		
		if (this.currentCallback > 0) {
			deleteCallback( this.currentCallback );
		}
		
		this.callbackFired = false;
		this.currentCallback = instanceCounter++;
		createCallback( this.currentCallback );
	}
	/**
	 * 
	 * @param target
	 */
	public void setTarget(BaseCallbackEvent target) {
		this.target = target;
	}
	/**
	 * 
	 * @return String
	 */
	private String getCallbackName() {
		return "BaseCallbackFnc"+String.valueOf(this.currentCallback)+".handler";
	}
	/*===================================================================
	 * CALLBACK
	 ===================================================================*/
	public void callback(int id, JavaScriptObject obj) {
		
		this.callbackFired = true;
		Logger.log(this.classe+": callback called! id["+id+"]");
		
		// fire-off the event
		this.target.handleCallbackEvent();
	}
	/**
	 * BLACK MAGIC at work!!!
	 */
	protected native void createCallback(int id) /*-{

		var fncName = "BaseCallbackFnc"+id;
		eval( "var obj = $wnd."+fncName+" = { id: '" + id + "' };"	);
		obj.handler = function(jsonobj) {
			this.@org.jldupont.web.BaseCallback::callback(ILcom/google/gwt/core/client/JavaScriptObject;)(this.id, jsonobj);
		};
		
	}-*/;
	/**
	 * Deletes a callback
	 */
	protected native void deleteCallback(int id) /*-{
		var fncName = "BaseCallbackFnc"+id;	
		eval( "$wnd."+fncName+" = null;" );
	}-*/;
	
	/*===================================================================
	 * ObjectPool
	 ===================================================================*/
	public void _clean() {
		
		super._clean();
		
		if (this.currentCallback > 0) {
			deleteCallback( this.currentCallback );
		}
		this.currentCallback = -1;
		this.callbackFired = false;
		this.target = null;
	}
	
}//end class
