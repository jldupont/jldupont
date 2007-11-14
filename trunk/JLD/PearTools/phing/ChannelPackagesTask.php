<?php
/**
 * @author Jean-Lou Dupont
 * @package JLD
 * @version $Id$
 *
 * PHING task
 *
 * <taskdef classname='JLD.PearTools.phing.ChannelPackagesTask' name='packages' />
 * <packages channelroot= "${channel.root}" 
 *             catname="${package.categoryname}" 
 *             packagename="${package.name}" />
 */
//<source lang=php> 

require_once "JLD/PhingTools/Task.php";
require_once "JLD/PearTools/Channel.php";
require_once "JLD/PearTools/ChannelPackages.php";

class ChannelPackagesTask extends JLD_PhingTools_Task
{
	// Attributes interface
	// Name of category to add + package name
	public function setChannelRoot( $val ) { $this->__set('channelroot', $val); }
	public function setCatName( $val ) { $this->__set('catname', $val ); }	
	public function setPackageName( $val ) { $this->__set('packagename', $val ); }		
	
    /**
     * The init method: Do init steps.
     */
    public function init() {}

    /**
     * The main entry point method.
     */
    public function main() 
	{
		$c = JLD_PearTools_Channel::singleton();
		$result = $c->init( $this->__get('channelroot') );
		if (!$result)
			throw new BuildException( 'channel object could not be created because channel.xml was not found' );
		
		$cp = JLD_PearTools_ChannelPackages::singleton();
		try
		{
			$cp->init( $c );
		}
		catch(Exception $e)
		{
			throw new BuildException( $e->getMessage() );
		}
		// 1- add category directory in REST structure
		//    if the directory already exists, don't alarm.
		$result = $cp->addPackageDirectory( $this->__get('packagename') );
		if (!$result)
			throw new BuildException( 'could not create the package directory in the REST structure' );

		// 2- add the package's 'info.xml' file
		$result = $cp->createPackageInfoFile( $this->__get('packagename'), $this->__get('catname'));
		if (!$result)
			throw new BuildException( 'could not create the file "info.xml" for the package in the REST structure' );
		
    }

}
//</source>