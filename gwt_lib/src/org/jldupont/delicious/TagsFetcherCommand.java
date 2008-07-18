/**
 * @author Jean-Lou Dupont
 */
package org.jldupont.delicious;

import org.jldupont.command.Command;
import org.jldupont.command.CommandParameters;
import org.jldupont.command.CommandStatus;

import org.jldupont.system.Factory;

public class TagsFetcherCommand 
	extends Command {

	final static String thisClass = "org.jldupont.delicious.TagsFetcherCommand";
	
	TagsManager manager = null;
	
	/*===================================================================
	 * Constructor 
	 ===================================================================*/
	public TagsFetcherCommand() {
		super( thisClass, "default_id", true );
	}

	/*===================================================================
	 * Constructor 
	 ===================================================================*/
	
	@Override
	protected void _onError() {
		// TODO Auto-generated method stub

	}

	@Override
	protected void _onPending() {
		// TODO Auto-generated method stub

	}

	@Override
	protected CommandStatus _run(CommandParameters p) {

		this.manager = (TagsManager) Factory.create( "org.jldupont.delicious.TagsManager" );
		
		// set the callback

		// place the request

		// completed right away?  the tags must have been available
		// in the localstore then...
		
		return null;
	}

	/**
	 * @see org.jldupont.command.CommandInterface
	 */
	@Override
	public void setStatus(CommandStatus s) {
		this.propagateCommandStatus(s);

	}
	/*===================================================================
	 * CALLBACK 
	 ===================================================================*/

	
	/*===================================================================
	 * Recycling 
	 ===================================================================*/
	public void _clean() {
		super._clean();
	}
	
}//end class
