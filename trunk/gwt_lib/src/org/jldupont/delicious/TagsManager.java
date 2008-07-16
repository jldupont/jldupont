/**
 * TagsManager
 * 
 * @author Jean-Lou Dupont
 */
package org.jldupont.delicious;

import org.jldupont.system.JLD_Object;
import org.jldupont.system.Factory;

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
	 * 
	 */
	public void setStorageName(String name) {
		this.name = new String( name );
	}
	
	/**
	 * Returns the tag list for a specified user
	 * + Verifies the localstore
	 * + else performs remote fetch 
	 */
	public TagsList get( String user ) {
	
		TagsList tl = null;
		

		
		return tl;
	}
	/**
	 * Sets a tag list
	 * 
	 * @param user
	 * @param liste
	 * @param expiry
	 */
	public void set( String user, TagsList liste, int expiry ) {
		
	}

	/*===================================================================
	 * PRIVATE INTERFACE 
	 ===================================================================*/
	/**
	 * @param user
	 */
	private TagsList remoteFetch( String user ) {
		
		TagsFetcher tf = (TagsFetcher) Factory.create("org.jldupont.delicious.TagsFetcher");
		
		return null;
	}
	private TagsList localFetch( String user ) {
		
		return null;
	}
	/*===================================================================
	 * PROTECTED 
	 ===================================================================*/
	/**
	 * Recycling
	 */
	public void _clean() {
		super._clean();
	}
	
}//end class