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
	 * 
	 */
	static int instanceCounter = 0;
	
	/**
	 * 
	 */
	int id = 0;
	
	/**
	 * 
	 */
	boolean callbackFired = false;

	/**
	 * 
	 */
	BaseCallbackEvent target=null;
	
	/*===================================================================
	 * CONSTRUCTORS
	 ===================================================================*/
	public BaseCallback(String classe, String id) {
		super(classe, id);
	}
	
	/*===================================================================
	 * PUBLIC
	 ===================================================================*/
	public void create() {
		
	}
	public void setTarget(BaseCallbackEvent target) {
		this.target = target;
	}
	/*===================================================================
	 * CALLBACK
	 ===================================================================*/
	public void callback(int id, JavaScriptObject obj) {
		this.callbackFired = true;
		Logger.log(this.classe+": callback called! id["+id+"]");
		
		// fire-off the event
		this.target.handleEvent();
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
	
	private String getCallbackName() {
		return "BaseCallbackFnc"+String.valueOf(this.id)+".handler";
	}
	
	/*===================================================================
	 * ObjectPool
	 ===================================================================*/
	public void _clean() {
		
	}
	
}//end class
