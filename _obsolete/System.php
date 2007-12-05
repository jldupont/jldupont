<?php
/**
 * System Class
 *
 * @author Jean-Lou Dupont
 * @package System
 * @version @@package-version@@
 * @Id $Id$
 */
//<source lang=php>

require 'System.inc.php';

class JLD_System 
{
	/**
	 * Constructor
	 */
	protected function __construct(){}
	
	/**
	 * Singleton interface.
	 */
	static $instance = null;
	public static function g()
	{
		if ( is_object( self::$instance ) )
			return self::$instance;
			
		$_c = __CLASS__;
		
		return self::$instance = new $_c;
	}
	/**
	 * Cloning is not allowed for this class.
	 */
    public function __clone()
    {
        throw new Exception('Cloning is not allowed.', E_USER_ERROR);
    }

// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// MESSAGING

	var $msgMap = array();

	/**
	 * Registers an object for a precise message
	 */
	public function registerListener( $msg, &$obj )
	{
		$this->msgMap[ $msg ][] = $obj;
	}
	/**
	 * Unregisters an object for a precise message
	 */
	public function unregisterListener( $msg, &$obj )
	{
		if ( !isset( $this->msgMap[ $msg ] ) )
			return false;
			
		$liste = $this->msgMap[ $msg ];
		$loc = array_search( $obj, $liste, true /*strict*/ );
		if ( $loc === false )
			return false;
			
		unset( $this->msgMap[ $msg ][ $loc ] );
		
		return true;
	}
	/**
	 * Posts a message
	 */
	public function postMessage( $msg, &$params = null )
	{
		if ( !isset( $this->msgMap[ $msg ] ))
			return null;
			
		$liste = $this->msgMap[ $msg ];
		if ( empty( $liste ) )
			return null;
			
		foreach( $liste as $index => &$obj )
		{
			try 
			{
				$obj->sinkMessage( $msg, $params );
			}
			catch( Exception $e )
			{
				#TODO
			}
		}
		return true;
	}
	/**
	 * isRegisteredListeners
	 */
	public function isRegisteredListeners( $msg )
	{
		return ( isset( $this->msgMap[ $msg ] ) );
	}
	/**
	 * Purges the listeners array
	 */
	public function purgeListeners()
	{
		$this->msgMap = null;
	}
// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// 

}//end class
//</source>