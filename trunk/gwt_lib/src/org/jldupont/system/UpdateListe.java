/**
 * UpdateListe interface
 * 
 * @author Jean-Lou Dupont
 */
package org.jldupont.system;

public interface UpdateListe {

	/**
	 * Clears the list
	 */
	public void clear();
	
	/**
	 * Inserts key at tail
	 * @param key String
	 */
	public void insertItem(String key);
	
	/**
	 * Inserts key at index
	 * @param key
	 * @param index
	 */
	public void insertItem(String key, int index);
	
}//end