/**
 * @author Jean-Lou Dupont
 */
package org.jldupont.command;



public class CommandStatus {

	/**
	 * Pending status
	 */
	boolean pending = false;
	
	/**
	 * Exit code
	 */
	boolean code = false;

	/**
	 * Message
	 */
	String message = null;
	
	/*===================================================================
	 * Constructors 
	 ===================================================================*/
	public CommandStatus() {
		
	}
	
	public CommandStatus( boolean pending, boolean code ) {
		this.pending = pending;
		this.code = code;
	}

	public CommandStatus( boolean pending ) {
		this.pending = pending;
	}
	
	public CommandStatus( String msg ) {
		this.pending = false;
		this.code = false;
		this.message = new String(msg);
	}
	
	/*===================================================================
	 * Pending 
	 ===================================================================*/

	public boolean isPending() {
		return this.pending;
	}
	
	public void setPending() {
		this.pending = true;
	}
	
	public void setPending( boolean p ) {
		this.pending = p;
	}
	
	/*===================================================================
	 * ExitCode 
	 ===================================================================*/
	
	public boolean getExitCode() {
		return this.code;
	}
	
	public void setExitCode() {
		this.code = true;
	}
	
	public void setExitCode( boolean code ) {
		this.code = code;
	}

	/*===================================================================
	 * Message 
	 ===================================================================*/
	
	public void setMessage( String msg ) {
		this.message = msg;
	}
	
	public String getMessage() {
		return this.message;
	}
}//end
