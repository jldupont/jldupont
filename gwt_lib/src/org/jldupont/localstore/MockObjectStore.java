/**
 * MockObjectStore
 *  Used when no other appropriate local database is available
 *  
 * @author Jean-Lou Dupont
 */
package org.jldupont.localstore;

import org.jldupont.system.JLD_Object;

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
	 * not much todo :-)
	 */
	public void initialize() {
		
	}
	public void setStorageName(String name) {
		
	}
	
	public void put(LocalObjectStoreInterface obj) {
		
	}
	
	public LocalObjectStoreInterface get(String key) {
		
		return null;
	}
	
	public int headKey(String key) {
		
		return 0;
	}
	
	public boolean containsKey(String key) {
	
		return false;
	}
	
	public void clear() {
		
	}
	
}//end 
