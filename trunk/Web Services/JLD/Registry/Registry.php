<?php
/**
 * @author Jean-Lou Dupont
 * @package JLD
 * @subpackage Registry
 * @version $Id$
 */
//<source lang=php> 

require 'JLD/Object/Object.php';
require 'JLD/Cache/Cache.php';
require 'JLD/AmazonS3/AmazonS3.php';

// only one instance.
JLD_Registry::singleton();

/*
 *  The Amazon access & secret keys are fetched from the cache.
 *
 *  The registry entries are assumed to be pretty much static 
 *  from a relativistic timescale point of view of $expiry.
 */
class JLD_Registry extends JLD_Object
{
	const thisVersion = '$Id$';
	
	static $expiry = 86400; // 1day.

	// session based cache.
	static $entries = null;
	var $cache = null;

	// S3 related.
	static $S3SecretKeyCacheKeyName = null;
	static $S3AccessKeyCacheKeyName = null;
	static $S3BucketNameCacheKeyName = null;
	
	static $S3accessKey = null;
	static $S3secretKey = null;
	static $S3bucketName = null;
	
	var $s3;

	public function __construct() 
	{
		self::$S3SecretKeyCacheKeyName = __CLASS__.':AmazonS3:secretKey';
		self::$S3AccessKeyCacheKeyName = __CLASS__.':AmazonS3:accessKey';		
		self::$S3BucketNameCacheKeyName = __CLASS__.':AmazonS3:registrybucketName';				
		
		if (JLD_Cache_Manager::isFake())
			die( __CLASS__.':'.__METHOD__.' requires a real cache for performance consideration' );
			
		$this->cache = JLD_Cache_Manager::getCache();
		
		// Init S3 support.
		$this->initS3();
	}
	public static function singleton()
	{
		return parent::singleton( __CLASS__, self::thisVersion );	
	}
	/**
	 */
	protected function initS3()
	{
		self::$S3accessKey = $this->cache->get( self::$S3AccessKeyCacheKeyName );
		self::$S3secretKey = $this->cache->get( self::$S3SecretKeyCacheKeyName );		
		self::$S3bucketName = $this->cache->get( self::$S3BucketNameCacheKeyName );		
		
		$this->s3 = new AmazonS3(	self::$S3secretKey,
									self::$S3accessKey );
	}
	/**
	 */
	public function get( $key )
	{
		
	}
	/**
	 *  This method will set the session, local cache & S3 store
	 *  with the required [$key] = $value pair.
	 *
	 *  If there was a failure whilst storing to S3, 'false' is returned.
	 */
	public function set( $key, $value )
	{
		self::$entries[ $key ] = $value;
		$cache->set( $key, $value, self::$expiry );
		
	}
	
} // end class

//</source>