/**
 * CommandStatus
 * 
 * @author Jean-Lou Dupont
 */
package org.jldupont.command;


public class CommandStatus {

	/**
	 * Exit codes
	 */
	final static int TIMEOUT = 1;
	
	/**
	 * Pending status
	 */
	boolean pending = false;
	
	/**
	 * Exit code
	 */
	int exitCode = 0;

	/**
	 * StatusCode
	 */
	boolean statusCode = false;
	
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
		this.exitCode = 0;
	}

	public CommandStatus( boolean pending ) {
		this.pending = pending;
	}
	
	public CommandStatus( String msg ) {
		this.pending = false;
		this.exitCode = 0;
		this.statusCode = false;
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
	
	public int getExitCode() {
		return this.exitCode;
	}
	
	public void setExitCode( int code ) {
		this.exitCode = code;
	}

	/*===================================================================
	 * StatusCode 
	 ===================================================================*/
	
	public boolean getStatusCode() {
		return this.statusCode;
	}
	public void setStatusCode( boolean code ) {
		this.statusCode = code;
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
