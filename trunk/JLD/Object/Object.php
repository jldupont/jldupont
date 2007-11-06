<?php
/**
 * @author Jean-Lou Dupont
 * @package JLD
 * @version $Id$
 */
//<source lang=php> 

abstract class JLD_Object
{
	static $instance = array();
	var $version = null;
	
	public function __construct( $version )
	{
		$this->version = $version;
	}
	
	public static function singleton( $pClass = null, $version = null)
	{
		if ( self::$instance[$pClass] !== null)	
			return self::$instance[$pClass];
		
		if (empty($pClass))
			die (__CLASS__.':'.__METHOD__." requires a valid class name." );
		
		self::$instance[$pClass] = new $pClass( $version );
		
		return self::$instance[$pClass];
	}
	
	protected static function getCacheKey( $var )
	{
		return 'JLD:'.self::$pClass.":$var";
	}
}
//</source>