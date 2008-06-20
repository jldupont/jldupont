package com.jldupont.project.client;

import java.util.Iterator;

public class ParamsList 
	implements Iterator {
	
	/**
	 * Constant 
	 */
	static int MAX_PARAMS = 10;
	
	int index = 0;
	
	int num_params = 0;
	
	String liste;
	
	Param[] params;

	/**
	 * Constructor
	 * 
	 * @param liste String
	 */
	ParamsList( ) {
		
		this.params = new Param[MAX_PARAMS];
		this.liste = new String( this.getLocationHref() );
		this.extractParams();
	}

	/*===================================================================
	 * ITERATOR 
	 ===================================================================*/
	public boolean hasNext() {
		
		if ( this.params == null )
			return false;
		
		return ( this.index < this.num_params );
	}
	
	public Object next() {
		
		if ( this.params == null )
			throw new NullPointerException("empty params list");
		
		return this.params[ this.index++ ];
	}
	//TODO if necessary...
	public void remove() {
		
	}
	
	public void rewind() {
		this.index = 0;
	}
	/*===================================================================
	 * 
	 ===================================================================*/
	
	/**
	 * Extracts the params from the "liste" provided
	 * e.g. liste =  u=username&tf=tag1+tag2&pf=companies*
	 */
	protected void extractParams( ) {
		
		int index = this.liste.indexOf( '?' );
		if ( index == -1 )
			return;
		
		// first, split off where the ? is
		String s = new String( this.liste.substring(index +1).trim() );
		if ( s.length() == 0 )
			return;
		
		// "explode" string through the & char
		String[] tuples = s.split("&");
		
		int i,j=0;
		String[] bits;
		
		// "explode" string through the = char
		for ( i=0; i<tuples.length && j<MAX_PARAMS; i++ ) {

			bits = tuples[i].split("=");
			if ( bits.length != 2 )
				continue;
			
			this.params[j++] = new Param( bits[0], bits[1] );
		}
		
		this.num_params = j;
		
	}//extractParams
	
	/**
	 * GWT loads the application through an iframe
	 */
	protected native String getLocationHref()  /*-{
	  return parent.window.location.href;
	}-*/;
	
}//endclass