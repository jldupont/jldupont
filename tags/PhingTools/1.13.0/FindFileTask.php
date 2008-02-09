<?php
/**
 * PHING task 
 * Returns the absolute path to the root of PEAR.
 *
 * 	<taskdef classname='JLD.PhingTools.FindFileTask' name='findfiletask' />
 *	
 *  <findfiletask	dir="directory-where-to-start-the-search"
 *					source="filename-of-file-to-find" 
 * 					target="absolute-path-if-found" />
 *
 * @author Jean-Lou Dupont
 * @package PhingTools
 * @version 1.13.0
 * @Id $Id: FindFileTask.php 330 2008-02-09 18:27:58Z JeanLou.Dupont $
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
		'dir' 	 => array( 'm' => true, 'l' => true, 't' => 'dir' ),	
		'source' => array( 'm' => true, 'l' => true, 't' => 'string' ),
		'target' => array( 'm' => true, 'l' => true, 't' => 'string' ),		
	);
	
	// Attributes interface
	public function setDir( $val )		{ $this->__set('dir', $val); }		
	public function setSource( $val )	{ $this->__set('source', $val); }	
	public function setTarget( $val )	{ $this->__set('target', $val); }	
		
    /**
     * The main entry point method.
     */
    public function main() 
	{
		$parameters = JLD_Validate::initFromObject( $this, self::$params );
		$result = JLD_Validate::doListSanitization( $parameters, self::$params );
		
		if ( !is_array( $result ))
			throw new BuildException( self::thisName.': missing parameter '.$result );
			
		$key = JLD_Validate::doSanitization( $parameters, self::$params );

		if ( $key !== true)
			throw new BuildException( 
				self::thisName.': parameter '.$key.' of wrong type. Expecting "'.self::$params[$key]['t'].'"' );		

		$path = $this->findFile( $this->dir, $this->source );

        $project = $this->getProject();					
		$this->project->setProperty( $this->target, $path);
    }
	/**
	 *
	 */
	protected function findFile( $dir, &$file )
	{
		$result = null;
		do {
			if ( !is_dir( $dir ) )
				break;
				
			$filepath = $dir.'/'.$file;
			if ( is_file( $filepath ))
			{
				$result = $filepath;
				break;
			} 
			// go 1 level up
			$dir = realpath( $dir.'/../' );
		} while(true);
		
		return $result;
	} 

}// end class

//</source>