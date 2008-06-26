/**
 * LocalObjectStore
 * 
 * @author Jean-Lou Dupont
 * 
 *  Uses the most "appropriate" local storage.
 *  Works with GoogleGears only at the moment.
 */
/**
 * Schema:
 *  key TEXT , type TEXT, timestamp INTEGER, data BLOB
 *  
 *  key:       text string with / denoting hierarchy
 *  type:      Java object type
 *  timestamp: milliseconds since 1/1/1970
 *  data:      object representation
 */
package org.jldupont.localstore;

import org.jldupont.system.JLD_Object;

public class LocalObjectStore 
	extends JLD_Object 
	implements ObjectStoreInterface {
	
	final static String thisClass = "org.jldupont.localstore.LocalObjectStore";
	
	String name = null;
	
	/**
	 * Initialization status
	 *  Lazy initialization strategy
	 */
	boolean initialized = false;
	
	/**
	 * Storage
	 */
	BaseObjectStore store = null;
	
	/*===================================================================
	 * CONSTRUCTORS 
	 ===================================================================*/
	public LocalObjectStore(String classe, String id) {
		super(classe,id);
		setup();
	}
	public LocalObjectStore(String id) {
		super(thisClass,id);
		setup();
	}
	/**
	 * setup
	 *  Only GoogleGears support at the moment.
	 */
	private void setup() {
		
		// try GoogleGears...
		this.store = new GearsObjectStore(getId());
		if (this.store.exists())
			return;
		
		// fallback to Mock ...
		this.store = new MockObjectStore(getId());
	}
	
	/*===================================================================
	 * PUBLIC - ObjectStoreInterface
	 ===================================================================*/
	/**
	 * We always have Mock database ...
	 */
	public boolean exists() {
		return true;
	}
	public void setStorageName(String name) {
		this.name = new String( name );
	}
	
	public void initialize() {
		if (this.name.length() == 0) {
			throw new RuntimeException(thisClass+".initialize: storage name cannot be null");
		}
		this.store.initialize();
	}
	public void put(LocalObjectStoreInterface obj) {
		this.init();
	}
	
	public LocalObjectStoreInterface get(String key) {
		this.init();
		
		return null;
	}
	
	public boolean containsKey(String key) {
		this.init();
		
		return false;
	}
	
	public int headKey(String key) {
	
		return 0;
	}
	
	public void clear() {
		
	}
	/*===================================================================
	 * PROTECTED
	 ===================================================================*/
	
	protected void init() {
		
		if (this.initialized)
			return;
		
	}
	
	/*===================================================================
	 * ObjectPool
	 ===================================================================*/
	public void _clean() {
		super._clean();
		this.name = null;
	}
	
}//end class
