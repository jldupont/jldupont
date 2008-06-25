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
	extends JLD_Object 
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
	private void setup() {
		
	}
	
	/*===================================================================
	 * ObjectStoreInterface 
	 ===================================================================*/
	public void setStorageName(String name) {
		this.storageName = new String( name );
	}
	
	public void put(LocalObjectStoreInterface obj) {
		
	}
	
	public LocalObjectStoreInterface get(String key) {
		
		return null;
	}
	
	public boolean containsKey(String key) {
		
		return false;
	}
	
}//end class
