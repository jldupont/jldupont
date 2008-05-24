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
/*
 1) http://www.mindmeister.com/services/auth/?api_key=abc123
 2) http://www.mindmeister.com/services/auth/?api_key=abc123&perms=delete
 3) http://www.mindmeister.com/services/auth/?api_key=abc123&perms=delete&api_sig=zxy987
 
 */
class JLD_MindMeister_method_authen 
	extends JLD_MindMeister_Method {

	/**
	 * REST end-point for this method
	 */
	const REST = 'http://www.mindmeister.com/services/authen/?api_key=%api_key%&perms=%perms%&api_sig=%api_sig%';
	
	/**
	 * not really required
	 */
	const METHOD = 'mm.authen';
	
	/**
	 * Reference list for parameters
	 */
	static $refParams = array(
		'perms'		=> array( 'l' => true, 'a' => array( 'read', 'write', 'delete' ) )
	);
	
	public function __construct( &$key, &$secret, &$args  ) {

		// not really needed in this case
		$this->method = self::METHOD;

		parent::__construct( $key, $secret, $args, self::REST );
	}
	/**
	 * Returns the reference list for parameters of this method
	 * Used in the base class for parameter verification
	 */
	protected function getRefList() {
	
		return self::$refParams;
	}
	
}