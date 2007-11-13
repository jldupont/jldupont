<?php
/**
 * @author Jean-Lou Dupont
 * @package JLD
 * @version $Id$
 *
 * PHING task
 *
 * <taskdef classname='JLD.PearTools.phing.CategoriesTask' name='categories' />
 * <categories catname="${package.categoryname}" packagename="${package.name}" />
 */
//<source lang=php> 

require_once "JLD/PhingTools/Task.php";
require_once "JLD/PearTools/Channel.php";
require_once "JLD/PearTools/ChannelCategories.php";

class CategoriesTask extends JLD_PhingTools_Task
{
	// Attributes interface
	// Name of category to add + package name
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
		$result = $c->init( $this->path );
		if (!$result)
			throw new BuildException( 'channel object could not be created because channel.xml was not found' );
		
		$cs = new JLD_PearTools_ChannelCategories;
		try
		{
			$cs->init( $c );
		}
		catch(Exception $e)
		{
			throw new BuildException( $e->getMessage() );
		}
		// 0- read all the categories in
		$cs->readAll();
		
		// 1- add category directory in REST structure
		//    if the directory already exists, don't alarm.
		$result = $cs->addCategoryDirectory( $this->__get('catname') );
		if (!$result)
			throw new BuildException( 'could not create the category directory in the REST structure' );
		// 2- add the category to the 'categories.xml' file
		try
		{
			$result = $cs->updateCategories();
		}
		catch (Exception $e)
		{
			throw new BuildException( $e->getMessage() );
		}
    }
}
//</source>