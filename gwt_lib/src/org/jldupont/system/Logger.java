/**
 * @author Jean-Lou Dupont
 *
 */
package org.jldupont.system;

public class Logger {

	public final static int INFO  = 0;
	public final static int DEBUG = 1;
	public final static int ERROR = 2;
	public final static int WARN  = 3;
	
	public static void log( String msg ) {
		
		if ( isAvailable() == false )
			return;
		
		logToFirebug( msg );
	}

	public static void logError( String msg ) {
		if ( isAvailable() == false ) return;
		error(msg);
	}

	public static void logInfo( String msg ) {
		if ( isAvailable() == false ) return;		
		info(msg);
	}

	public static void logDebug( String msg ) {
		if ( isAvailable() == false ) return;		
		debug(msg);
	}
	
	public static void logWarn( String msg ) {
		if ( isAvailable() == false ) return;		
		warn(msg);
	}
	
	public static void logDir( Object obj ) {
		if ( isAvailable() == false ) return;		
		dir( obj );
	}
	
	public static void log( String msg, int code ) {
		
		if ( isAvailable() == false )
			return;
		
		switch( code ) {
		case INFO: 
			info(msg); 
			break;
		case DEBUG:
			debug(msg);
			break;
		case ERROR:
			error(msg);
			break;
		case WARN:
			warn(msg);
			break;
		}
		
	}
	
	/**
	 * Returns the availability status
	 * of Firebug console
	 * 
	 * @return boolean
	 */
	protected static native boolean isAvailable() /*-{
	
		return ( typeof console != "undefined" );
		
	}-*/;
	
	protected static native void logToFirebug( String msg ) /*-{
		console.log( msg );
		
	}-*/;

	protected static native void info( String msg ) /*-{
		console.info( msg );
	
	}-*/;

	protected static native void debug( String msg ) /*-{
		console.debug( msg );

	}-*/;

	protected static native void warn( String msg ) /*-{
		console.warn( msg );

	}-*/;
	
	protected static native void error( String msg ) /*-{
		console.error( msg );

	}-*/;

	protected static native void dir( Object o ) /*-{
			console.dir( o );

	}-*/;
	
	
}//end