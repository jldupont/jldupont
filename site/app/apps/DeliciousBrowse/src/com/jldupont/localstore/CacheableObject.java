/**
 * @author Jean-Lou Dupont
 */
package com.jldupont.localstore;

/**
 * @author Jean-Lou Dupont
 *
 */
public abstract class CacheableObject 
	extends Object {

	/**
	 * Key name
	 */
	private String name;
	
	/* ========================================================
	 * CONSTRUCTORS 
	 ========================================================*/
	/**
	 * Constructor
	 */
	CacheableObject() {
		this.name = "";
	}
	
	CacheableObject( String Name ) {
		this.name = Name;
	}

	/* ========================================================
	 * PUBLIC INTERFACE
	 ========================================================*/
	public String getName() {
		return this.name;
	}
	
	/* ========================================================
	 * INHERITED
	 ========================================================*/
	/**
	 * serialize
	 *  Used for serialiazation for storage 
	 */
	abstract public String serialize();
	
	/**
	 * unserialize
	 * 
	 * @return
	 */
	abstract public Object unserialize();
	
}//end class
