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

class JLD_MindMeister {

	const CLASS_PATH = 'JLD_MindMeister_';

	/**
	 * REST API end-point
	 */
	static $REST = 'http://www.mindmeister.com/services/rest/';
	
	/**
	 * No need to instantiate from this class
	 */
	protected function __construct() {
	}
	/**
	 * 
	 */
	public static function factory( $classe ) {
		
		$c = self::CLASS_PATH . $classe ;
		if (class_exists( $c ))
			return new $c;
			
		$r = @include 'Classes/$classe/$classe.php';
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

		$c = self::CLASS_PATH . 'Method_'. $method ;
		if (class_exists( $c ))
			return new $c;
			
		$r = @include 'Methods/$method.php';
		if ( !$r )
			throw new Exception( __METHOD__. ": can't load class $c" );
			
		if ( !class_exists( $c ))
			throw new Exception( __METHOD__. ": can't find class $classe" );
		
		return new $c;		
	
	
	}
	
}//end-of-class


//EOF