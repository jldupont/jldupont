/**
 * @author Jean-Lou Dupont
 * 
 * @example 
 * 		JSONcallback jscb = new JSONcallback("my_id");
 * 		jscb.setTimeout = 2000;  //from BaseRequest
 * 		jscb.setUrl = "http://del.icio.us/feeds/json/tags/jldupont";
 * 		jscb.addParam( "callback", "some_callback_function" );
 * 
 */
package org.jldupont.web;

import com.google.gwt.user.client.DOM;
import com.google.gwt.user.client.Element;
import org.jldupont.system.Logger;

public class JSONcallback 
	extends BaseRequest {

	final static String thisClass = "org.jldupont.web.JSONcallback";
	
	/**
	 * static counter for tracking usage count
	 */
	static int count = 0;
	
	/**
	 * This instance id
	 *  Derived from static counter
	 */
	int id;
	
	/**
	 * The id used for 
	 *  the script element generated
	 */
	int scriptElementIdCounter = 0;
	
	/**
	 * DOM element
	 */
	Element eScript = null;
	
	/**
	 * The DOM element id
	 *  for the generated script tag
	 */
	String scriptElementId = null;
	
	/*===================================================================
	 * CONSTRUCTORS 
	 ===================================================================*/
	public JSONcallback( String classe, String id ) {
		super(classe,id);
		setup();
	}
	public JSONcallback(String id) {
		super(thisClass, id);
		setup();
	}
	public JSONcallback() {
		super(thisClass,"default_id");
		setup();		
	}
	private void setup() {
		setRecyclable();
		this.id = count++;
	}
	/*===================================================================
	 * PUBLIC 
	 ===================================================================*/
	public int getUniqueId() {
		return this.id;
	}
	
	/*===================================================================
	 * TEMPLATE METHOD pattern 
	 ===================================================================*/
	/**
	 * doFetch
	 * @see org.jldupont.web.BaseRequest#doFetch()
	 */
	protected void doFetch( String complete_url ) {
		
		setupScriptElement( complete_url );
		watchLoadStatus( this.scriptElementId ); // for IE...
	}
	/**
	 * @see org.jldupont.system.JLD_Object#_clean()
	 */
	public void _clean() {
		deleteScriptElement();
	}
	/**
	 * @see org.jldupont.system.JLD_Object#_exId()
	 */
	protected String _exId() {
		return String.valueOf( this.id );
	}
	
	protected void loaded() {
		Logger.log( thisClass+":loaded!");
	}
	
	/*===================================================================
	 * PRIVATE 
	 ===================================================================*/
	/**
	 * setupScriptElement
	 * 
	 * - If the script element already exists on the page, get rid of it.
	 * - Create a new script tag with a new id
	 */
	private void setupScriptElement( String cUrl ) {

		Logger.log(thisClass + ".setupScriptElement");
		
		// get rid of any previous script tag.
		//  This assumes that this object instance was recycled properly of course.
		if ( this.scriptElementId != null ) {
			Logger.log("JSONcallback.setupScriptElement: script tag element exists with id[" + this.scriptElementId + "]" );
			deleteScriptElement();
		}		
		// create a new script tag element
		this.scriptElementId = "JSONcallback" + String.valueOf(this.scriptElementIdCounter++);
		
		Logger.log(thisClass + ".setupScriptElement: *before* injectScript");
		injectScript( this.scriptElementId, cUrl );
		Logger.log(thisClass + ".setupScriptElement: *after* injectScript");		
		
		// hope everything went ok...
		this.eScript = DOM.getElementById( this.scriptElementId );
		if ( this.eScript == null ) {
			String msg = new String( thisClass+".setupScriptElement: ERROR creating tag element with id[" + this.scriptElementId + "]"  );
			Logger.log( msg );
			throw new RuntimeException(msg);
		}
		
	}
	/**
	 * Deletes a script tag element from the wrapper
	 */
	private void deleteScriptElement( ) {
	
		if ( this.eScript != null ) {
			Element parent = DOM.getParent( this.eScript );
			DOM.removeChild( parent, this.eScript );
			Logger.log("JSONcallback.deleteScriptElement: deleted script tag ");
			this.eScript = null;
		}
	}
	

	/*===================================================================
	 * NATIVE methods 
	 ===================================================================*/
	
	private native void injectScript( String script_id, String src ) /*-{
	
		//$wnd.document.write("<script id='"+script_id+"' onload='"+this.@org.jldupont.web.JSONcallback::loadedMozilla()+"' defer src='"+src+"' type='text/javascript'><\/script>");
		//$wnd.document.write("<script id='"+script_id+"' src='"+src+"' type='text/javascript'><\/script>");

		var method = this.@org.jldupont.web.JSONcallback::loadedMozilla();
		var script = $wnd.document.createElement("script");
		script.setAttribute("src", src);
		script.setAttribute("id", script_id);
		script.setAttribute("type", "text/javascript");
		script.setAttribute("onload", method);
       
		$wnd.document.getElementsByTagName("head")[0].appendChild(script);
		
	}-*/;
	
	private native void watchLoadStatus(String script_id) /*-{
	
		var script = $wnd.document.getElementById( script_id );
		
		script.onreadystatechange = function() {
			if (this.readyState == "complete")
				this.@org.jldupont.web.JSONcallback::loadedIE(); // call the onload handler
		};
		
	}-*/;
	
	private void loadedMozilla() {
		loaded();
	}
	private void loadedIE() {
		loaded();
	}
	
}//end class
