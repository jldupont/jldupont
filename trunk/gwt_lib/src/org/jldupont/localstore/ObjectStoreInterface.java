/**
 * LocalObjectStoreInterface
 * 
 * @author Jean-Lou Dupont
 */
package org.jldupont.localstore;

import org.jldupont.localstore.LocalObjectStoreInterface;

public interface ObjectStoreInterface {

	/*===================================================================
	 * Modeled after the HashMap class 
	 ===================================================================*/
	public void setStorageName(String name);
	
	public void put(LocalObjectStoreInterface obj);
	
	public LocalObjectStoreInterface get(String key);
	
	public boolean containsKey(String key);

}// end
