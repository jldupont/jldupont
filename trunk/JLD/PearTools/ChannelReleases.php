<?php
/*
	PEAR Channel Releases

	@author: Jean-Lou Dupont
	$Id$
*/
//<source lang=php>

require_once "PEAR/XMLParser.php";
require_once 'JLD/PearTools/PearObject.php';
require_once 'JLD/PearTools/Channel.php';
require_once 'JLD/Directory/Directory.php';


// use a class for namespace management.
class JLD_PearTools_ChannelReleases extends JLD_PearObject
{
	const thisVersion = '$Id$';

	// Template related
	const tpl_v = '/Templates/version.xml.tpl';

	// relative to the REST structure; this is standard.
	static $baseReleases = '/r';
		
	public function __construct( $version ) 
	{
		return parent::__construct( $version );
	}
	public static function singleton()
	{
		return parent::singleton( __CLASS__, self::thisVersion );	
	}
	/**
	 * The required variables must have been set prior to calling this method.
	 * (see initVars in PearObject)
	 */
	public function createVersionFile( )
	{
		$tpl = $this->getTemplate( self::tpl_v );
		if (empty( $tpl ))
			return false;
		
		$c = $this->replaceMagicWords2( $tpl );
		
		$v = $this->package_version;
		
		$file =  $this->buildFileSystemRestPath( self::$baseReleases );
		$file .= '/'.$this->package_name.'/'."$v.xml";
		
		return $this->writeFile( $file, $c );
	}
	/**
	 * Create deps.$version.txt file
	 * Must read & parse source package.xml file,
	 * extract 'depedencies' section and serialize.
	 */
	public function createDepsFile( )
	{
		$v = $this->package_version;
		$file  = $this->buildFileSystemRestPath( self::$baseReleases );
		$file .= '/'.$this->package_name."/deps.$v.txt";
		return $this->writeFile( $file, $this->package_dependencies );
	}
	/**
	 * Scans the package's /r REST directory and find 
	 * all releases. This is accomplished by reading in
	 * all the files of the pattern 'package.$version.xml'
	 */
	public function getAllReleases()
	{
		$pattern = '/package\.(.*)\.xml/';
		$path = $this->buildFileSystemRestPath( self::$baseReleases );
		$raw = JLD_Directory::getDirectoryInformation( $path, $path, true, false );		
		$files = array();

		if ( empty( $raw ) )
			foreach( $raw as )
	}
	
}//end class
//</source>