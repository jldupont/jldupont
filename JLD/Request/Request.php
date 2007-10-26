<?php
/**
 * @author Jean-Lou Dupont
 * @package JLD
 * @subpackage Request
 * @version $Id$
 */
//<source lang=php> 

// only one of those...
JLD_Request::singleton();

class JLD_Request
{
	var $requestTime;
	
	var $errorMsg;
	var $error;

	static $verboten = array(
		'GLOBALS',
		'_SERVER',
		'HTTP_SERVER_VARS',
		'_GET',
		'HTTP_GET_VARS',
		'_POST',
		'HTTP_POST_VARS',
		'_COOKIE',
		'HTTP_COOKIE_VARS',
		'_FILES',
		'HTTP_POST_FILES',
		'_ENV',
		'HTTP_ENV_VARS',
		'_REQUEST',
		'_SESSION',
		'HTTP_SESSION_VARS'
	);
	
	public function __construct()
	{
		$this->error = false;
		$this->errorMsg = null;
		
		$this->requestTime = microtime(true);
		
		@ini_set( 'allow_url_fopen', 0 ); # For security
		
		$this->error = $this->fixRegisterGlobals();	
	}
	public static function singleton()
	{
		if ( self::$instance === null )
			self::$instance = new JLD_Request;	
		
		return self::$instance;
	}
	
	protected function fixRegisterGlobals()
	{
		$error = false;
		
		if ( !ini_get( 'register_globals' ) )
			return true;

		if ( isset( $_REQUEST['GLOBALS'] ) ) 
		{
			$this->errorMsg = '<a href="http://www.hardened-php.net/index.76.html">$GLOBALS overwrite vulnerability</a>';
			return false;
		}

		global $_REQUEST;
		foreach ( $_REQUEST as $name => $value ) 
		{
			if( in_array( $name, self::$verboten ) ) 
			{
				$error = true;
				$this->errorMsg = "register_globals security paranoia: trying to overwrite superglobals.";
			}
			unset( $GLOBALS[$name] );
		}

		return $error;
	}

	public function isError()
	{
		return $this->error;	
	}	
	public function getErrorMsg()
	{
		return $this->errorMsg;	
	}
} // end class

//</source>