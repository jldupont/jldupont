/**
 * StdListe
 *  Standard list class
 *  
 * @author Jean-Lou Dupont
 */
package org.jldupont.system;

import org.jldupont.system.JLD_Object;
import org.jldupont.system.IteratorEx;

import java.util.HashMap;
import java.util.Set;
import java.util.Iterator;

public class StdListe 
	extends JLD_Object 
	implements IteratorEx {

	final static String thisClass = "org.jldupont.command.StdListe";
	
	HashMap liste = null;
	
	Set keys = null;
	
	Iterator keysIterator = null;
	
	int index = -1;
	
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
	 * Iterator interface  
	 ===================================================================*/
	
	public boolean hasNext() {
		
		return this.keysIterator.hasNext();
	}
	public Object next() {
		
		String key = (String) this.keysIterator.next();
		Object value = this.liste.get(key);
		
		return value;
	}
	public void remove() {
		//NOOP
	}
	/**
	 * Reset the iterator interface
	 *  Addition to the standard Iterator interface.
	 *  This method shall be called *before* using the Iterator interface
	 */
	public void reset() {
		this.keys = this.liste.keySet();
		this.keysIterator = this.keys.iterator();
		this.index = -1;
	}
	/*===================================================================
	 * PROTECTED - helpers for Iterator interface  
	 ===================================================================*/
	
	
	/*===================================================================
	 * RECYCLING  
	 ===================================================================*/
	public void _clean() {
		super._clean();
		this.keys = null;
		this.keysIterator = null;
		this.liste.clear();
		
	}
	
}//endclass
