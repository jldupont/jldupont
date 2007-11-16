<?php
/**
 * @author Jean-Lou Dupont
 * @package Object
 * @version $Id$
 */
//<source lang=php> 

require 'JLD/System/Exception.php';

abstract class JLD_Object
{
	const JLD_Object_Version = '$Id$';
	static $instance = array();
	var $version = null;
	
	/**
	 * Class variables
	 * @var mixed
	 */
	var $vars = array();
	/**
	 * Constructor
	 * Optional 'version' parameter when used in conjunction with
	 * the singleton functionality.
	 */
	public function __construct( $version = null )
	{
		$this->version = $version;
	}
	/**
	 * Singleton interface
	 * 
	 * @param string $pClass
	 * @param string $version
	 * @return JLD_Object
	 */
	public static function singleton( $pClass = null, $version = null)
	{
		if ( self::$instance[$pClass] !== null)	
			return self::$instance[$pClass];
		
		if (empty($pClass))
			throw new JLD_System_Exception(__CLASS__.':'.__METHOD__." requires a valid class name." );
		
		self::$instance[$pClass] = new $pClass( $version );
		
		return self::$instance[$pClass];
	}
	/**
	 * Get class version
	 * @return string
	 */
	public function getVersion()
	{
		return $this->version;
	}
	/**
	 * Generates a 'unique' key for this object class.
	 * Uses the top level namespace 'JLD'.
	 *
	 * @param string $var
	 */
	protected static function getCacheKey( $var )
	{
		return 'JLD:'.self::$pClass.":$var";
	}
	/**
	 * Catch-all parameter 'setter'
	 * @param string $key
	 * @param mixed $value
	 * @param mixed
	 */
	public function __set( $key, $value )
	{
		return $this->vars[$key] = $value;
	}
	/**
	 * Catch-all parameter 'getter'
	 * This function suppresses any error. 
	 *
	 * @param string $key
	 * @param mixed
	 */
	public function __get( $key )
	{
		return @$this->vars[$key];
	}
	
}//end class
//</source>