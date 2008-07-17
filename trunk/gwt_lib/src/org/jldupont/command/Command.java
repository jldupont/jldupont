/**
 * Command base class
 * 
 * @author Jean-Lou Dupont
 */
package org.jldupont.command;

import org.jldupont.system.JLD_Object;

abstract public class Command 
	extends JLD_Object 
	implements CommandInterface {

	/**
	 * Pending status
	 */
	boolean pending = false;
	
	/**
	 * Exit code
	 */
	boolean code = false;
	
	/**
	 * CommandParameter
	 */
	CommandParameter param = null;
	
	/**
	 * Previous in command chain
	 */
	CommandInterface prev = null;
	
	/**
	 * Next in command chain
	 */
	CommandInterface next = null;
	
	/*===================================================================
	 * CONSTRUCTORS 
	 ===================================================================*/

	public Command() {
		super();
	}

	/*===================================================================
	 * CommandInterface 
	 ===================================================================*/

	/**
	 * @see org.jldupont.command.CommandInterface#setParameter(CommandParameter)
	 */
	public void setParameter( CommandParameter p ) {
		this.param = p;
	}

	/**
	 * @see org.jldupont.command.CommandInterface#setNext(CommandInterface, CommandInterface)
	 */
	public void setNext( CommandInterface me, CommandInterface next ) {
		this.prev = me;
		this.next = next;
	}
	
	/**
	 * @see org.jldupont.command.CommandInterface#isPending()
	 */
	public boolean isPending() {
		return this.pending;
	}
	/**
	 * @see org.jldupont.command.CommandInterface#getExitCode()
	 */
	public boolean getExitCode() {
		return this.code;
	}
	
	/**
	 * @see org.jldupont.command.CommandInterface#run()
	 */
	abstract public void run();
	
}//end
