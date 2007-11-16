<?php
/**
 * RegistryRepository abstract class
 *  This class is used as a base for the RegistryRepository classes.
 *  A Registry Repository class allows interfacing to an repository.
 *
 * @author Jean-Lou Dupont
 * @package JLD
 * @subpackage Registry
 * @version $Id$
 */
//<source lang=php> 

require 'JLD/Object/Object.php';

abstract class JLD_RegistryRepository extends JLD_Object
{
	/**
	 * This class' version
	 */
	const thisVersion = '$Id$';

	/**
	 * Gets a value corresponding to a key in the registry.
	 * @param string $key
	 * @param object $value reference to a object that will hold the value
	 * @return bool Returns TRUE/FALSE
	 */
	public function getKey( $key, &$value );
	
	/**
	 * Gets the integer expiry timeout in seconds associated with a given key.
	 * @param string $key
	 * @return integer Expiry timeout value in seconds.
	 */
	public function getExpiry( $key );
	
}//end class
//</source>