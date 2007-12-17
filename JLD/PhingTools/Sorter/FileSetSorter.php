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
	
	var $sObj = null;
	var $tObj = null;
	var $tId = null;
	var $ds;
	var $srcFiles = array();
	var $srcDirs = array();
	var $project;
	
	public function __construct( &$prj, &$obj, $tid )
	{
		$this->project = $prj;
		$this->sObj = $obj;
		$this->tId = $tid;
	}
	
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
			$this->doRealSort( $fliste);
		}
		// next, sort the directories
		if (!empty( $this->srcDirs ))
		{
			foreach( $this->srcDirs as $dir )
			{
				$tag = $this->$helper( $file );
				$dliste[] = array( 'n' => $file, 't' => $tag );
			}
			$this->doRealSort( $dliste);			
		}
		
		$this->srcFiles = array();
		foreach( $fliste as $key => &$na )
			$this->srcFiles[] = $key;

		$this->srcDirs = array();
		foreach( $dliste as $key => &$na )
			$this->srcDirs[] = $key;

	}
	/**
	 * Verifies if the $key is supported
	 */
	public function checkKey( $key )
	{
		return in_array( $key, self::$keyMap );		
	}		
	/**
	 * 
	 */
	protected function init()
	{
		$fs = $this->sObj;
		
        $ds = $fs->getDirectoryScanner( $this->project );
        $this->srcFiles = $ds->getIncludedFiles();
        $this->srcDirs  = $ds->getIncludedDirectories();
	}
	protected function finalize()
	{
		$this->ds = $this->createDirectoryScanner( $srcFiles, $srcDirs );		
		
		$this->tObj = clone $this->sObj;
		$this->tObj->setRefid( $this->ds );		
		
		$this->project->addReference( $this->tid, $this->tObj );
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
		
		if ($this->dir)
			uksort( $files, array( __CLASS__, 'sortHelperUp' ));
		else
			uksort( $files, array( __CLASS__, 'sortHelperDown' ));		
	}
	/**
	 * Custom sorting function
	 */
	 protected static function sortHelperUp( $a, $b )
	 {
	 	return $a['t'] > $b['t'];
	 }
	/**
	 * Custom sorting function
	 */
	 protected static function sortHelperDown( $a, $b )
	 {
	 	return $a['t'] < $b['t'];
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