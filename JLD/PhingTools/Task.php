<?php
/**
 * @author Jean-Lou Dupont
 * @package JLD
 * @version $Id$
 */
//<source lang=php> 
require_once "phing/Task.php";

abstract class JLD_PhingTools_Task extends Task
{
	var $vars;
	
	public function __set( $nm, $val )
	{
		return $this->vars[ $nm ] = $val;
	}
	public function __get( $nm )
	{
		return @$this->vars[ $nm ];
	}
	/**
	 * This interface does not seem to work with the current
	 * version of phing...
	 */
	public function __call( $method, $args )
	{
		$action = substr( $method, 0, 3);
		$var = substr( $method, 3 );
		
		if ($action === 'set')
			return $this->__set( $var, $args[0] );

		if ($action === 'get')
			return $this->__get( $var );
	
		throw new Exception( __CLASS__.': unknown method' );
	}
}
//</source>