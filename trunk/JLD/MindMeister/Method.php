<?php
/**
 * JLD_MindMeister_Method
 *  
 *
 * @author Jean-Lou Dupont
 * @version @@package-version@@
 * @package MindMeister
 */

class JLD_MindMeister_Method {

	/**
	 * REST API end-point
	 */
	static $REST = 'http://www.mindmeister.com/services/rest/?api_key=%api_key%&method=%method%&api_sig=%api_sig%';

	/**
	 * Parameters list for this method
	 */
	var $params = array();
	
	var $args = null;
	
	var $api_key = null;
	var $secret_key = null;
	
	var $method = null;
	
	var $rep_headers = null;
	var $rep_body    = null;
	var $rep_code    = null;
	
	
	public function __construct( &$api_key, $secret_key, &$args ) {
	
		$this->api_key = $api_key;
		$this->secret_key = $secret_key;
		
		$this->args = $args;
	}
	/**
	 * Verify the parameter list given a reference list
	 */
	protected function verifyParamsList( &$refListe ) {
	
		$pl = array();
	
		foreach( $refListe as $key =>$entry ) {
		
		}
		
		return $pl;
	}
	
	/**
	 * 
	 */
	public function execute() {

		// get the signature
		$api_sign = $this->sign();
	
		if ( is_null( $this->method) )
			throw new Exception( __METHOD__.": method name is not initialized" );
			
		$url = $this->formatURL( $this->method, $api_sign );
		
		var_dump( $url );
		die;
		
		return $this->doRequest( $url );
	}
	/**
	 * 
	 */
	protected function formatURL( &$method, &$signature ) {
	
		$url = str_replace( '%method%',  $method, self::$REST );
		$url = str_replace( '%api_key%', $this->api_key, $url );
		$url = str_replace( '%api_sig%', $signature, $url );
		
		return $url;
	
	}
	protected function doRequest( &$url ) {
	
		$request =& new HTTP_Request( $url );
										
		// REDIRECTS are a requirement
		$request->_allowRedirects = true;
		
		$request->setMethod( "GET" );

		try
		{
			$exception = false;
			$code = $request->sendRequest();			
		}
		catch(Exception $e)
		{
			$exception = true;
		}
		
		if ( PEAR::isError( $code ) || $exception )
			return false;

	    $this->rep_headers = $request->getResponseHeader();
		$this->rep_body    = $request->getResponseBody();
		$this->rep_code    = $request->getResponseCode();

		return ( $this->rep_code == 200 );
	}
	/**
	 * Sign the request
	 */
	protected function sign() {

		$key = $this->secret_key;
		$ol = $this->getOrderedParamsList();
		$to = "$key".$this->getStringToSign( $ol );
 
		$api_sig = md5( $to );
	
		return $api_sig;
	}
	/**
	 * Orders the parameters in alphabetical order
	 */
	protected function getOrderedParamsList() {
	
		if ( empty( $this->params ))
			return array();
	
		$r = ksort( $this->params, SORT_STRING );
		
		if ( !$r )
			throw new Exception( __METHOD__.": can't sort parameters list" );
	}
	/**
	 * Extracts the value of each parameter and
	 * concatenates those to form a string
	 */
	protected function getStringToSign( &$orderedList ) {

		if ( empty( $orderedList ))
			return '';

		$str = '';
		
		foreach( $orderedList as $key =>$value )
			$str .= $value;
		
		return $str;
	}
	
}//end class