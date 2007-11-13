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
	const tpl_p = '/Templates/packagesinfo.xml.tpl';
	
	// relative to the REST structure; this is standard.
	static $baseCategories = '/c';
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
		if (!is_object( $this->channel ))
			throw new Exception('invalid channel object');
		
		$this->channel = $channel;
		
		// we'll be needing these parameters in the templating process...
		$this->setVar('channel_name',	$this->channel->getName());
		$this->setVar('base_rest', 		$this->channel->getRESTPath());
		$this->setVar('base_categories',self::$baseCategories );		
		
		$this->rootPath = $this->channel->getRootPath();
		$this->baseREST = $this->channel->getRESTPath();
		$this->restPathC = $this->rootPath . $this->baseREST . self::$baseCategories;
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
		$result = @mkdir( $this->restPathC.'/'.$name );	
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
		$file = $this->$this->restPathC.'/categories.xml';
		$result = $this->writeFile( $file, $final_result );
		
		return $result;
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
