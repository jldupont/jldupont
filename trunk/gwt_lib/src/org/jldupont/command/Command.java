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
	 * CommandStatus
	 */
	CommandStatus status = new CommandStatus();
	
	/**
	 * CommandParameter
	 */
	protected CommandParameters param = null;
	
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

	public Command( String classe, String id, boolean recyclable ) {
		super( classe, id, recyclable );
	}

	/*===================================================================
	 * CommandInterface 
	 ===================================================================*/

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
		return this.status.isPending();
	}
	/**
	 * @see org.jldupont.command.CommandInterface#getExitCode()
	 */
	public int getExitCode() {
		return this.status.getExitCode();
	}

	/**
	 * @see org.jldupont.command.CommandInterface#getStatusCode()
	 */
	public boolean getStatusCode() {
		return this.status.getStatusCode();
	}

	/**
	 * @see org.jldupont.command.CommandInterface#run()
	 * 
	 * @pattern template_method
	 */
	public CommandStatus run( CommandParameters p ) {
		
		this.param = p;
		
		// run our command
		this.status = this._run( );

		// if we failed, then don't bother with the rest of the chain
		if ( !this.status.isPending() && !this.status.getStatusCode() ) {
			return this.status;
		}
		
		// Continue the chain
		// ##################
		CommandStatus nextStatus = this.runNext( );
		
		// End-of-Chain:
		//  if no next is present, then return our status
		if ( nextStatus == null )
			return this.status;
		
		// if next command in the chain is pending,
		// then the whole chain is pending
		if ( nextStatus.isPending() ) {
			this._onPending();
			return nextStatus;
		}
		
		// if the next command in the chain isn't successful,
		// then the whole chain is declared unsuccessful too.
		if ( status.getStatusCode() == false ) {
			this._onError();
			return nextStatus;
		}
		
		// the next command in the chain was successful,
		// then the determining status is ours ... for now ;-)
		return this.status;
	}

	/*===================================================================
	 * ABSTRACT 
	 ===================================================================*/
	
	abstract protected CommandStatus _run( );
	
	abstract protected void _onPending( );
	
	abstract protected void _onError( );

	/*===================================================================
	 * PROTECTED 
	 ===================================================================*/
	/**
	 * Used by callbacks to propagate the command chain status
	 * @param s
	 */
	protected void propagateCommandStatus( CommandStatus s ) {
		
		// first in the chain...
		if ( this.prev == null ) {
			this.status = s;
			return;
		}

		// propagate upstream
		this.prev.setStatus(s);
	}
	
	
	/**
	 * Runs the next command in the chain
	 */
	protected CommandStatus runNext( ) {
		
		if (this.next != null)
			return this.next.run( this.param );
		
		return null;
	}
	
}//end
