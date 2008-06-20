/**
 * @author Jean-Lou Dupont
 */
package com.jldupont.libs.system;

import com.jldupont.services.Delicious.Tags;

import java.lang.Object;

public class Factory 
	extends Object {

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
	
		/**
		 * @see com.jldupont.system.ObjectPool
		 */
		if ( className == "ObjectPool" ) {
			return (JLD_Object) new ObjectPool();
		}
		/**
		 * @see com.jldupont.services.Delicious.Tags
		 */
		if ( className == "Delicious.Tags" ) {
			return (JLD_Object) new Tags( id );
		}
		
		Logger.log( "FACTORY: ERROR CREATING INSTANCE OF CLASS: " + className );
		
		return null;
	}
	
}
