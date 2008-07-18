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
	 *  
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
		
		// extract 'user' parameter
		
		// place the request
		try {
			this.manager.generateKey(user);
		} catch(RuntimeException e) {
			
		} finally {
			
		}
		
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
	 * TagsChangedListener interface 
	 ===================================================================*/
	
	public void fireCallEvent(CallEventObject c) {
		
		if (c.isTimeout()) {
			
		}
		
	}
	/**
	 * Declare here so to help derived classes 
	 */
	public void onBrowserEvent(Event event) {
	}
	
	/*===================================================================
	 * Recycling 
	 ===================================================================*/
	public void _clean() {
		super._clean();
	}
	
}//end class
