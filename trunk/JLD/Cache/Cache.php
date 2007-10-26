<?php
/**
 * @author Jean-Lou Dupont
 * @package JLD
 * @subpackage Cache
 * @version $Id$
 */
//<source lang=php> 

// create only one instance of the following class.
new JLD_Cache_Manager;

class JLD_Cache_Manager
{
	/**
	 * Array sorted in order of preference
	 */
	static $classes = array(
		'JLD_Cache_eAccel',
		'JLD_Cache_APC',
		
		// fake cache must be last in list!
		'JLD_Cache_Fake'
	);

	static $instance = null;
	static $cache = null;

	public function __construct()
	{
		// singleton pattern
		if ( self::$instance !== null)
			return self::$instance;
		else
		{
			self::$instance = new JLD_Cache_Manager;
			self::init();	
		}
	}
	public static function isFake()
	{
		return (self::$cache instanceof JLD_Cache_Fake);	
	}
	protected function init()
	{
		foreach ( self::$classes as $classe )
			if (self::checkPresence( $classe ))
				self::$cache = new $classe;				
	}
	public static function getCache()
	{
		return self::$cache;
	}

	public static function getAvailableCaches()
	{
		$caches = array();
		
		foreach ( self::$classes as $classe )
			if (self::checkPresence( $classe ))
				array_push( $caches, $classe );

		return $caches;
	}
	
	public static function checkPresence( &$classe )
	{
		$c = 'return '.$classe.'::checkPresence();';	
		return eval( $c );
	}
	
}// end JLD_Cache_Manager

/**
 * Simple generic object store
 */
class JLD_Cache
{
	function __construct() 
	{}

	/**
	 * This method must check the availability
	 * of the cache functionality in question.
	 */
	public static function checkPresence()
	{
		/* stub */
		return false;	
	}

	public function clearCache()
	{
		/* stub */
		return false;	
	}
	/* *** THE GUTS OF THE OPERATION *** */
	/* Override these with functional things in subclasses */

	function get($key) 
	{
		/* stub */
		return false;
	}

	function set($key, $value, $exptime=0) 
	{
		/* stub */
		return false;
	}

	function delete($key, $time=0) 
	{
		/* stub */
		return false;
	}

	function lock($key, $timeout = 0) 
	{
		/* stub */
		return true;
	}

	function unlock($key) 
	{
		/* stub */
		return true;
	}

	/* *** Emulated functions *** */
	/* Better performance can likely be got with custom written versions */
	function get_multi($keys) 
	{
		$out = array();
		foreach($keys as $key)
			$out[$key] = $this->get($key);
		return $out;
	}

	function set_multi($hash, $exptime=0) 
	{
		foreach($hash as $key => $value)
			$this->set($key, $value, $exptime);
	}

	function add($key, $value, $exptime=0) 
	{
		if( $this->get($key) == false ) {
			$this->set($key, $value, $exptime);
			return true;
		}
	}

	function add_multi($hash, $exptime=0) 
	{
		foreach($hash as $key => $value)
			$this->add($key, $value, $exptime);
	}

	function delete_multi($keys, $time=0) 
	{
		foreach($keys as $key)
			$this->delete($key, $time);
	}

	function replace($key, $value, $exptime=0) 
	{
		if( $this->get($key) !== false )
			$this->set($key, $value, $exptime);
	}

	function incr($key, $value=1) 
	{
		if ( !$this->lock($key) )
			return false;

		$value = intval($value);
		if($value < 0) $value = 0;

		$n = false;
		if( ($n = $this->get($key)) !== false ) 
		{
			$n += $value;
			$this->set($key, $n); // exptime?
		}
		$this->unlock($key);
		return $n;
	}

	function decr($key, $value=1) 
	{
		if ( !$this->lock($key) ) 
			return false;

		$value = intval($value);
		if($value < 0) $value = 0;

		$m = false;
		if( ($n = $this->get($key)) !== false ) 
		{
			$m = $n - $value;
			if($m < 0) $m = 0;
			$this->set($key, $m); // exptime?
		}
		$this->unlock($key);
		return $m;
	}

	/**
	 * Convert an optionally relative time to an absolute time
	 */
	static function convertExpiry( $exptime ) 
	{
		if(($exptime != 0) && ($exptime < 3600*24*30)) 
		{
			return time() + $exptime;
		} 
		else 
		{
			return $exptime;
		}
	}
}

/**
 * This is a wrapper for APC's shared memory functions
 *
 */
class JLD_Cache_APC extends JLD_Cache 
{
	public static function checkPresence()
	{
		return function_exists( 'apc_fetch' );
	}

	public function clearCache()
	{
		return apc_clear_cache();
	}

	function get($key) 
	{
		$val = apc_fetch($key);
		if ( is_string( $val ) ) 
			$val = unserialize( $val );

		return $val;
	}
	
	function set($key, $value, $exptime=0) 
	{
		apc_store($key, serialize($value), $exptime);
		return true;
	}
	
	function delete($key, $time=0) 
	{
		apc_delete($key);
		return true;
	}
}

/**
 * This is a wrapper for eAccelerator's shared memory functions.
 *
 */
class JLD_Cache_eAccel extends JLD_Cache 
{
	public static function checkPresence()
	{
		return function_exists( 'eaccelerator_get' );		
	}

	public function clearCache()
	{
		return eaccelerator_clear();
	}

	function get($key) 
	{
		$val = eaccelerator_get( $key );
		if ( is_string( $val ) ) 
			$val = unserialize( $val );

		return $val;
	}

	function set($key, $value, $exptime=0) 
	{
		eaccelerator_put( $key, serialize( $value ), $exptime );
		return true;
	}

	function delete($key, $time=0) 
	{
		eaccelerator_rm( $key );
		return true;
	}

	function lock($key, $waitTimeout = 0 ) 
	{
		eaccelerator_lock( $key );
		return true;
	}

	function unlock($key) 
	{
		eaccelerator_unlock( $key );
		return true;
	}
}

class JLD_Cache_Fake
{
	public static function checkPresence() { return true; }
	public function clearCache() { return true; }

	function add ($key, $val, $exp = 0) { return true; }
	function decr ($key, $amt=1) { return null; }
	function delete ($key, $time = 0) { return false; }
	function get ($key) { return null; }
	function get_multi ($keys) { return array_pad(array(), count($keys), null); }
	function incr ($key, $amt=1) { return null; }
	function replace ($key, $value, $exp=0) { return false; }
	function set ($key, $value, $exp=0){ return true; }
}
//</source>