/**
 * TagsManager
 * 
 * @author Jean-Lou Dupont
 */
package org.jldupont.delicious;

import org.jldupont.system.JLD_Object;
import org.jldupont.system.Factory;
import org.jldupont.localstore.LocalObjectStore;
import org.jldupont.localstore.LocalStoreException;
import org.jldupont.localstore.LocalObjectStoreInterface;

public class TagsManager 
	extends JLD_Object {

	/**
	 * Storage name
	 */
	String name = null;
	
	final static String thisClass = "org.jldupont.delicious.TagsManager";
	
	/*===================================================================
	 * CONSTRUCTORS 
	 ===================================================================*/
	public TagsManager() {
		super( thisClass, "default_id", true );
	}
	
	public TagsManager( String classe, String id, boolean recyclable ) {
		super( classe, id, recyclable );
	}

	/*===================================================================
	 * PUBLIC INTERFACE 
	 ===================================================================*/
	/**
	 * setStorageName
	 * 
	 * @param name String
	 */
	public void setStorageName(String name) {
		this.name = new String( name );
	}
	
	/**
	 * Returns the tag list for a specified user
	 * + Verifies the localstore
	 * + else performs remote fetch
	 * 
	 *  @return TagsList or NULL
	 */
	public TagsList get( String user ) {
	
		// try the local copy
		TagsList tl = this.localFetch(user);
		if ( tl != null )
			return tl;
		
		return this.remoteFetch(user);
	}
	/**
	 * Sets a tag list
	 * 
	 * @param user
	 * @param liste
	 * @param timestamp
	 */
	public void set( String user, TagsList liste, int timestamp ) {
		
	}

	/*===================================================================
	 * PRIVATE INTERFACE 
	 ===================================================================*/
	/**
	 * @param user
	 */
	private TagsList remoteFetch( String user ) {
		
		TagsFetcher tf = (TagsFetcher) Factory.create("org.jldupont.delicious.TagsFetcher");

		tf.setUser(user);
		
		try {

		} catch(RuntimeException e) {
			
		} finally {
			tf.recycle();
		}
		
		return null;
	}
	/**
	 * localFetch
	 * 
	 * @param user
	 * @return TagsList or NULL
	 */
	private TagsList localFetch( String user ) {
		
		LocalObjectStore store = (LocalObjectStore) Factory.create("org.jldupont.delicious.LocalObjectStore");
		LocalObjectStoreInterface obj = null;
		
		store.setStorageName(this.name);
		
		try {
			obj = store.get( this.generateKey(user) );
		} catch (LocalStoreException e) {
			return null;
		} finally {
			store.recycle();			
		}
		
		return (TagsList) obj;
	}
	/*===================================================================
	 * PROTECTED 
	 ===================================================================*/
	
	protected String generateKey( String user ) {
		
		return new String( this.name + '/' + user );
	}
	
	/**
	 * Recycling
	 */
	public void _clean() {
		super._clean();
	}
	
}//end class