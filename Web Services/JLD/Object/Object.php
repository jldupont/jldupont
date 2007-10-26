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
	
	public static function singleton( $pClass )
	{
		if ( self::$instance !== null)	
			return self::$instance;
			
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