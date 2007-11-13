<?php
/**
 * @author Jean-Lou Dupont
 * @package JLD
 * @version $Id$
 */
//<source lang=php> 

require_once "JLD/PhingTools/Task.php";
require_once "JLD/PhingTools/Path.php";
require_once "JLD/PearTools/Channel.php";

class ChannelTask extends JLD_PhingTools_Task
{
	// Attributes interface
	public function setName( $val ) { $this->__set('name', $val ); }
	public function setAlias( $val ) { $this->__set('alias', $val ); }
	public function setUri( $val ) { $this->__set('uri', $val ); }	
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
		$p = JLD_PhingTools_Path::resolve( $this->path );

		$c->name = $this->name;
		$c->alias = $this->alias;
		$c->uri = $this->uri;
		$c->file = $p.'/channel.xml';
		
		$result = $c->create();
		if (!$result)
			throw new BuildException( 'error building channel.xml file' );
		
		$result = $c->write();		
		if (!$result)
			throw new BuildException( 'error writing channel.xml file' );
    }
}
