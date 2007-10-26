<?php
/**
 * @author Jean-Lou Dupont
 * @package JLD
 * @subpackage AutoLoader
 * @version $Id$
 */
//<source lang=php> 

require 'JLD/Object/Object.php';
require 'JLD/Cache/Cache.php';
require 'JLD/Directory/Directory.php';

class JLD_AutoLoader extends JLD_Object
{
	const thisCacheKeyVar = 'liste';
	
	static $cList = array();
	
	public function __construct() 
	{
		spl_autoload_register( array( __CLASS__, 'load' ) );		
		self::initFromCache();
	}
	public static function singleton()
	{
		return parent::singleton( __CLASS__ );	
	}
	public static function getList()
	{
		return self::$cList;	
	}
	public static function add( $classe, $filepath )
	{
		self::$cList[ $classe ] = $filepath;
	}
	protected static function initFromCache()
	{
		$fake = JLD_Cache_Manager::isFake();
		// if the cache is fake, then go the the lengthy process...
		if ($fake === true)
			return self::initFromFileSystem();
		
		$cache = JLD_Cache_Manager::getCache();
		
		$key = self::getCacheKey( self::thisCacheKeyVar );
		
		self::$cList = $cache->get( $key );
	}
	/**
	 * Goes through the 'JLD/' folder hierarchy
	 */
	public static function initFromFileSystem()
	{
		$pear = JLD_Directory::getPearIncludePath();
		if (empty( $pear ))
			die(__CLASS__.': pear include path not found.');
		
		$files = JLD_Directory::getDirectoryInformation( $pear, 'JLD', true );
	}
	public static function load() 
	{
		
	}
} // end class

//</source>