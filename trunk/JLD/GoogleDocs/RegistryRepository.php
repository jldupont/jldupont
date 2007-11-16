<?php
/**
 * RegistryRepository based on GoogleDocs
 *
 * @author Jean-Lou Dupont
 * @package GoogleDocs
 * @subpackage RegistryRepository
 * @version $Id$
 */
//<source lang=php> 

require 'JLD/Object/Object.php'; //includes also the 'JLD_System_Exception' class
require 'JLD/Cache/Cache.php';
require 'JLD/Registry/RegistryRepository.php';

class JLD_GoogleDocs_RegistryRepository extends JLD_RegistryRepository
{
	const thisVersion = '$Id$';
	
	public function __construct( ) 
	{
		
	}

	/**
	 * Gets a value corresponding to a key in the registry.
	 * @param string $key
	 * @param object $value reference to a object that will hold the value
	 * @return bool Returns TRUE/FALSE
	 */
	public function getKey( $key, &$value )
	{
		
	}
	/**
	 * Gets the integer expiry timeout in seconds associated with a given key.
	 * @param string $key
	 * @return integer Expiry timeout value in seconds.
	 */
	public function getExpiry( $key )
	{
		
	}

}//end class
//</source>