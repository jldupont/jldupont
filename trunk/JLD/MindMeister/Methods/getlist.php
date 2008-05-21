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

class JLD_MindMeister_method_getlist 
	extends JLD_MindMeister_Method {
	
	const METHOD = 'mm.maps.getList';
	
	public function __construct( &$key, &$secret, &$args ) {

		$this->method = self::METHOD;

		parent::__construct( $key, $secret, $args );
	}

	
}