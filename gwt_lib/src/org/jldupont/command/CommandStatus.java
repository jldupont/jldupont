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
	
}//end
