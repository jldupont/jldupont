/**
 * BaseObjectStore
 * 
 * @author Jean-Lou Dupont
 */
package org.jldupont.localstore;

import org.jldupont.system.JLD_Object;

abstract public class BaseObjectStore 
	extends JLD_Object 
	implements ObjectStoreInterface {
	
	public BaseObjectStore(String classe,String id) {
		super(classe,id);
	}
	
	abstract public boolean exists();
	
	abstract public void setStorageName(String name);
	
	abstract public void put(LocalObjectStoreInterface obj) throws LocalStoreException;
	
	abstract public LocalObjectStoreInterface get(String key) throws LocalStoreException;
	
	abstract public boolean containsKey(String key) throws LocalStoreException;
	
	abstract public int headKey(String key) throws LocalStoreException;
	
	abstract public void clear() throws LocalStoreException;
	

}//end 
