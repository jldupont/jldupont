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
	var $srcFiles = array();
	var $srcDirs = array();
	
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
		
		$this->doSort();
		
		$this->finalize();
	}
	/**
	 * Sort by 'modification' time
	 */
	protected function helper_mtime( &$file )
	{
		return @filemtime( $file );
	}
	/**
	 * Sort by 'creation' time
	 */
	protected function helper_ctime( &$file )
	{
		return @filectime( $file );
	}
	/**
	 * 
	 */
	protected function doSort( )
	{
		$helper = 'helper_'.$this->key;
		$fliste = array();
		$dliste = array();
		
		// first, sort the files
		if (!empty( $this->srcFiles ))		
		{
			foreach( $this->srcFiles as $file )
			{
				$tag = $this->$helper( $file );
				$fliste[] = array( 'n' => $file, 't' => $tag );
			}
			$this->srcFiles = $this->doRealSort( $fliste);
		}
		// next, sort the directories
		if (!empty( $this->srcDirs ))
		{
			foreach( $this->srcDirs as $dir )
			{
				$tag = $this->$helper( $file );
				$dliste[] = array( 'n' => $file, 't' => $tag );
			}
			$this->srcDirs = $this->doRealSort( $dliste);			
		}
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
        $this->srcFiles = $ds->getIncludedFiles();
        $this->srcDirs  = $ds->getIncludedDirectories();
	}
	protected function finalize()
	{
		$this->ds = $this->createDirectoryScanner( $srcFiles, $srcDirs );		
		$this->tObj->setRefid( $this->ds );		
	}	
	protected function createDirectoryScanner( &$srcFiles, &$srcDirs )
	{
		return new DirectoryScanner_FS( $srcFiles, $srcDirs );
	}
	
// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

	/**
	 * 
	 * 
	 */
	protected function & doRealSort( &$files )
	{
		if (empty( $files ))
			return array();
			
		uksort( $files, array( __CLASS__, 'SortHelper' ));
		
		return $files;
	}
	/**
	 * Custom sorting function
	 */
	 protected static function SortHelper( $a, $b )
	 {
	 	switch( $this->dir )
		{
			
		}
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