/**
 * Factory for the org.jldupont.localstore package
 * 
 * @author Jean-Lou Dupont
 */
package org.jldupont.localstore;

import org.jldupont.system.JLD_Object;
import org.jldupont.system.Logger;
import org.jldupont.system.ObjectPool;

public class Factory 
	extends	Object {

	/**
	 * create
	 * 
	 * @param className
	 * @return
	 */
	public static JLD_Object create( String className ) {
		return create( className, null );
	}
	
	/**
	 * create
	 * 
	 * @param className
	 * @return JLD_Object
	 */
	public static JLD_Object create( String className, String id ) {

		ObjectPool pool = new ObjectPool();
		JLD_Object obj;
		String rid = null;
		
		// check the ObjectPool first
		obj = pool.get( className );
		if ( obj != null ) {
			rid = obj.getId();
			Logger.log( "FACTORY: retrieved object of class: " + className + " id("+rid+")" +" asked id("+id+")" );
			
			// clean-up!
			obj._clean();
			
			return obj;
		}
		
		// no luck, create one from scratch
		Logger.log( "FACTORY: creating object of class: " + className );		
		
		return createInstance( className, id );
	}
	
	/**
	 * createInstance
	 * 
	 * TODO implement this a better way!! 
	 * @param className
	 * @return
	 */
	protected static JLD_Object createInstance( String className, String id ) {
	
		// =======================
		// org.jldupont.localstore
		// =======================
		if ( className == "org.jldupont.delicious.LocalObjectStore" ) {
			return (JLD_Object) new org.jldupont.localstore.LocalObjectStore(id);
		}
			
		Logger.log( "FACTORY: ERROR CREATING INSTANCE OF CLASS: " + className );
		
		return null;
	}
	
	
}//end
