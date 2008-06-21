/**
 * @author Jean-Lou Dupont
 *
 */
package org.jldupont.delicious;

import org.jldupont.system.JLD_Object;

public class Tags 
	extends JLD_Object {

	/**
	 * Delicious end-point 
	 */
	static String feedJSON = "";
	
	/*===================================================================
	 * CONSTRUCTORS 
	 ===================================================================*/
	public Tags( String id ) {
		super("org.jldupont.delicious.Tags", id );
		setRecyclable();
	}
	
	
	
}//end class
