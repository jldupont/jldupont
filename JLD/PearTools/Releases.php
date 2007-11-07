<?php
/*
	PEAR Channel Tool

	@author: Jean-Lou Dupont
	$Id$
*/
//<source lang=php>

require_once "PEAR/XMLParser.php";
require_once 'JLD/Object/Object.php';

// use a class for namespace management.
class JLD_PearTools_Releases extends JLD_Object
{
	const thisVersion = '$Id$';
	static $baseReleases = '/r';	

	static $thisDir = null;	

	var $channel;
	var $rootPath;
	var $baseREST;
	var $restPathR;
	var $channelURI;
	
	public function __construct( $version ) 
	{
		return parent::__construct( $version );
	}
	public static function singleton()
	{
		return parent::singleton( __CLASS__, self::thisVersion );	
	}
	public function init( &$channel )
	{
		$this->channel = $channel;

		self::$thisDir = dirname( __FILE__ );
		$this->channel = $channel;
		$this->rootPath = $this->channel->getRootPath();
		$this->baseREST = $this->channel->getRESTPath();
		$this->restPathR = $this->rootPath . $this->baseREST . self::$baseReleases;
		$this->channelURI = $this->channel->getURI();
	}
	/**
	 */
	public function createVersionFile( $packageName, $version, $stability, &$msg )
	{
		$msg = '';
		
		$file = $this->genFilePath( $packageName ).'/'."$version.xml";
		
		$tpl = $this->getTemplate( 'version' );
		if (empty( $tpl ))
		{
			$msg = 'error reading "version.xml.tpl" template file';
			return false;
		}
		
		$this->replaceMagicWords( $tpl, $this->channelURI, $packageName, $version, $stability );
		
		$msg = 'error writing '."$version.xml file";
		$len = strlen( $tpl );
		$bytes_written = @file_put_contents( $file, $tpl );

		return ($len === $bytes_written);
	}
	protected function genFilePath( $packageName )
	{
		return $this->restPathR . '/' . strtolower( $packageName );
	}
	protected function getTemplate( $name )
	{
		$file = self::$thisDir."/Templates/$name.xml.tpl";
		$contents = @file_get_contents( $file );
		return $contents;
	}
	protected function replaceMagicWords( &$tpl, $channel, $packageName, $version, $stability = 'stable' )
	{
		$tpl = str_replace( '$packageH$', $packageName, $tpl);
		$tpl = str_replace( '$packageL$', strtolower($packageName), $tpl);		
		$tpl = str_replace( '$channel$', $channel, $tpl);
		$tpl = str_replace( '$version$', $version, $tpl);
		$tpl = str_replace( '$stability$', $stability, $tpl);		
						
	}
}
//</source>