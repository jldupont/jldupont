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

require_once 'JLD/Object/Object.php'; //includes also the 'JLD_System_Exception' class
require_once 'JLD/Cache/Cache.php';
require_once 'JLD/Registry/RegistryRepository.php';

require_once 'Zend/Gdata/Spreadsheets.php';
require_once 'Zend/Gdata/ClientLogin.php';
require_once 'Zend/Exception.php';

class JLD_GoogleDocs_RegistryRepository extends JLD_RegistryRepository
{
	const thisVersion = '$Id$';
	
	/**
	 * Mandatory configuration parameters list
	 */
	static $configParametersList = array(
		// Username
		array( 'r' => true, 'key' => 'gs_user' ),
		// Password
		array( 'r' => true, 'key' => 'gs_password' ),
		// Document		
		array( 'r' => true, 'key' => 'gs_document' ),		
		// Worksheet
		array( 'r' => true, 'key' => 'gs_worksheet' ),
	);
	/**
	 */
	var $gs_service = null;
	var $gs_client = null;
	var $gs_spreadsheetService = null;
	
	public function __construct( ) 
	{
		
	}
	/**
	 * Initialization of the configuration parameters
	 *
	 * @param mixed $parameters Configuration Array
	 */
	public function init( $parameters )
	{
		if ($this->digestConfiguration( self::$configParametersList, $parameters ) === false)
			throw new JLD_System_Exception( );

		// let the client deal with any potential error
		return $this->initGdoc( );
	}
	/**
	 * Init the Gdoc service
	 */
	protected function initGdoc()
	{
		try 
		{
			$this->gs_service = Zend_Gdata_Spreadsheets::AUTH_SERVICE_NAME;
			$this->gs_client = Zend_Gdata_ClientLogin::getHttpClient( $gs_user, $gs_password, $this->service);
			$this->gs_spreadsheetService = new Zend_Gdata_Spreadsheets($this->gs_client);
		}
		// whatever exception we catch, let's try not to be too dramatic...
		// let the client layer deal with this.
		catch( Zend_Exception $e )
		{
			return false;	
		}
		
		return true;
	}
	
// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// INHERITED METHODS
// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

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
	/**
	 * Fetches a fresh & complete copy of the registry.
	 */
	public function refresh()
	{
		
	}

}//end class
//</source>