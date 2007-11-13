<?php
/**
 * @author Jean-Lou Dupont
 * @package JLD
 * @version $Id$
 */
//<source lang=php> 

require_once "JLD/PhingTools/Task.php";
require_once "JLD/PearTools/Package.php";

class PackageReadTask extends JLD_PhingTools_Task
{
	// Attributes interface
	// Property names that will contain the desired properties read from the package file.
	public function setPropertyPackageName( $val ) { $this->__set('propertyPackageName', $val ); }
	public function setPropertyPackageVersion( $val ) { $this->__set('propertyPackageVersion', $val ); }	
	public function setPropertyPackageFile( $val ) { $this->__set('propertyPackageFile', $val ); }	
		
    /**
     * The init method: Do init steps.
     */
    public function init() {}

    /**
     * The main entry point method.
	 * This method creates the 'channel.xml' file based on the
	 * given parameters.
     */
    public function main() 
	{
		$contents = null;
		$p = new JLD_PearTools_Package( $contents, $this->propertyPackageFile );
		if (!$p->isValid())
			throw new BuildException( 'package file appears invalid' );

		$this->project->setProperty($this->propertyPackageName, $p->getName() );		
		$this->project->setProperty($this->propertyPackageVersion, $p->getVersion() );				
    }
}
