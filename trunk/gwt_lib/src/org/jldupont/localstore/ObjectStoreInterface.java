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
	/**
	 * Returns the availability status of the storage facility
	 *  and *not* a particular instance of storage.
	 */
	public boolean exists();
	
	/**
	 * Used to name the storage instance
	 * 
	 * @param name
	 */
	public void setStorageName(String name);

	/**
	 * Initialize the storage facility for a given
	 *  storage instance. The "name" of the storage
	 *  instance must have been set prior.
	 */
	public void initialize();
	
	/**
	 * Puts 
	 * @param obj
	 */
	public void put(LocalObjectStoreInterface obj);
	
	public LocalObjectStoreInterface get(String key);
	
	public boolean containsKey(String key);

}// end
