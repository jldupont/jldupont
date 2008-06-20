/**
 * @author Jean-Lou Dupont
 *
 */
package com.jldupont.libs.system;

import java.lang.Object;
import com.jldupont.libs.system.Factory;;

abstract public class JLD_Object 
	extends Object {

	/**
	 * Class type
	 */
	String classe = null;
	
	/**
	 * Identifier
	 */
	String id = null;
	
	/**
	 * Recyclable capability flag
	 */
	boolean recyclable = false;
	
	/*===================================================================
	 * CONSTRUCTORS 
	 ===================================================================*/
	
	public JLD_Object() {
		super();
		this.classe = null;
		this.id = null;
	}
	
	public JLD_Object( String classe ) {
		super();
		this.classe = classe;
	}
	
	public JLD_Object( String classe, String id ) {
		super();		
		this.classe = classe;
		this.id = id;
	}
	/*===================================================================
	 * PUBLIC 
	 ===================================================================*/
	/**
	 * getClasse
	 * @return classe
	 */
	public String getClasse() {
		return this.classe;
	}
	/**
	 * getId
	 * @return String
	 */
	public String getId() {
		return this.id;
	}
	
	/*===================================================================
	 * ObjectPool functionality 
	 ===================================================================*/
	
	protected void setRecyclable() {
		this.recyclable = true;
	}
	protected void setRecyclable( boolean state ) {
		this.recyclable = state;
	}
	/**
	 * getRecyclable
	 * @return boolean
	 */
	public boolean getRecyclable() {
		return this.recyclable;
	}
	/**
	 * recycle 
	 *  recycles this object by putting it
	 *  in the ObjectPool
	 */
	public void recycle() {
		
		if ( getRecyclable() ) {
			ObjectPool pool = (ObjectPool) Factory.create("ObjectPool", "recycle" );
			pool.recycle( this );
		} else {
			Logger.log( "JLD_OBJECT: class (" + getClasse() +") is not recyclable" );
		}
	}
	
}//end class
