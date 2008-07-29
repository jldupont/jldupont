package org.jldupont.rest;

import java.util.Iterator;
import java.util.HashMap;
import java.util.Map;

import org.jldupont.system.Liste;

import com.google.gwt.http.client.URL;

/**
 * URLParamsList
 * @author Jean-Lou Dupont
 *
 */
public class URLParamsList {

	private URLParamsList() {
		
	}
	
	public static String build( String s, HashMap params ) {

		Iterator iter = params.entrySet().iterator();
		String liste = new String( s );
		String key, value;
		int j = 0;
		
		while( iter.hasNext() ) {
			
			if ( j>0 ) {
				liste += "&";
			}
				
			Map.Entry entry = (Map.Entry)iter.next();
			key = (String)entry.getKey();
			value = (String)entry.getValue();

			liste += URL.encode( key + "=" + value );
			j++;
		}
		
		// if there was at least one parameter
		//  start the query part with the ? separator
		if ( j>0 ) {
			liste = "?" + liste;
		}
		
		return liste;
		
	}
	
	public static String build( HashMap params ) {
		return build( "", params );
	}
	
}//