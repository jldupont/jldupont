<?php
/**
 * PHING task 
 * Returns the absolute path to the root of PEAR.
 *
 * 	<taskdef classname='JLD.PhingTools.FindFileTask' name='findfiletask' />
 *	
 *  <findfiletask	source="filename-of-file-to-find" 
 * 					target="absolute-path-if-found" />
 *
 * @author Jean-Lou Dupont
 * @package PhingTools
 * @version @@package-version@@
 * @Id $Id$
 */
//<source lang=php> 

require_once "JLD/PhingTools/Task.php";
require_once "JLD/Validate/Validate.php";

class FindFileTask extends JLD_PhingTools_Task
{
	const thisName = 'FindFileTask';

/**
 * m: mandatory parameter
 * s: sanitization required
 * l: which parameters to pick from list
 * d: default value

EXAMPLE of a reference list:
============================
	static $parameters = array(
		'email_p1'	=> array( 'm' => true,  's' => true, 'l' => false, 'd' => null,   'sq' => true, 'dq' => true  ),
		'email_p2'	=> array( 'm' => true,  's' => true, 'l' => false, 'd' => null,   'sq' => true, 'dq' => true  ),
		'size'		=> array( 'm' => false, 's' => true, 'l' => false, 'd' => '40',   'sq' => true, 'dq' => true  ),
		'default'	=> array( 'm' => false, 's' => true, 'l' => false, 'd' => null,   'sq' => true, 'dq' => true  ),
		'width'		=> array( 'm' => false, 's' => true, 'l' => true,  'd' => null,   'sq' => true, 'dq' => true  ),
		'height'	=> array( 'm' => false, 's' => true, 'l' => true,  'd' => null,   'sq' => true, 'dq' => true  ),		
		'alt'		=> array( 'm' => false, 's' => true, 'l' => true,  'd' => null,   'sq' => true, 'dq' => true  ),		
		'title'		=> array( 'm' => false, 's' => true, 'l' => true,  'd' => null,   'sq' => true, 'dq' => true  ),		
	);
*/
	
	static $params = array(
		'source' => array( 'm' => true, 'l' => true, 't' => 'string' ),
		'target' => array( 'm' => true, 'l' => true, 't' => 'string' ),		
	);
	
	// Attributes interface
	public function setSource( $val ) { $this->__set('source', $val); }	
	public function setTarget( $val ) { $this->__set('target', $val); }	
		
    /**
     * The main entry point method.
     */
    public function main() 
	{
		if ( is_null( $this->source ))
			throw new BuildException( self::thisName.': source filename name must be specified.');

		$path = $this->findFile( $this->source );

        $project = $this->getProject();					
		$this->project->setProperty( $this->target, $path);
    }
	/**
	 *
	 */
	protected function findPearPath()
	{
		$pathArray = explode( PATH_SEPARATOR, get_include_path() );
		
		if ( empty( $pathArray ))
			return null;
			
		foreach( $pathArray as &$e )
			if ( preg_match( '/pear/si', $e ) === 1 )
				return $e;
									
		return null;			
	} 

}// end class

//</source>