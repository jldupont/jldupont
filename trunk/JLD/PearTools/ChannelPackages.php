<?php
/*
	PEAR Channel Packages

	@author: Jean-Lou Dupont
	$Id$
*/
//<source lang=php>

require_once "PEAR/XMLParser.php";
require_once 'JLD/PearTools/PearObject.php';
require_once 'JLD/PearTools/Channel.php';
require_once 'JLD/Directory/Directory.php';


// use a class for namespace management.
class JLD_PearTools_ChannelPackages extends JLD_PearObject
{
	const thisVersion = '$Id$';

	// Template related
	const tpl_i = '/Templates/info.xml.tpl2';

	// relative to the REST structure; this is standard.
	static $basePackages = '/p';
	var $rootPath  = null;
	var $baseREST  = null;
	var $restPathP = null;
		
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
		if (!is_object( $channel ))
			throw new Exception('invalid channel object');
		
		$this->channel = $channel;
		
		// we'll be needing these parameters in the templating process...
		$this->setVar('channel_name',	$this->channel->getName());
		$this->setVar('base_rest', 		$this->channel->getRESTPath());
		$this->setVar('base_packages',	self::$basePackages );		
		
		$this->rootPath = $this->channel->getRootPath();
		$this->baseREST = $this->channel->getRESTPath();
		$this->restPathP = $this->rootPath . $this->baseREST . self::$basePackages;
	}
	/**
	 * Adds a package directory in the REST structure
	 */
	public function addPackageDirectory( $name )
	{
		$dir = $this->restPathP.'/'.$name;
		if (is_dir( $dir ))
			return true;
			
		$result = @mkdir( $dir );	
			
		return $result;
	}
	/**
	 * Creates the 'info.xml' file based on a template.
	 */
	public function	createPackageInfoFile( $packageName, $categoryName )
	{
		$this->setVar( 'category_name', $categoryName );
		$this->setVar( 'package_name', $packageName );		
				
		$tpl = $this->getTemplate( self::tpl_i );
		if (empty( $tpl ))
			throw new Exception( 'could not access "info.xml" template' );
			
		$c = $this->replaceMagicWords2( $tpl );
		$len = strlen( $c );
		$file = $this->restPathP.'/'.$packageName.'/info.xml';
		$bytes_written = @file_put_contents( $file, $c );
		return ( $len === $bytes_written );
	}
}
//</source>