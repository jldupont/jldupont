<?php
/*
	PEAR Channel Categories

	@author: Jean-Lou Dupont
	$Id$
*/
//<source lang=php>

require_once "PEAR/XMLParser.php";
require_once 'JLD/PearTools/PearObject.php';
require_once 'JLD/PearTools/Channel.php';
require_once 'JLD/Directory/Directory.php';


// use a class for namespace management.
class JLD_PearTools_ChannelCategories extends JLD_PearObject
{
	const thisVersion = '$Id$';
	const tpl_c = '/Templates/categories.xml.tpl';
	const tpl_c2= '/Templates/categories.xml.tpl2';	
	
	const tpl_i = '/Templates/info.xml.tpl';	
	const tpl_p = '/Templates/packagesinfo.xml.tpl';  // top level
	const tpl_p2= '/Templates/packagesinfo.xml.tpl2'; // package instance
	const tpl_p3= '/Templates/packagesinfo.xml.tpl3'; // release instance
	
	// relative to the REST structure; this is standard.
	static $baseCategories = '/c';
	static $baseReleases = '/r'; // because of packagesinfo.xml file...
	var $rootPath  = null;
	var $baseREST  = null;
	var $restPathC = null;
	
	// categories
	var $cats = array();

	// Magic Words: used for filling the templates
	static $magic_words = array(
		'$channel_name$'	=> 'channel_name',	 // for categories.xml
		'$all_categories$'	=> 'all_categories', // for categories.xml
		'$category_name$'	=> 'category_name',  // for categories.xml
		'$base_rest$'		=> 'base_rest',      // for categories.xml
		'$base_categories$'	=> 'base_categories',// for categories.xml		
		'$base_releases$'	=> 'base_releases',  // for packagesinfo.xml				
	);
	
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
		$this->setVar('base_categories',self::$baseCategories );		
		$this->setVar('base_releases',  self::$baseReleases );		
		
		$this->rootPath = $this->channel->getRootPath();
		$this->baseREST = $this->channel->getRESTPath();
		$this->restPathC = $this->rootPath . $this->baseREST . self::$baseCategories;
		$this->restPathR = $this->rootPath . $this->baseREST . self::$baseReleases;		
	}
// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	/**
	 * Reads all the categories from the directory structure 
	 * in the REST channel.
	 */
	public function readAll()
	{
		// no need to get resursive here.
		$raw = JLD_Directory::getDirectoryInformation(	$this->restPathC, 
														$this->restPathC, true, true );
		
		// strip off leading /
		foreach( $raw as &$e )
		{
			$e['name'] = substr( $e['name'], 1);
			$this->cats[] = $e['name'];
		}
	}
	/**
	 * Returns TRUE if the specified category exists
	 * in the current instance.
	 */
	public function existsCategory( $categoryName )	
	{
		return (in_array( $categoryName, $this->cats ));
	}
	/**
	 * Adds a category directory in the REST structure
	 */
	public function addCategoryDirectory( $name )
	{
		$dir = $this->restPathC.'/'.$name;
		if (is_dir( $dir ))
			return true;
			
		$result = @mkdir( $dir );	
		if ($result)
			$this->cats[] = $name;
			
		return $result;
	}
	/**
	 * Updates the 'categories.xml' file according to the
	 * registered categories contained in the class instance.
	 */
	public function updateCategories()
	{
		if (empty( $this->cats ))
			return null;
			
		$tpl = $this->getTemplate( self::tpl_c );	
		if (empty( $tpl ))
			throw new Exception( 'template file#1 for "categories.xml" appears invalid or non-existent');

		$tpl2 = $this->getTemplate( self::tpl_c2 );	
		if (empty( $tpl2 ))
			throw new Exception( 'template file#2 for "categories.xml" appears invalid or non-existent');
		
		$result = '';
		foreach ($this->cats as $cat)
		{
			$this->setVar( 'category_name', $cat );
			
			// format one line
			$result .= $this->replaceMagicWords2( $tpl2, self::$magic_words );	
		}
		// do replacement in the base template
		// the channel name parameter was already set.		
		$this->setVar( 'all_categories', $result );
		$final_result = $this->replaceMagicWords2( $tpl, self::$magic_words );
		
		// finally, write the file!
		$file = $this->restPathC.'/categories.xml';
		$result = $this->writeFile( $file, $final_result );
		
		return $result;
	}
	/**
	 * Updates / creates the 'info.xml' file associated with a category.
	 * Make sure the category directory exists prior to using this method.
	 * <n>$category_name$</n>
	 * <c>$channel_name$</c>
	 * <a>$category_name$</a> <!-- alias? -->
	 * <d>$description$</d>
	 */
	public function updateCategoryInfo( $name )
	{
		$tpl = $this->getTemplate( self::tpl_i );	
		if (empty( $tpl ))
			throw new Exception( 'template file for "info.xml" appears invalid or non-existent');
		
		$this->__set( 'category_name', $name );
		$this->replaceMagicWords( $tpl, self::$magic_words );
		
		// write the file
		$file = $this->restPathC.'/'.$name.'/info.xml';
		return $this->writeFile( $file, $tpl );
	}
	
// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	
	/**
	 * Updates / creates the 'packagesinfo.xml' file in the REST structure.
	 * Must read in the current file, parse it & then add the specified information.
	 */
	public function updatePackagesInfo(	$name, $packagename, $packageversion, $packagestability ) 
	{
		$file = $this->restPathC.'/'.$name.'/packagesinfo.xml';
		$c = @file_get_contents( $file );
		
		// if the file does not exists, then create one
		// from the template.
		if (empty( $c ))
			return $this->createPackageInfo( $name, $packagename, $packageversion, $packagestability );
		
		// the file exists... the 'fun' begins...
		$p = $this->parse( $c );
		
		var_dump( $p );
	}
	/**
	 * Creates a new packageinfo.xml file from scratch.
	 */
	public function createPackageInfo( $name, $packagename, $packageversion, $packagestability )
	{
		$pi = $this->createPackageInstance( );
	}
	/**
		<pi>
			<p>
				 <n>$package_name$</n>
				 <c>$channel_name$</c>
				 <ca xlink:href="$category_path$">$category_name$</ca>
				 <l>$license$</l>
				 <s>$summary$</s>
				 <d>$description$</d>
				 <r xlink:href="$base_rest$$base_releases$/$package_name$"/>
			</p>
			<a>
				$all_releases$
			</a>
		</pi>
	 */
	public function createPackageInstance( $packageName )
	{
		$tpl = $this->getTemplate( self:tpl_p2 );
		$r   = $this->replaceMagicWords2( $tpl, self::$magic_words );
	}	 
	/**
	 * Inserts $contents in the top level template
	 * for the 'packagesinfo.xml' file
	 */
	public function insertTopPackagesInfo( &$contents )
	{
		$tpl = $this->getTemplate( self::tpl_p );
		if (empty( $tpl ))
			throw new Exception( 'could not access top level "packagesinfo.xml" template' );
		return str_replace( '$all_packages$', $contents, $tpl );
	}
	public function addPackage( &$contents, &$tpl )
	{
		
	}
// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

	/**
	 * Write file.
	 */
	protected function writeFile( $file, &$contents )
	{
		$len = strlen( $contents );
		$bytes_written = @file_put_contents( $file, $contents );
		return ($len === $bytes_written);
	}
	/**
	 * Parses an XML file.
	 */
	protected function parse( &$contents )
	{
		$parser = new PEAR_XMLParser;
		$result = $parser->parse( $contents );
		if (!$result)
			return false;
		return $parser->getData();
	}
		
}
//</source>
/* Example 'packagesinfo.xml' file

array(2) 
{
  
  ["attribs"]=>
  array(4) {
    ["xmlns"]=>
    string(48) "http://pear.php.net/dtd/rest.categorypackageinfo"
    ["xmlns:xsi"]=>
    string(41) "http://www.w3.org/2001/XMLSchema-instance"
    ["xmlns:xlink"]=>
    string(28) "http://www.w3.org/1999/xlink"
    ["xsi:schemaLocation"]=>
    string(105) "http://pear.php.net/dtd/rest.categorypackageinfo     http://pear.php.net/dtd/rest.categorypackageinfo.xsd"
  }
  
  ["pi"]=>
  array(2) {
    ["p"]=>
    array(7) {
      ["n"]=>
      string(9) "Directory"
      ["c"]=>
      string(27) "jldupont.googlecode.com/svn"
      ["ca"]=>
      array(2) {
        ["attribs"]=>
        array(1) {
          ["xlink:href"]=>
          string(18) "/rest/c/Filesystem"
        }
        ["_content"]=>
        string(10) "Filesystem"
      }
      ["l"]=>
      string(0) ""
      ["s"]=>
      string(50) "Helper class for manipulating directory structures"
      ["d"]=>
      string(0) ""
      ["r"]=>
      array(1) {
        ["attribs"]=>
        array(1) {
          ["xlink:href"]=>
          string(17) "/rest/r/directory"
        }
      }
    } //end p
	
    ["a"]=>
    array(1) {
      ["r"]=>
      array(2) {
        [0]=>
        array(2) {
          ["v"]=>
          string(5) "1.0.1"
          ["s"]=>
          string(6) "stable"
        }
        [1]=>
        array(2) {
          ["v"]=>
          string(5) "1.0.0"
          ["s"]=>
          string(6) "stable"
        }
      }
    }// end a
	
  }// end pi

}//end
*/
