/**
 * @author Jean-Lou Dupont
 *
 */
package com.jldupont.services.Delicious;

import com.jldupont.libs.system.JLD_Object;

public class Tags 
	extends JLD_Object {

	/*===================================================================
	 * CONSTRUCTORS 
	 ===================================================================*/
	public Tags( String id ) {
		super("com.jldupont.services.Delicious.Tags", id );
		setRecyclable();
	}
	
}
