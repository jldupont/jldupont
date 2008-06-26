/**
 * MockObjectStore
 *  Used when no other appropriate local database is available
 *  
 * @author Jean-Lou Dupont
 */
package org.jldupont.localstore;

import org.jldupont.system.Logger;

public class MockObjectStore 
	extends BaseObjectStore 
	implements ObjectStoreInterface {
	
	final static String thisClass = "org.jldupont.localstore.MockObjectStore";

	/**==================================================================
	 * CONSTRUCTORS 
	 ===================================================================*/
	
	public MockObjectStore(String classe, String id) {
		super(classe,id);
	}
	public MockObjectStore(String id) {
		super(thisClass,id);
	}
	public MockObjectStore() {
		super(thisClass,"default_id");
	}
	
	/**==================================================================
	 * @see org.jldupont.localstore.ObjectStoreInterface 
	 ===================================================================*/
	public boolean exists() {
		return true;
	}
	/**
	 * @see org.jldupont.localstore.ObjectStoreInterface#isPersistent()
	 */
	public boolean isPersistent() {
		return false;
	}
	/**
	 * not much todo :-)
	 */
	public void initialize() {
		Logger.log(thisClass+".initialize: called");
	}
	public void setStorageName(String name) {
		Logger.log(thisClass+".setStorageName: called");		
	}
	
	public void put(LocalObjectStoreInterface obj) {
		Logger.log(thisClass+".put: called");		
	}
	
	public LocalObjectStoreInterface get(String key) {
		Logger.log(thisClass+".get: called");		
		return null;
	}
	
	public int headKey(String key) {
		Logger.log(thisClass+".headKey: called");		
		return -1;
	}
	
	public boolean containsKey(String key) {
		Logger.log(thisClass+".containsKey: called");	
		return false;
	}
	
	public void clear() {
		Logger.log(thisClass+".clear: called");		
	}
	
}//end 
