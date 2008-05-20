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
	static $REST = 'http://www.mindmeister.com/services/rest/?method=%method%';

	/**
	 * Parameters list for this method
	 */
	var $params = array();
	
	public function __construct() {
	
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
	
	}
	/**
	 * 
	 */
	protected function formatURL( &$signature ) {
	
	}
	/**
	 * Sign the request
	 */
	protected function sign() {
	
		$ol = $this->getOrderedParamsList();
		$to = $this->getStringToSign( $ol );
		
		$api_sig = md5( $to );
	
		return $api_sig;
	}
	/**
	 * Orders the parameters in alphabetical order
	 */
	protected function getOrderedParamsList() {
	
	}
	/**
	 * Extracts the value of each parameter and
	 * concatenates those to form a string
	 */
	protected function getStringToSign( &$orderedList ) {
	
		$str = '';
		
		foreach( $orderedList as $key =>$value )
			$str .= $value;
		
		return $str;
	}
	
}//end class