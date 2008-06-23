/**
 * @author Jean-Lou Dupont
 *
 */
package org.jldupont.system;

import java.lang.Object;
import org.jldupont.system.Logger;

abstract public class JLD_Object 
	extends Object {

	/**
	 * Class type
	 */
	public String classe = null;
	
	/**
	 * Identifier
	 */
	String id = null;
	
	/**
	 * Recyclable capability flag
	 */
	boolean recyclable = false;
	
	/**
	 * Only initialized if used.
	 */
	org.jldupont.system.Timer timer = null;
	
	/**
	 * Operation busy flag
	 */
	boolean isBusy = false;
	
	/*===================================================================
	 * CONSTRUCTORS 
	 ===================================================================*/
	
	public JLD_Object() {
		super();
		Logger.log("JLD_Object: creating object class[null] id[null]");
		this.classe = null;
		this.id = null;
	}
	
	public JLD_Object( String classe ) {
		super();
		Logger.log("JLD_Object: creating object class["+classe+"] id[null]");		
		this.classe = classe;
	}
	
	public JLD_Object( String classe, String id ) {
		super();		
		Logger.log("JLD_Object: creating object class["+classe+"] id["+id+"]");		
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
		
		String exid = _exId();
		String id = new String();
		if ( exid != null )
			id = this.id+ " ["+exid+"]" ;
		else
			id = this.id;
		
		if ( getRecyclable() ) {
			ObjectPool pool = (ObjectPool) Factory.create("ObjectPool", "recycle" );
			Logger.log( "JLD_OBJECT: sending object with id("+id+") to the recycle bin" );
			pool.recycle( this );
		} else {
			Logger.log( "JLD_OBJECT: class (" + getClasse() +") is not recyclable" );
		}
	}

	/*===================================================================
	 * OPERATION functionality 
	 ===================================================================*/
	protected void startOperation(int timeout) {
		
		if ( this.isBusy ) {
			throw new RuntimeException(this.classe+".startOperation : already busy");
		}
		
		this.isBusy = true;
		
		if ( this.timer == null ) {
			this.timer = new org.jldupont.system.Timer();
			this.timer.setTarget( this );
		}
		
		this.timer.schedule( timeout );
	}
	public boolean getBusy() {
		return this.isBusy;
	}
	/**
	 * TODO override
	 */
	public void timerExpiredEvent() {
		this.isBusy = false;
		Logger.log(this.classe+".timerExpiredEvent: default method called");
	}
	
	/*===================================================================
	 * PROTECTED 
	 ===================================================================*/
	/**
	 * Derived classes should handle this
	 *  if special "cleaning" is required when the object is retrieved 
	 *  from the ObjectPool before being handed-off to the requesting
	 *  party.
	 *  
	 * Also, derived classes which use "object composition" 
	 *  should _clean also their composing objects.
	 */
	public void _clean() {
		this.timer = null;
	}
	/**
	 * Used by derived classes to provide
	 * additional "extra" identification information 
	 */
	protected String _exId() {
		return null;
	}
}//end class
