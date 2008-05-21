<?php
/**
 * JLD_MindMeister
 *  
 *
 * @author Jean-Lou Dupont
 * @version @@package-version@@
 * @package MindMeister
 * @category OnlineTools
 * @example
 */

require_once 'Method.php';
require_once 'Liste.php';
require_once 'HTTP/Request.php';

class JLD_MindMeister {

	const CLASS_PATH = 'JLD_MindMeister_';

	static $key  = null;
	static $skey = null;
	
	/**
	 * No need to instantiate from this class
	 */
	protected function __construct() {
	}
	public static function setApiKey( $api_key, $secret_key ){
	
		self::$key  = $api_key;
		self::$skey = $secret_key;
	}
	
	/**
	 * 
	 */
	public static function factory( $classe ) {
		
		$c = self::CLASS_PATH . $classe ;
		if (class_exists( $c ))
			return new $c;
			
		$r = include dirname(__FILE__).'/Classes/$classe/$classe.php';
		if ( !$r )
			throw new Exception( __METHOD__. ": can't load class $classe" );
			
		if ( !class_exists( $c ))
			throw new Exception( __METHOD__. ": can't find class $classe" );
		
		return new $c;		
	}
	/**
	 * 
	 */
	public static function callMethod( $method, $args ) {

		if ( is_null( self::$key ) || is_null( self::$skey) )
			throw new Exception( __METHOD__.": api_key not set");
	
		$method = strtolower( $method );
	
		$c = self::CLASS_PATH . 'Method_'. $method ;
		$m = "Methods/$method.php";
		
		if (class_exists( $c ))
			return self::executeMethod ( $c , $args );
			
		$r = include dirname(__FILE__).'/'.$m;
		if ( !$r )
			throw new Exception( __METHOD__. ": can't load class $c associated with method $m" );
			
		if ( !class_exists( $c ))
			throw new Exception( __METHOD__. ": can't find class $c associated with method $m" );

		return self::executeMethod ( $c , $args );		
	}
	/**
	 * 
	 */
	protected static function executeMethod( &$classe, &$args ) {


		$o = new $classe( self::$key, self::$skey, $args );

		return $o->execute();
	}
	
}//end-of-class


//EOF