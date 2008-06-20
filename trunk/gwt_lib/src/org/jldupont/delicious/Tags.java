/**
 * @author Jean-Lou Dupont
 *
 */
package org.jldupont.delicious;

import org.jldupont.system.JLD_Object;

public class Tags 
	extends JLD_Object {

	/*===================================================================
	 * CONSTRUCTORS 
	 ===================================================================*/
	public Tags( String id ) {
		super("org.jldupont.delicious.Tags", id );
		setRecyclable();
	}
	
}
