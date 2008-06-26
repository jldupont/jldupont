/**
 * GearsObjectStore
 *  Uses GoogleGears database functionality to store objects 
 *  through a 'BLOB' representation
 * 
 * @author Jean-Lou Dupont
 * 
 */
package org.jldupont.localstore;

import org.jldupont.system.JLD_Object;

public class GearsObjectStore 
	extends BaseObjectStore 
	implements ObjectStoreInterface {

	final static String thisClass = "org.jldupont.localstore.GearsObjectStore";
	
	String storageName = null;
	
	/*===================================================================
	 * CONSTRUCTORS 
	 ===================================================================*/
	public GearsObjectStore(String classe, String id) {
		super(classe,id);
		setup();
	}
	public GearsObjectStore(String id) {
		super(thisClass,id);
		setup();
	}
	public GearsObjectStore() {
		super(thisClass,"default_id");
		setup();
	}
	private void setup() {
		
	}
	
	/*===================================================================
	 * ObjectStoreInterface 
	 ===================================================================*/
	public boolean exists() {
		
		return false;
	}
	
	public void initialize() {
		
	}
	public void setStorageName(String name) {
		this.storageName = new String( name );
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
	
}//end class
