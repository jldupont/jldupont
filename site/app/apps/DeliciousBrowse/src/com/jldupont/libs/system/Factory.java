/**
 * @author Jean-Lou Dupont
 */
package com.jldupont.libs.system;

import java.lang.Object;

public class Factory 
	extends Object {

	/**
	 * create
	 * 
	 * @param className
	 * @return JLD_Object
	 */
	public static JLD_Object create( String className ) {

		ObjectPool pool = new ObjectPool();
		JLD_Object obj;
		
		// check the ObjectPool first
		obj = pool.get( className );
		if ( obj != null ) {
			
			Logger.log( "FACTORY: retrieved object of class: " + className );
			return obj;
		}
		
		// no luck, create one from scratch
		Logger.log( "FACTORY: creating object of class: " + className );		
		
		return createInstance( className );
	}
	
	/**
	 * createInstance
	 * 
	 * TODO implement this a better way!! 
	 * @param className
	 * @return
	 */
	protected static JLD_Object createInstance( String className ) {
	
		if ( className =="ObjectPool" ) {
			return (JLD_Object) new ObjectPool();
		}
		
		return null;
	}
	
}
