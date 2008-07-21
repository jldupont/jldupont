/**
 * TagsManagerCommand
 * 
 * @author Jean-Lou Dupont
 */
package org.jldupont.delicious;

import com.google.gwt.user.client.Event;

import org.jldupont.command.Command;
import org.jldupont.command.CommandStatus;

import org.jldupont.system.Factory;
import org.jldupont.system.LoggableRuntimeException;

import org.jldupont.web.CallbackResponseObject;

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
	
	protected void _onError() {
		// TODO Auto-generated method stub
		// not much todo...
	}

	protected void _onPending() {
		// TODO Auto-generated method stub
		// not much todo...
	}
	
	public void setParameterName( String paramName ) {
		//nothing todo
	}

	protected CommandStatus _run( ) throws RuntimeException {
		
		// extract 'user' parameter
		String user = (String) this.param.getParameter("user");
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
			this.param.setParameter( "taglist", tl );
			return new CommandStatus( /*OK*/ );
		}

		return new CommandStatus( true /*pending*/ );
	}

	/**
	 * @see org.jldupont.command.CommandInterface
	 */
	public void setStatus(CommandStatus s) {
		this.propagateCommandStatus(s);

	}
	/*===================================================================
	 * TagsChangedListener interface 
	 ===================================================================*/
	
	public void fireCallEvent(CallbackResponseObject c) {
		
		// timeout?  => error
		if (c.isError()) {
			this.propagateCommandStatus( new CommandStatus( CommandStatus.TIMEOUT, "TagsFetcher: timeout" ) );
			return;
		}
	
		//TODO what about empty list?
		this.param.setParameter("taglist", c);
			
		// success? continue chain
		this.runNext();
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
