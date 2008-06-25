/**
 * @author Jean-Lou Dupont
 */
package org.jldupont.web;

import com.google.gwt.user.client.EventListener;

public interface CallListener 
	extends EventListener {
	
	public void fireCallEvent(CallEventObject c);
	
}
