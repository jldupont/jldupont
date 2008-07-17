/**
 * Command interface
 * 
 * @author Jean-Lou Dupont
 */
package org.jldupont.command;

public interface CommandInterface {

	public void setParameter( CommandParameter p );
	
	/**
	 * Execute the command chain
	 */
	public void run();
	
	/**
	 * Verifies if the completion is pending
	 * @return boolean
	 */
	public boolean isPending();
	
	/**
	 * Returns the exit code
	 * Only valid if the 'pending' status is false
	 * 
	 * @return boolean
	 */
	public boolean getExitCode();
	
	/**
	 * Sets the next command in the chain
	 * 
	 * @param me Command - used for callback path
	 * @param next Command
	 */
	public void setNext( CommandInterface me, CommandInterface next );
	
}//end