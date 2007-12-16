<?php
/**
 * PHING task which sorts entries of the data-type 'FileSet'
 *
 * 	<taskdef classname='JLD.PhingTools.SortTask' name='sort' />
 *	
 *  <sort tid='reference-to-object' key='' dir ='' />
 * 
 * @author Jean-Lou Dupont
 * @package PhingTools
 * @version @@package-version@@
 * @Id $Id$
 */
//<source lang=php> 

require_once "JLD/PhingTools/Task.php";

class SortTask extends JLD_PhingTools_Task
{
	const thisName = 'SortTask';
	
	var	$tObj = null;
	
	public function setTId( $val ) { $this->__set('tid', $val); }	
	public function setKey( $val ) { $this->__set('key', $val); }
	public function setDir( $val ) { $this->__set('dir', $val); }	
	
    /**
     * The main entry point method.
     */
    public function main() 
	{
		$this->validateParameters();
		$this->sort();
    }
	/**
	 *
	 */
	protected function validateParameters()
	{
		if ( $this->tsid === null )
			throw new BuildException( self::thisName.': missing target object id.');

		$refs = $this->project->getReferences();
		if (isset( $refs[ $this->tid ] ))
			$this->tObj = $refs[ $this->tid ];

		if ( !is_object( $this->tObj ))
			throw new BuildException(self::thisName.': object id given does not point to a valid object.');

		if ( !$this->tObj instanceof FileSet )
			throw new BuildException(self::thisName.': object id given does not point a supported object.');		

		$this->classe = get_class( $this->tObj );
		if ( !method_exists( $this, "sort_$classe" ) )
			throw new BuildException(self::thisName.': unsupported object class.');		
			
		if ( empty( $this->__get( 'key' ) ) )
			throw new BuildException(self::thisName.': requires a valid "key" attribute.');

		if ( empty( $this->__get( 'dir' ) ) )
			throw new BuildException(self::thisName.': requires a valid "dir" attribute.');
	} 
	
	/**
	 * 
	 */
	protected function sort()
	{
		$method = "sort_".$this->classe;
		return $this->$method();
	}	
	/**
	 * 
	 */
	protected function sort_fileset()
	{
		$project = $this->getProject();
		$fs = $this->tObj;
		
        $ds = $fs->getDirectoryScanner($project);
        $srcFiles = $ds->getIncludedFiles();
        $srcDirs  = $ds->getIncludedDirectories();
	
		$this->sort_fileset_real( $srcFiles, $srcDirs );
		
		$ds = $this->createDirectoryScanner( $srcFiles, $srcDirs );
		
		$this->tObj->setRefid( $ds );
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
}// end class

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