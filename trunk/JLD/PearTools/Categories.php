<?php
/*
	PEAR Channel Tool: parses the 'categories' folder of the REST interface.
	@author: Jean-Lou Dupont
	$Id$
*/
//<source lang=php>

require_once "PEAR/XMLParser.php";
require_once 'JLD/Object/Object.php';
require_once 'JLD/PearTools/Channel.php';
require_once 'JLD/Directory/Directory.php';
require_once 'JLD/PearTools/Xml.php';
require_once 'PEAR/Exception.php';

// use a class for namespace management.
class JLD_PearTools_Categories extends JLD_Object implements Iterator
{
	const thisVersion = '$Id$';
	static $baseCategories = '/c';
	
	var $channel = null;
	var $categories = array();
	
	static $thisDir;
	static $tplDir = '/Categories';
	
	//
	var $rootPath = null;
	var $baseREST = null;
	var $restPathC = null;
	
	public function getAll() { return $this->categories; }
	
	// Iterator Interface
	public function current() { return $this->categories->current(); }
	public function key() { return $this->categories->key(); }
	public function next() { return $this->categories->next(); }
	public function rewind() { return $this->categories->rewind(); }
	public function valid() { return $this->categories->valid(); }	
	
	public function __construct( $version ) 
	{
		return parent::__construct( $version );		
	}
	public static function singleton()
	{
		return parent::singleton( __CLASS__, self::thisVersion );	
	}
	/**
	 */
	public function init( &$channel )
	{
		self::$thisDir = dirname( __FILE__ );
		$this->channel = $channel;
		$this->rootPath = $this->channel->getRootPath();
		$this->baseREST = $this->channel->getRESTPath();
		$this->restPathC = $this->rootPath . $this->baseREST . self::$baseCategories;
		$this->categories = $this->readAll();
	}
	/**
	 */
	protected function readAll()
	{
		// no need to get resursive here.
		$cats = JLD_Directory::getDirectoryInformation( $this->restPathC, $this->restPathC, true, true );
		
		// strip off leading /
		foreach( $cats as &$cat )
			$cat['name'] = substr( $cat['name'], 1);
		
		return $cats;
	}
	/**
	 *
	 */
	public function addRelease( $categoryName, $packageName, $release )
	{
		// get the 'packageinfo.xml' file from the desired category.
		$contents = $this->getPackageInfoFile( $categoryName );
		if (empty( $contents ))
			throw new PEAR_Exception( 'packageinfo.xml file is empty', 0 );
		
		$pif = new JLD_Packagesinfo( $contents );
		
		echo $pif->get();
		
	}
	/**
	 */
	public function getPackageInfoFile( $cName )
	{
		$file = $this->restPathC.'/'.$cName.'/packagesinfo.xml';
		return @file_get_contents( $file );
	}
	/**
	 */

}

class JLD_Packagesinfo extends JLD_PearTools_Xml
{
static $map = array(
// Elements found in 'packagesinfo.xml'
'f|attribs'		=> array( 'type' => 'attr','tpl' => '<f %attribs% >%n%%contents%%n%' ),
'f|pi' 			=> array( 'type' => 'br',	'tpl' => '<pi>%n%%contents%%n%</pi>%n%'),
'f|pi|p' 		=> array( 'type' => 'br',	'tpl' => '<p>%n%%contents%%n%</p>%n%'),	
'f|pi|p|n' 		=> array( 'type' => 'leaf',	'tpl' => '<n>%contents%</n>%n%'),								
'f|pi|p|c'		=> array( 'type' => 'leaf',	'tpl' => '<c>%contents%</c>%n%'),								
'f|pi|p|ca'		=> array( 'type' => 'attr',	'tpl' => '<ca %attribs%>%contents%</ca>%n%'),
'f|pi|p|l'		=> array( 'type' => 'leaf', 'tpl' => '<l>%contents%</l>%n%'),
'f|pi|p|s'		=> array( 'type' => 'leaf', 'tpl' => '<s>%contents%</s>%n%'),
'f|pi|p|d'		=> array( 'type' => 'leaf', 'tpl' => '<d>%contents%</d>%n%'),
'f|pi|p|r'		=> array( 'type' => 'attr', 'tpl' => '<r %attribs% />%n%'),
'f|pi|a' 		=> array( 'type' => 'br', 	'tpl' => '<a>%n%%contents%%n%</a>%n%'),
'f|pi|a|r'		=> array( 'type' => 'br', 	'tpl' => '<r>%n%%contents%%n%</r>%n%'),
'f|pi|a|r|v'	=> array( 'type' => 'leaf', 'tpl' => '<v>%contents%</v>%n%'),
'f|pi|a|r|s' 	=> array( 'type' => 'leaf', 'tpl' => '<s>%contents%</s>%n%'),
);

	public function __construct( &$contents )
	{
		$this->data = $this->parse( $contents );
	}
	protected function parse( &$contents )
	{
		$parser = new PEAR_XMLParser;
		$result = $parser->parse( $contents );
		if (!$result)
			return false;
		return $parser->getData();
	}
	public function get()
	{
		$this->emap = self::$map;
		$result = $this->getXML( 'f', $this->data );
		$result .= "\n</f>\n";
		return $result;
	}
}

//</source>