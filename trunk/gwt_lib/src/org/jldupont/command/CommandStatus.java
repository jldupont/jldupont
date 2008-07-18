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
	public final static int TIMEOUT = 1;
	
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
	
	public CommandStatus( int exitCode, String msg ) {
		setup( exitCode, msg );
	}
	
	/**
	 * Constructor used in error state
	 * @param exitCode
	 */
	public CommandStatus( int exitCode ) {
		this.exitCode = exitCode;
		this.statusCode = false;
		this.pending = false;
	}
	
	public CommandStatus( boolean pending, boolean statusCode ) {
		this.pending = pending;
		this.statusCode = statusCode;
	}

	/**
	 * Constructor for pending state
	 * @param pending
	 */
	public CommandStatus( boolean pending ) {
		this.pending = pending;
	}
	
	/**
	 * Constructor for error state
	 * @param msg
	 */
	public CommandStatus( String msg ) {
		this.pending = false;
		this.exitCode = 0;
		this.statusCode = false;
		this.message = new String(msg);
	}
	
	private void setup( int exitCode, String msg ) {
		this.exitCode = exitCode;
		this.message = msg;
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
