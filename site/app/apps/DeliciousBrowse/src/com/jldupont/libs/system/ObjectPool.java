/**
 * 
 */
package com.jldupont.libs.system;

import java.util.HashMap;

/**
 * @author Jean-Lou Dupont
 *
 */
public class ObjectPool 
	extends JLD_Object {

	static HashMap bin = null;
	
	/*===================================================================
	 * CONSTRUCTORS 
	 ===================================================================*/
	/**
	 * Borg pattern
	 */
	ObjectPool() {
		super( "ObjectPool" );
		
		if ( bin == null )
			bin = new HashMap();
	}
	
	/**
	 * 
	 * @param obj
	 * @return void
	 */
	public void recycle( JLD_Object obj ) {
		
		classe = obj.getClasse();
		
		// do we already have an object of this class?
		if ( bin.containsKey(classe) )
			return;
		
		bin.put( classe, obj );
	}
	
	public JLD_Object get( String classe ) {
		
		JLD_Object obj;
		
		if ( bin.containsKey(classe) ) {
			// get it
			obj = (JLD_Object) bin.get( classe );
			
			// remove from bin
			bin.remove( classe );
			
			return obj;
		}
		
		return null;
	}
	
}//endclass
