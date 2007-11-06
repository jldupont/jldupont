<?php
/*
	PEAR Channel Tool: parses 'channel.xml' file given the root directory.
	Command Line Utility
	@author: Jean-Lou Dupont
	$Id$
*/
//<source lang=php>

require "PEAR/XMLParser.php";
require 'JLD/Object.php';

// use a class for namespace management.
class JLD_PearTools_Channel extends JLD_Object
{
	// REST related
	static $baseREST = '/rest';
	static $baseTAGS = '/tags';
	static $file_name = 'channel.xml';
	
	// filesystem absolute path to channel
	var $dir = null; 
	
	var $contents = null;
	var $file = null;
	var $data = null; // parsed file.
	
	// this variable will hold the channel's uri
	var $uri = null;
	
	public function __construct() 
	{
		if (self::$instance !== null)
			die( __CLASS__.': only one instance of this class can be created.' );
	}
	public static function singleton()
	{
		return parent::singleton( __CLASS__, self::thisVersion );	
	}
	public function getURI() { return $this->uri; }
	public function getRootPath() { return $this->dir; }
	public function getRESTPath() { return self::$baseREST; }
	public function getTAGSPath() { return self::$baseTAGS; }	
		
	/**
	 *
	 * @input provide the root path of the channel.
	 */
	function init( $rootPath )
	{
		$this->dir = $rootPath;

		$this->file = $this->dir.'/'.self::$file_name;
		
		$this->contents = @file_get_contents( $this->file );
		if (empty( $this->contents ))
			return;
			
		$this->uri = $this->parse( $this->contents );
	}
	/**
	 */
	protected function parse( &$contents )
	{
		$parser = new PEAR_XMLParser;
		$result = $parser->parse( $contents );
		if (!$result)
			return false;
		$data = $parser->getData();
		
		if (isset($data['name']))
			return $data['name'];
			
		return null;
	}
}
//</source>