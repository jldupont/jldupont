<?php
/**
 * JLD_MindMeister_Method
 *  
 *
 * @author Jean-Lou Dupont
 * @version @@package-version@@
 * @package MindMeister
 */

	abstract
class JLD_MindMeister_Method {

	/**
	 * REST API end-point
	 */
	const DEFAULT_REST = 'http://www.mindmeister.com/services/rest/?api_key=%api_key%&method=%method%&api_sig=%api_sig%';

	/**
	 * List of parameters that are not to be included when
	 * calculating the signature
	 */
	static $excludeFromSignature = array(
		'api_sign', 'api_key', 'secret_key'
	);
	
	/**
	 * Parameters list for this method
	 */
	var $params = array();
	
	var $args = null;
	
	var $method = null;
	
	var $rep_headers = null;
	var $rep_body    = null;
	var $rep_code    = null;
	
	var $rest = null;
	
	public function __construct( &$api_key, $secret_key, &$args, $rest = null ) {
	
		$this->setParam( 'api_key' ,    $api_key );
		$this->setParam( 'secret_key' , $secret_key );		

		// don't include in $params just yet...
		$this->args = $args;
		
		// sub-classes should update this info if required.
		if ( is_null( $rest ) )
			$this->rest = self::DEFAULT_REST;
		else
			$this->rest = $rest;
	}
	/**
	 * 
	 */
	protected function setParam( $key, $value ) {
	
		$this->params[ $key ] = $value;
		return $this;
	}
	/**
	 * 
	 */
	protected function getParam( $key ) {
	
		return $this->params[ $key ];
	}
	/**
	 * Verify the parameter list given a reference list
	 * 
	 * 1) Verify that mandatory parameters are specified
	 * 2) Verify allowable values
	 */
	protected function verifyParamsList( ) {
	
		$refListe = $this->getRefList();
		
		$pl = array();
	
		foreach( $refListe as $key =>$entry ) {
		
			if ()
		}
		
		return $pl;
	}
	
	/** 
	 * Needs to be defined in derived classes.
	 */
	abstract protected function getRefList();
	
	/**
	 * 
	 */
	public function execute() {
		
		// get the signature
		$api_sign = $this->sign();
		$this->setParam( 'api_sign', $api_sign );
	
		$url = $this->formatURL( );
		
		var_dump( $url );
		die;
		
		return $this->doRequest( $url );
	}
	/**
	 * 
	 */
	protected function formatURL( ) {
	
		$url = $this->rest;
		
		foreach( $this->params as $key => $value ) {
			$url = str_replace( '%' . $key . '%', $this->getParam( $key ), $url );	
		}
	
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
		
		foreach( $orderedList as $key =>$value ) {
			if ( !in_array( $key, self::$excludeFromSignature ) )
				$str .= $value;			
		}
		
		return $str;
	}
	
}//end class