/**
 * StdListe
 *  Standard list class
 *  
 * @author Jean-Lou Dupont
 */
package org.jldupont.system;

import org.jldupont.system.JLD_Object;

import java.util.HashMap;

public class StdListe 
	extends JLD_Object {

	final static String thisClass = "org.jldupont.command.StdListe";
	
	HashMap liste = null;
	
	/*===================================================================
	 * CONSTRUCTORS  
	 ===================================================================*/
	
	public StdListe(String classe, String id ) {
		super( classe, id, true );
		setup();		
	}
	
	public StdListe( String id ) {
		super( thisClass, id, true );
		setup();
	}
	
	private void setup() {
	
		this.liste = new HashMap();
	}
	
	/*===================================================================
	 * PUBLIC  
	 ===================================================================*/
	public boolean isEmpty() {
		return this.liste.size()!=0;
	}
	/**
	 * containsKey
	 */
	public boolean containsKey(String key) {
		return this.liste.containsKey(key);
	}
	
	/**
	 * Getter
	 * @param key
	 * @return
	 */
	public Object get(String key) {
		return this.liste.get(key);
	}
	/**
	 * Setter
	 * @param key
	 * @param value
	 * @return void 
	 */
	public void put(String key, Object value) {
		this.liste.put(key, value);
	}
	/**
	 * Clear
	 * @return void
	 */
	public void clear() {
		this.liste.clear();
	}
	/**
	 * Remove
	 * 
	 * @param key
	 */
	public void remove(String key) {
		this.liste.remove(key);
	}
	
	/*===================================================================
	 * RECYCLING  
	 ===================================================================*/
	public void _clean() {
		super._clean();
		
		this.liste.clear();
		
	}
	
}//endclass
