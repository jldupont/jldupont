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
		if (self::$instance !== null)
			die( __CLASS__.': only one instance of this class can be created.' );
			
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
	 *  Returns the registry value in $value
	 *  
	 *  Returns 'true' if $value is in 'PHP format'
	 *  Returns 'false' if $key was not found
	 *  Returns 'null' if $value retrieved is in 'raw' format
	 *   i.e. coming straight from the S3 store.
	 *
	 *  When the data comes directly from the S3 store,
	 *  it is the responsibility of the requester to 'parse' the document
	 *  to a usage format.
	 */
	public function get( $key, &$value )
	{
		// check if we can get lucky with the session scoped cached.
		if (isset( self::$entries[ $key ] ))
		{
			$value = self::$entries[ $key ];
			return true;
		}
			
		// next, try with the system scoped cache
		$value = $this->cache( $key );
		if ( $value !== false )
			return true;
		
		// lastly, pull from S3 store...
		$result = $this->s3->getObject( self::$bucketName, $key, $value );
		if ($result !== true)
			return null;
	}
	/**
	 *  This method will set the LOCAL session & local caches
	 *  with the required [$key => $value] pair.
	 *
	 *  NOTE: this method DOES NOT update the 'permanent' registry on S3.
	 */
	public function setLocal( $key, $value )
	{
		self::$entries[ $key ] = $value;
		
		// this shouldn't fail... some init check has already been done.
		$this->cache->set( $key, $value, self::$expiry );

		return true;		
	}
	/**
	 *  This function is used to update the S3 store.
	 *  If there was a failure whilst storing to S3, 'false' is returned.	 
	 */
	public function update( $key, $value, $MIMEType = null )
	{
		return $this->s3->putObject( self::$bucketName, $key, $value, $MIMEType );		
	}
	
} // end class

//</source>