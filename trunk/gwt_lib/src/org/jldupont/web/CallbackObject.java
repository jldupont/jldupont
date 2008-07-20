/**
 * CallbackObject
 * 
 * @author Jean-Lou Dupont
 */
package org.jldupont.web;

import org.jldupont.system.JLD_Object;

public class CallbackObject 
	extends JLD_Object {

	final static String thisClass = "org.jldupont.web.CallbackObject";
	
	
	/*===================================================================
	 * CONSTRUCTORS 
	 ===================================================================*/

	public CallbackObject() {
		super( thisClass, "default_id", true );
		setup();		
	}
	public CallbackObject(String id) {
		super( thisClass, id, true );
		setup();
	}
	
	private void setup() {
		
	}

	/*===================================================================
	 * PUBLIC INTERFACE
	 * 
	 *  CommandStatus
	 ===================================================================*/


	
	
}//end
