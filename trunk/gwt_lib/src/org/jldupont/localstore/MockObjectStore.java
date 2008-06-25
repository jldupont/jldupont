/**
 * MockObjectStore
 *  Used when no other appropriate local database is available
 *  
 * @author Jean-Lou Dupont
 */
package org.jldupont.localstore;

import org.jldupont.system.JLD_Object;

public class MockObjectStore 
	extends JLD_Object 
	implements ObjectStoreInterface {
	

	/**==================================================================
	 * @see org.jldupont.localstore.ObjectStoreInterface 
	 ===================================================================*/
	public void setStorageName(String name) {
		
	}
	
	public void put(LocalObjectStoreInterface obj) {
		
	}
	
	public LocalObjectStoreInterface get(String key) {
		
		return null;
	}
	
	public boolean containsKey(String key) {
	
		return false;
	}
	
}//end 
