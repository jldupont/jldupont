<?php
/**
 * @author Jean-Lou Dupont
 * @package JLD
 * @version $Id$
 */
//<source lang=php> 

abstract class JLD_Object
{
	static $pClass = null;
	static $instance = null;
	static $version = null;
	
	public static function singleton( $pClass = null, $version = null)
	{
		if ( self::$instance !== null)	
			return self::$instance;
		
		if (empty($pClass))
			die (__CLASS__.':'.__METHOD__." requires a valid class name." );
		
		self::$version = $version;
		self::$pClass = $pClass;
		
		self::$instance = new $pClass;
		
		return self::$instance;
	}
	
	protected static function getCacheKey( $var )
	{
		return 'JLD:'.self::$pClass.":$var";
	}
}
//</source>