/**
 * @author Jean-Lou Dupont
 */
package org.jldupont.test.client;

import com.google.gwt.json.client.JSONObject;
import com.google.gwt.json.client.JSONValue;
import com.google.gwt.user.client.Event;

import com.google.gwt.user.client.ui.ListBox;

import java.util.Set;
import java.util.Iterator;

import org.jldupont.delicious.TagsChangedListener;
import org.jldupont.web.CallEventObject;
import org.jldupont.system.Logger;


public class TagsChangedListenerTest

	implements TagsChangedListener {

	ListBox lb = null;
	
	public TagsChangedListenerTest( ListBox lb ) {
		this.lb = lb;
	}
	
	public void fireCallEvent(CallEventObject c) {
		//Window.alert("TagsChangedListenerTest.fireCallEvent: called! " + c.getJSONObject().toString() );
		JSONObject obj = c.getJSONObject();
		
		Set set = obj.keySet();
		Iterator i = set.iterator();
		
		while( i.hasNext() ) {
			String key = (String) i.next();
			JSONValue value = (JSONValue) obj.get( key );
			Logger.log("key: "+key+" value: "+value );
			this.lb.insertItem(key, 0);
		}
	}
	
	/**
	 * Declare here so to help derived classes 
	 */
	public void onBrowserEvent(Event event) {
	}
	
}//end class
