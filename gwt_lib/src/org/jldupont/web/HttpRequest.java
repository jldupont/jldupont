/**
 * HttpRequest
 * 
 * @author Jean-Lou Dupont
 */
package org.jldupont.web;

import com.google.gwt.http.client.RequestBuilder;
import com.google.gwt.http.client.RequestException;
import com.google.gwt.http.client.RequestTimeoutException;
import com.google.gwt.http.client.RequestCallback;
import com.google.gwt.http.client.Request;
import com.google.gwt.http.client.Response;
import com.google.gwt.http.client.URL;

import java.util.HashMap;
import java.util.Map;
import java.util.Iterator;
import java.lang.Throwable;

import org.jldupont.system.JLD_Object;
import org.jldupont.system.Logger;

abstract public class HttpRequest 
	extends JLD_Object {

	final static int codeNull    		= 0;
	final static int codeOK      		= 200;
	final static int codeTimeout 		= 1;
	final static int codeRequestError	= 2;
	final static int codeUnhandledError = 3;
	
	/*....................................................................
	 * PROPERTIES
	 ...................................................................*/
	HashMap params = null;
	
	/**
	 * Default request timeout
	 */
	int timeout = 2000;
	
	/**
	 * URL
	 */
	String url = null;
	
	/**
	 * Last error code
	 */
	int lastError = codeNull;
	
	/**
	 * Response
	 */
	Request response = null;
	
	/*===================================================================
	 * CONSTRUCTORS 
	 ===================================================================*/
	public HttpRequest(String id) {
		super("org.jldupont.web.HttpRequest", id );
		setRecyclable();
		this.params = new HashMap();
	}

	/*===================================================================
	 * PUBLIC interface 
	 ===================================================================*/
	/**
	 * setTimeout
	 * 
	 * @param timeout
	 */
	public void setTimeout( int timeout ) {
		this.timeout = timeout;
	}
	
	public void setUrl( String url ) {
		this.url = new String( url );
	}
	/**
	 * Fetches the specified resource
	 * 
	 * @return boolean
	 */
	public boolean fetch( ) {
		
		boolean returnCode = true; // be optimistic
		String cUrl = new String();
		String p;
		
		// Analyze url to determine if the requested url resource
		// is local or remote
		if ( this.url.length() == 0) {
			throw new RuntimeException("HttpRequest.fetch : url can not be empty");
		}
		// build complete url
		p = buildParamsList();
		cUrl = this.url + p;
		
		// build and perform the request
		RequestBuilder builder = new RequestBuilder(RequestBuilder.GET, cUrl);
		try {
			builder.setTimeoutMillis(this.timeout);
			
			this.response = builder.sendRequest(null, new RequestCallback() {
				public void onError(Request request, Throwable exception) {}
		        public void onResponseReceived(Request request, Response response) {}
		      });
		    } catch( RequestTimeoutException e ) {
		    	this.lastError = codeTimeout;
		    	log( p, "timeout" );
		    	returnCode = false;
		    } catch (RequestException e) {
		    	this.lastError = codeRequestError;
		    	log( p, "can't retrieve url" );
		    	returnCode = false;		    	
		    } catch (Exception e) {
		    	this.lastError = codeUnhandledError;
		    	log( p, "unhandled error msg:"+e.getMessage() );
		    	returnCode = false;		    	
		    }
		
		if (returnCode)
			callbackSuccess( response );
		else
			callbackError( );
		    
		return returnCode;
	}
	/**
	 * addParam
	 * 
	 * @param key
	 * @param value
	 */
	public void addParam( String key, String value ) {
		params.put(key, value);
	}
	/*===================================================================
	 * DERIVED interface 
	 ===================================================================*/
	abstract void callbackSuccess(Request response);
	abstract void callbackError();
	
	/*===================================================================
	 * PROTECTED 
	 ===================================================================*/
	protected void log( String params, String msg ) {
		Logger.log("HttpRequest: url("+this.url+") query("+params+") => " + msg );
	}
	/**
	 * Iterates through the params list and builds the URL
	 */
	protected String buildParamsList() {
		
		Iterator iter = this.params.entrySet().iterator();
		String liste = new String();
		String key, value;
		Integer j = 0;
		
		while( iter.hasNext() ) {
			
			if ( j>0 ) {
				liste += "&";
			}
				
			Map.Entry entry = (Map.Entry)iter.next();
			key = (String)entry.getKey();
			value = (String)entry.getValue();

			liste += URL.encode( key + "=" + value );
		}
		
		// if there was at least one parameter
		//  start the query part with the ? separator
		if ( j>0 ) {
			liste = "?" + liste;
		}
		
		return liste;
	}
	/**
	 * Called by the ObjectPool when retrieving
	 *  an instance from the pool.
	 *  
	 * @see org.jldupont.system.JLD_Object#_clean()
	 */
	protected void _clean() {
		this.params.clear();
		this.timeout = 2000;
		this.url = null;
		this.response = null;
		this.lastError = codeNull;
	}
	
}//endclass
