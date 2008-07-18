/**
 * CommandParameter interface
 * 
 * @author Jean-Lou Dupont
 */
package org.jldupont.command;

public interface CommandParameters {

	public Object getParameter( String key );
	
	public void   setParameter( String key, Object o );
	
}//end
