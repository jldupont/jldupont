/**
 * LocalObjectStore
 * 
 * @author Jean-Lou Dupont
 * 
 *  Uses the most "appropriate" local storage.
 *  Works with GoogleGears
 */
package org.jldupont.localstore;

import org.jldupont.system.JLD_Object;

public class LocalObjectStore 
	extends JLD_Object 
	implements ObjectStoreInterface {
	
	final static String thisClass = "org.jldupont.localstore.LocalObjectStore";
	
	/*===================================================================
	 * CONSTRUCTORS 
	 ===================================================================*/
	public LocalObjectStore(String classe, String id) {
		super(classe,id);
		setup();
	}
	/**
	 * setup
	 */
	private void setup() {
		
	}
	
	/*===================================================================
	 * PUBLIC
	 *  Modeled after the HashMap class 
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
	
}//end class
