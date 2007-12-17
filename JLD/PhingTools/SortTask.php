<?php
/**
 * PHING task which sorts entries of the data-type 'FileSet'
 *
 * 	<taskdef classname='JLD.PhingTools.SortTask' name='sort' />
 *	
 *  <sort sid='reference-to-source-object' key='' dir ='' tid='result-object-reference-id' />
 *
 * dir := [0 => up; 1 => down ]
 * FileSet := key = [ mtime, ctime ];
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
	
	var	$sObj = null;
	
	public function setSid( $val ) { $this->__set('sid', $val); }	
	public function setKey( $val ) { $this->__set('key', $val); }
	public function setDir( $val ) { $this->__set('dir', $val); }
	public function setTid( $val ) { $this->__set('tid', $val); }	
	
    /**
     * The main entry point method.
     */
    public function main() 
	{
		$this->validateParameters();
		$this->sort( $this->tObj, $this->__get('key' ), $this->__get( 'dir' ) );
    }
	/**
	 *
	 */
	protected function validateParameters()
	{
		if ( $this->tid === null )
			throw new BuildException( self::thisName.': missing target object id.');

		if ( $this->sid === null )
			throw new BuildException( self::thisName.': missing source object id.');

		$refs = $this->project->getReferences();
		if (isset( $refs[ $this->sid ] ))
			$this->sObj = $refs[ $this->sid ];

		if ( !is_object( $this->sObj ))
			throw new BuildException(self::thisName.': sourceobject id given does not point to a valid object.');

		if ( !$this->sObj instanceof FileSet )
			throw new BuildException(self::thisName.': object id given does not point a supported object.');		

		$this->classe = get_class( $this->sObj );
		if ( !$this->checkSorter( $this->classe ) )
			throw new BuildException(self::thisName.': unsupported object class.');		

		$key = $this->key;
		if ( empty( $key ) )
			throw new BuildException(self::thisName.': requires a valid "key" attribute.');

		$dir = $this->dir;
		if ( empty( $dir ) )
			throw new BuildException(self::thisName.': requires a valid "dir" attribute.');
			
		$this->sorter = $this->createSorter( $this->classe );
		if (!is_object( $this->sorter ))
			throw new BuildException(self::thisName.': error creating sorter object.');	
				
		if ( !$this->sorter->checkKey( $key ) )
			throw new BuildException(self::thisName.': unsupported sort key.');		
	} 
	/**
	 * 
	 */
	protected function checkSorter( $classe )
	{
		require 'Sorter/'.$classe.'Sorter.php';
		return class_exists( $classe.'Sorter' );
	}
	/**
	 * 
	 */
	protected function & createSorter( $classe )
	{
		$name = $classe.'Sorter';
		return new $name( $this->project, $this->sObj, $this->tid );
	}	
	/**
	 * 
	 */
	protected function sort( &$obj, $key, $dir )
	{
		return $this->sorter->sort( $obj, $key, $dir);
	}	
}// end class

//</source>