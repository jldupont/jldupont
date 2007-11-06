<?php
/*
	PEAR Channel Tool: parses the 'categories' folder of the REST interface.
	@author: Jean-Lou Dupont
	$Id$
*/
//<source lang=php>

require_once "PEAR/XMLParser.php";
require_once 'JLD/Object.php';
require_once 'JLD/PearTools/Channel.php';
require_once 'JLD/Directory/Directory.php';

// use a class for namespace management.
class JLD_PearTools_Categories extends JLD_Object implements Iterator
{
	var $channel = null;
	var $categories = array();
	
	// Iterator Interface
	public function current() { return $this->categories->current(); }
	public function key() { return $this->categories->key(); }
	public function next() { return $this->categories->next(); }
	public function rewind() { return $this->categories->rewind(); }
	public function valid() { return $this->categories->valid(); }	
	
	public function __construct() {}
	public static function singleton()
	{
		return parent::singleton( __CLASS__, self::thisVersion );	
	}
	/**
	 */
	public function init( &$channel )
	{
		$this->channel = $channel;
		$this->categories = $this->readAll();
	}
	/**
	 */
	protected function readAll()
	{
		$rootPath = $this->channel->getRootPath();
		$baseREST = $this->channel->getRESTPath();
		$restPath = $rootPath . $baseREST;
		
		return JLD_Directory::getDirectoryInformation( $restPath, $rootPath, true, true );
	}
}
//</source>