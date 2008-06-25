/**
 * Liste
 *  Generic list class
 *  
 * @author Jean-Lou Dupont
 */

package org.jldupont.system;

import org.jldupont.system.JLD_Object;

import java.util.HashMap;

public class Liste 
	extends JLD_Object {

	final static String thisClass = "org.jldupont.system.Liste";

	/**
	 * Main object 
	 */
	HashMap liste = null;
	
	/*===================================================================
	 * CONSTRUCTORS 
	 ===================================================================*/
	public Liste(String classe, String id) {
		super(classe,id);
		setup();
	}
	public Liste(String id) {
		super(thisClass, id);
		setup();
	}
	private void setup() {
		this.liste = new HashMap();
	}
	/*===================================================================
	 * PUBLIC 
	 *  Modeled after the HashMap class
	 ===================================================================*/
	public boolean isEmpty() {
		return this.liste.isEmpty();
	}
	/**
	 * containsKey
	 */
	public boolean containsKey(String key) {
		return this.liste.containsKey(key);
	}
	/**
	 * Puts a tag in the list
	 * @param key
	 * @param count
	 */
	public void put(String key, Object value) {
		this.liste.put(key, value);
	}
	/**
	 * Removes an entry from the list
	 * @param key
	 * @return
	 */
	public Object remove(String key) {
		return this.liste.remove(key);
	}
	/**
	 * toString
	 * @return String
	 */
	public String toString() {
		return this.liste.toString();
	}
	/*===================================================================
	 * ObjectPool
	 *  (recycling) 
	 ===================================================================*/
	public void _clean() {
		super._clean();
		liste.clear();
	}
	
}//end class
