/**
 * @author Jean-Lou Dupont
 */
package org.jldupont.system;

import org.jldupont.delicious.TagsFetcher;
import org.jldupont.browser.URLParamsList;
import org.jldupont.browser.CookieParamsList;
import org.jldupont.web.JSONcallback;
import org.jldupont.web.JSONcall;
import org.jldupont.delicious.TagsList;
import org.jldupont.localstore.LocalObjectStore;

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

		// org.jldupont.system
		// ===================
		if ( className == "org.jldupont.system.StdListe" ) {
			return (JLD_Object) new StdListe(id);
		}
	
		/**
		 * @see com.jldupont.system.ObjectPool
		 */
		if ( className == "ObjectPool" ) {
			return (JLD_Object) new ObjectPool();
		}
		
		// org.jldupont.command
		// ===================
		
		
		// org.jldupont.browser
		// =======================
		/**
		 * @see org.jldupont.browser.URLParamsList
		 */
		if ( className == "org.jldupont.browser.URLParamsList" ) {
			return (JLD_Object) new URLParamsList( );
		}
		/**
		 * @see org.jldupont.browser.CookieParamsList
		 */
		if ( className == "org.jldupont.browser.CookieParamsList" ) {
			return (JLD_Object) new CookieParamsList( );
		}
		// org.jldupont.web
		// =======================
		if ( className == "org.jldupont.web.JSONcall") {
			return (JLD_Object) new org.jldupont.web.JSONcall(id);
		}
		if ( className == "org.jldupont.web.JSONcallback") {
			return (JLD_Object) new org.jldupont.web.JSONcallback(id);
		}
		// org.jldupont.delicious
		// =======================
		/**
		 * @see org.jldupont.delicious.TagsFetcher
		 */
		if ( className == "org.jldupont.delicious.TagsFetcher" ) {
			return (JLD_Object) new TagsFetcher( id );
		}
		if ( className == "org.jldupont.delicious.TagsList" ) {
			return (JLD_Object) new org.jldupont.delicious.TagsList(id);
		}
		// org.jldupont.localstore
		// =======================
		if ( className == "org.jldupont.delicious.LocalObjectStore" ) {
			return (JLD_Object) new org.jldupont.localstore.LocalObjectStore(id);
		}
		
			
		Logger.log( "FACTORY: ERROR CREATING INSTANCE OF CLASS: " + className );
		
		return null;
	}
	
}
