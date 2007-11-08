<?php
/**
 * @author Jean-Lou Dupont
 * @package JLD
 * @subpackage DbManager
 * @version $Id$
 */
//<source lang=php> 

require 'JLD/Object/Object.php';

class JLD_Db_Manager extends JLD_Object
{
	const thisVersion = '$Id$';
	
	/**
	 *
	 */
	public function __construct( $version ) 
	{
		if (self::$instance !== null)
			die( __CLASS__.': only one instance of this class can be created.' );
		return parent::__construct( $version );			
	}
	/**
	 * Returns a singleton for this class.
	 */
	public static function singleton()
	{
		return parent::singleton( __CLASS__, self::thisVersion );	
	}
	/**
	 *
	 */	
	public function init() 
	{
		
	}	
	/**
	 *
	 */	
	public function factory()
	{
		
	}
	
} // JLD_Db_Manager

//</source>