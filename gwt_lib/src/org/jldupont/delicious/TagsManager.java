/**
 * TagsManager
 * 
 * @author Jean-Lou Dupont
 * 
 * The client of this class must register itself 
 */
package org.jldupont.delicious;

import org.jldupont.system.JLD_Object;
import org.jldupont.system.Factory;
import org.jldupont.localstore.LocalObjectStore;
import org.jldupont.localstore.LocalStoreException;
import org.jldupont.localstore.LocalObjectStoreInterface;
import org.jldupont.web.CallEventListener;
import org.jldupont.web.CallListener;

import com.google.gwt.user.client.Event;

public class TagsManager 
	extends JLD_Object 
	implements CallEventListener {

	/**
	 * Storage name
	 */
	String nameStorage = null;
	
	final static String thisClass = "org.jldupont.delicious.TagsManager";
	
	TagsFetcher tf = null;
	
	/*===================================================================
	 * CONSTRUCTORS 
	 ===================================================================*/
	public TagsManager() {
		super( thisClass, "default_id", true );
		setup();
	}
	
	public TagsManager( String classe, String id, boolean recyclable ) {
		super( classe, id, recyclable );
		setup();		
	}

	protected void setup() {
		
		this.tf = (TagsFetcher) Factory.create("org.jldupont.delicious.TagsFetcher");		
	}
	
	/*===================================================================
	 * PUBLIC INTERFACE 
	 ===================================================================*/
	/**
	 * setStorageName
	 * 
	 * @param name String
	 */
	public void setStorageName(String name) {
		this.nameStorage = new String( name );
	}
	
	/**
	 * Returns the tag list for a specified user
	 * + Verifies the localstore
	 * + else performs remote fetch
	 * 
	 *  @return TagsList or NULL to signify 'pending'
	 */
	public TagsList get( String user ) throws RuntimeException {
	
		// try the local copy
		TagsList tl = this.localFetch(user);
		if ( tl != null )
			return tl;
		
		// remoteFetch returns null to signal 'pending'
		return this.remoteFetch(user);
	}
	/**
	 * Sets a tag list
	 * 
	 * @param user
	 * @param liste
	 * @param timestamp
	 */
	public void set( String user, TagsList liste, int timestamp ) throws LocalStoreException {
		
		LocalObjectStore store = (LocalObjectStore) Factory.create("org.jldupont.delicious.LocalObjectStore");
		
		String key = this.generateKey(user);
		
		liste.setName(key);
		
		try {
			store.put( liste );
		} catch (LocalStoreException e) {
			throw e;
		} finally {
			store.recycle();			
		}
	}

	/*===================================================================
	 * CallEventListener 
	 ===================================================================*/
	
	public void addCallListener(CallListener s) {
		this.tf.addCallListener(s);
	}
	public void removeCallListener(CallListener s) {
		this.tf.removeCallListener(s);		
	}

	/*===================================================================
	 * PRIVATE INTERFACE 
	 ===================================================================*/
	/**
	 * @param user
	 */
	private TagsList remoteFetch( String user ) throws RuntimeException {
		
		this.tf.setUser(user);
		
		try {
			this.tf.get();
		} catch(RuntimeException e) {
			throw e;
		} finally {
			tf.recycle();
		}
		return null;
	}
	/**
	 * localFetch
	 * 
	 * @param user
	 * @return TagsList or NULL
	 */
	private TagsList localFetch( String user ) {
		
		LocalObjectStore store = (LocalObjectStore) Factory.create("org.jldupont.delicious.LocalObjectStore");
		LocalObjectStoreInterface obj = null;
		
		store.setStorageName(this.name);
		
		try {
			obj = store.get( this.generateKey(user) );
		} catch (LocalStoreException e) {
			return null;
		} finally {
			store.recycle();			
		}
		
		return (TagsList) obj;
	}

	/**
	 * Declare here so to help derived classes 
	 */
	public void onBrowserEvent(Event event) {
	}
	
	protected String generateKey( String user ) {
		
		return new String( this.nameStorage + '/' + user );
	}
	
	/**
	 * Recycling
	 */
	public void _clean() {
		super._clean();
	}
	
}//end class