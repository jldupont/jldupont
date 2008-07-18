/**
 * TagsManagerCommand
 * 
 * @author Jean-Lou Dupont
 */
package org.jldupont.delicious;

import org.jldupont.command.Command;
import org.jldupont.command.CommandParameters;
import org.jldupont.command.CommandStatus;

import org.jldupont.system.Factory;
import org.jldupont.system.LoggableRuntimeException;
import org.jldupont.web.CallEventObject;

import com.google.gwt.user.client.Event;

public class TagsManagerCommand 
	extends Command 
	implements TagsChangedListener {

	final static String thisClass = "org.jldupont.delicious.TagsFetcherCommand";
	
	TagsManager manager = null;
	
	/*===================================================================
	 * Constructor 
	 ===================================================================*/
	public TagsManagerCommand() {
		
		super( thisClass, "default_id", true );
		
		this.manager = (TagsManager) Factory.create( "org.jldupont.delicious.TagsManager" );

		// set listening interface
		this.manager.addCallListener(this);
	}
	
	/*===================================================================
	 * CONFIGURATION - must be set prior to using an instance
	 ===================================================================*/
	/**
	 * @see org.jldupont.delicious.TagsManager#setStorageName(String)
	 */
	public void setStorageName(String name) {
		this.manager.setStorageName(name);
	}
	
	/*===================================================================
	 * Command interface
	 ===================================================================*/
	
	@Override
	protected void _onError() {
		// TODO Auto-generated method stub
		// not much todo...
	}

	@Override
	protected void _onPending() {
		// TODO Auto-generated method stub
		// not much todo...
	}

	@Override
	protected CommandStatus _run(CommandParameters p) throws RuntimeException {
		
		// extract 'user' parameter
		String user = (String) p.getParameter("user");
		if ( user == null )
			throw new LoggableRuntimeException( "TagsManager::_run: parameter 'user' not found" );
		
		TagsList tl = null;
		
		// place the request
		try {
			tl = this.manager.get( user );
		} catch(RuntimeException e) {
			throw new LoggableRuntimeException( "TagsManager::_run: " + e.getMessage() );			
		} finally {
			this._onError();
		}
		
		// completed right away?  the tags must have been available
		// in the localstore then...
		if ( tl != null ) {
			// queue the result for the chain's benefit
			p.setParameter("taglist", tl);
			return new CommandStatus( false, true );
		}

		return new CommandStatus( true /*pending*/ );
	}

	/**
	 * @see org.jldupont.command.CommandInterface
	 */
	@Override
	public void setStatus(CommandStatus s) {
		this.propagateCommandStatus(s);

	}
	/*===================================================================
	 * TagsChangedListener interface 
	 ===================================================================*/
	
	public void fireCallEvent(CallEventObject c) {
		
		// timeout?  => error
		if (c.isTimeout()) {
			this.propagateCommandStatus( new CommandStatus( "TagsFetcher: timeout" ) );
			return;
		}
	
		// success? continue chain
		
		
	}//
	
	/**
	 * Declare here so to help derived classes 
	 */
	public void onBrowserEvent(Event event) {
		// NOTHING todo... i think.
	}
	
	/*===================================================================
	 * Recycling 
	 ===================================================================*/
	public void _clean() {
		super._clean();
	}
	
}//end class
