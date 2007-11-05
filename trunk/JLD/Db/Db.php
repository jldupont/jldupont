<?php
/**
 * @author Jean-Lou Dupont
 * @package JLD
 * @subpackage Db
 * @version $Id$
 */
//<source lang=php> 

require 'JLD/Object/Object.php';

class JLD_Db extends JLD_Object
{
	const thisVersion = '$Id$';
		
	public function __construct() 
	{
		if (self::$instance !== null)
			die( __CLASS__.': only one instance of this class can be created.' );
	}
	public static function singleton()
	{
		return parent::singleton( __CLASS__, self::thisVersion );	
	}

}
//</source>