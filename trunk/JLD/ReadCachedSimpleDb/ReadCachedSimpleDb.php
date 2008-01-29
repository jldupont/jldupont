<?php
/**
 * ReadCachedSimpleDb class
 *
 * This class implements a 'read cached' interface to Amazon's SimpleDB WEB service.
 * @author Jean-Lou Dupont
 * @version @@package-version@@
 * @package ReadCachedSimpleDb
 */
/*
 * 
 *
 */
require_once 'Amazon/SimpleDB/Client.php';
require_once 'JLD/ReadCachedSimpleDb/Interface.php';
require_once 'MDB2.php';

class ReadCachedSimpleDb extends Amazon_SimpleDB_Client implements ReadCachedSimpleDb_Interface, Amazon_SimpleDB_Interface
{
	/**
	 *
	 */
	public function __construct()
	{
		
	}	
	/**
	 *
	 */

	/**
	 *
	 */

// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// AMAZON SimpleDb interface
// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

	/**
	 * @throws ReadCachedSimpleDb_Exception
	 */
    public function createDomain($action)
	{
		require_once 'JLD/ReadCachedSimpleDb/Exception.php';	
		throw new ReadCachedSimpleDb_Exception;
	}
	/**
	 * @throws ReadCachedSimpleDb_Exception
	 */
    public function listDomains($action)
	{
		require_once 'JLD/ReadCachedSimpleDb/Exception.php';	
		throw new ReadCachedSimpleDb_Exception;
	}
	/**
	 *
	 * @throws ReadCachedSimpleDb_Exception
	 */
    public function deleteDomain($action)
	{
		require_once 'JLD/ReadCachedSimpleDb/Exception.php';	
		throw new ReadCachedSimpleDb_Exception;
	}
	/**
	 *
	 */
    public function putAttributes($action)
	{
		
	}
	/**
	 *
	 */
    public function getAttributes($action)
	{
		
	}
	/**
	 *
	 */
    public function deleteAttributes($action)
	{
		
	}
	/**
	 *
	 */
    public function query($action)
	{
		
	}


// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// Helper methods
// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

	
}