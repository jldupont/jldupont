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

class JLD_MindMeister_frob 
	extends JLD_MindMeister_Object {

	var $frob = null;

	public function __construct( $obj ) {
	
		$this->frob = (string) $obj->frob;
	}

	public function getValue() {
		return $this->frob;
	}
	
}//end definition