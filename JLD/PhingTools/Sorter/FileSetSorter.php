<?php
/**
 * @author Jean-Lou Dupont
 * @package PhingTools
 * @subpackage SortTask
 * @version @@package-version@@
 * @Id $Id$
 */
//<source lang=php> 
require 'DataTypeSorter.php';

class FileSetSorter extends DataTypeSorter
{
	static $keyMap = array(
		'mtime', 'ctime'
	);
	
	var $ds;
	
	public function __construct(){}
	
	/**
	 * Main method
	 */
	public function sort( &$ref, $key, $dir )
	{
		$this->ref = $ref;
		$this->key = $key;
		$this->dir = $dir;
		
		$this->init();
		
		$sort_method = 'sort_'.$key;
		$this->$sort_method();
		
		$this->finalize();
	}
	/**
	 * Sort by 'modification' time
	 */
	protected function sort_mtime()
	{
		return $this->doList( 'helper_mtime' );
	}
	/**
	 * Sort by 'creation' time
	 */
	protected function sort_ctime()
	{
		return $this->doList( 'helper_ctime' );		
	}
	/**
	 * 
	 */
	protected function doList( $helper )
	{
		
	}
	/**
	 * 
	 */
	protected function helper_mtime()
	{
		
	}
	/**
	 * 
	 */
	protected function helper_ctime()
	{
		
	}
	/**
	 * Verifies if the $key is supported
	 */
	public function checkKey( String $key )
	{
		return in_array( $key, self::$keyMap );		
	}		
	/**
	 * 
	 */
	protected function init()
	{
		$project = $this->getProject();
		$fs = $this->tObj;
		
        $ds = $fs->getDirectoryScanner($project);
        $srcFiles = $ds->getIncludedFiles();
        $srcDirs  = $ds->getIncludedDirectories();
	
		$this->ds = $this->createDirectoryScanner( $srcFiles, $srcDirs );
	}
	protected function finalize()
	{
		$this->tObj->setRefid( $this->ds );		
	}	
	
	protected function sort_fileset_real( &$srcFiles, &$srcDirs )
	{
		$srcFiles = $this->sort_files( $srcFiles );
		$srcDirs = $this->sort_files( $srcDirs );		
	}	
	protected function createDirectoryScanner( &$srcFiles, &$srcDirs )
	{
		return new DirectoryScanner_FS( $srcFiles, $srcDirs );
	}
	
// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

	protected function sort_files( &$files, $key, $dir )
	{
		if (empty( $files ))
			return array();
		$result = array();
		
		// get timestamp for each file
		foreach( $files as $file )
		{
			
		}

		$mtime = @filemtime( $dir.'/'.$file );		
	}	
	/**
	 * 
	 * 
	 */
	protected function & doSort( &$all, $helper )
	{
		$sorted = array();
		
		if (empty( $all ))
			return false;
			
		// starts by re-tagging each entry
		foreach	( $all as &$e )
			$sorted[ $e['v'] ] = $e;
			
		uksort( $sorted, array( __CLASS__, $helper ));
		
		return $sorted;
	}
	/**
	 * Custom sorting function
	 */
	 protected static function doSortHelper( $a, $b )
	 {
	 	return -version_compare( $a, $b );
	 }

} // end class

class DirectoryScanner_FS
{
	var $includedFiles = array();
	var $includedDirs = array();
		
	public function __construct( &$srcFiles, &$srcDirs )
	{
		$this->includedFiles = $srcFiles;
		$this->includedFirs = $srcDirs;
	}
	
    function getIncludedDirectories() 
	{
		return $this->includedDirs;
    }
    function getIncludedFiles() 
	{
		return $this->includedFiles;		
    }
}

//</source>