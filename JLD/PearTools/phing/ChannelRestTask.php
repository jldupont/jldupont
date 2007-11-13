<?php
/**
 * @author Jean-Lou Dupont
 * @package JLD
 * @version $Id$
 */
//<source lang=php> 

require_once "JLD/PhingTools/Task.php";
require_once "JLD/PearTools/Channel.php";

class ChannelRestTask extends JLD_PhingTools_Task
{
	public function setPath( $val ) { $this->__set('path', $val ); }	
		
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
		$c = JLD_PearTools_Channel::singleton();

		$result = $c->createRest();		
		if (!$result)
			throw new BuildException( 'error creating REST directories' );
    }
}
