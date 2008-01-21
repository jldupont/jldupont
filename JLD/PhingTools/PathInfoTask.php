<?php
/**
 * PHING task which returns the 'pathinfo' of a file resource
 *
 * 	<taskdef classname='JLD.PhingTools.PathInfoTask' name='pathinfo' />
 *	
 * <pathinfo file='desired-file' 
 *			[prop_dirname   ='property-name-for-dirname-info' ]
 *			[prop_basename  ='property-name-for-basename-info' ]
 *			[prop_extension ='property-name-for-extension-info' ]
 *			[prop_filename  ='property-name-for-filename-info'  ] 
 * />
 * All output properties are optional. 
 *
 * @author Jean-Lou Dupont
 * @package PhingTools
 * @version @@package-version@@
 * @Id $Id$
 */
//<source lang=php> 

require_once "JLD/PhingTools/Task.php";

class PathInfoTask extends JLD_PhingTools_Task
{
	const thisTask = 'PathInfo';
	
	public function setFile( $val ) { $this->__set('file', $val); }	
	public function setProp_dirname( $val ) { $this->__set('prop_dirname', $val); }	
	public function setProp_basename( $val ) { $this->__set('prop_basename', $val); }	
	public function setProp_extension( $val ) { $this->__set('prop_extension', $val); }	
	public function setProp_filename( $val ) { $this->__set('prop_filename', $val); }			
	
    /**
     * The main entry point method.
     */
    public function main() 
	{
		if ( $this->file === null )
			throw new BuildException(self::thisTask.': missing file property.');

		$path_parts = @pathinfo( $this->file );
		if (!is_array( $path_parts ))
			throw new BuildException(self::thisTask.': pathinfo error.');		

		if (isset( $this->prop_dirname ))
			$this->project->setProperty($this->prop_dirname, $path_parts['dirname'] );									
		if (isset( $this->prop_basename ))
			$this->project->setProperty($this->prop_basename, $path_parts['basename'] );									
		if (isset( $this->prop_extension ))
			$this->project->setProperty($this->prop_extension, $path_parts['extension'] );									
		if (isset( $this->prop_filename ))
			$this->project->setProperty($this->prop_filename, $path_parts['filename'] );									
    }
}// end class
//</source>