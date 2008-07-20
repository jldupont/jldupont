/**
 * ParameterList
 * 
 * @author Jean-Lou Dupont
 */
package org.jldupont.command;

import org.jldupont.system.StdListe;

public class ParameterList 
	extends StdListe 
	implements CommandParameters {

	final static String thisClass = "org.jldupont.command.ParameterList";
	
	/*===================================================================
	 * CONSTRUCTORS  
	 ===================================================================*/
	public ParameterList() {
		super( thisClass, "default_id" );
	}
	
	public ParameterList(String id ) {
		super( thisClass, id );
	}
	
	/*===================================================================
	 * CommandParameters interface
	 ===================================================================*/
	
	public Object getParameter( String key ) {
		
		return this.get(key);
	}
	
	public void   setParameter( String key, Object o ) {
		
		this.put(key, o);
	}

	
	/*===================================================================
	 * RECYCLING  
	 ===================================================================*/
	public void _clean() {
		super._clean();
	}
	
}//endclass
