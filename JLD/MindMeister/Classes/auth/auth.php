<?php
/**
 * JLD_MindMeister
 *  
 *
 * @author Jean-Lou Dupont
 * @version @@package-version@@
 * @package MindMeister
 * @category OnlineTools
 * @example
 */

class JLD_MindMeister_auth 
	extends JLD_MindMeister_Object {

	var $auth = null;

	public function __construct( $obj ) {
	
		$this->auth = (string) $obj->auth;
	}

	public function getValue() {
		return $this->auth;
	}
	
}//end definition