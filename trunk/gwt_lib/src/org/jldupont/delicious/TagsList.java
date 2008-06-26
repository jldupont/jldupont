/**
 * @author Jean-Lou Dupont
 * 
 * Delicious Tags
 * 
 */

package org.jldupont.delicious;

import java.util.Iterator;
import java.util.Set;

import org.jldupont.system.Liste;
import org.jldupont.system.Logger;

import org.jldupont.localstore.StorableListe;

import com.google.gwt.json.client.JSONObject;
import com.google.gwt.json.client.JSONValue;

public class TagsList 
	extends org.jldupont.localstore.StorableListe {

	final static String thisClass = "org.jldupont.delicious.TagsList";
	
	/*===================================================================
	 * CONSTRUCTORS 
	 ===================================================================*/
	public TagsList() {
		super(thisClass, "default_id",true);
		setup();
	}
	public TagsList(String classe, String id) {
		super(classe,id,true);
		setup();
	}
	public TagsList(String id) {
		super(thisClass, id,true);
		setup();
	}
	private void setup() {
	}
	/*===================================================================
	 * PUBLIC 
	 ===================================================================*/
	public void putAll( JSONObject obj ) {

		Set set = obj.keySet();
		Iterator i = set.iterator();
		
		while( i.hasNext() ) {
			String key = (String) i.next();
			JSONValue value = obj.get( key );
			this.put(key, value);
		}

	}
	public String toString() {
		return super.toString();
	}
	/*===================================================================
	 * ObjectPool 
	 ===================================================================*/
	public void _clean() {
		super._clean();
	}
	
}//end class
