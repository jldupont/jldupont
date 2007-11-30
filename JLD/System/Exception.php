<?php
/**
 * Base exception class
 *
 * @author Jean-Lou Dupont
 * @package System
 * @version @@package-version@@
 * @Id $Id$
 */
//<source lang=php>
require 'JLD/System/ExceptionList.php';

class JLD_System_Exception extends Exception
{
	/**
	 * Each 'listener' object must implement the 'exception_listener' interface
	 *
	 * @var mixed An array containing the registered 'listeners'
	 */
	static $listeners = array();
	
	/**
	 * Each listener will be called in turn when an exception turns up.
	 * @param mixed Object reference
	 */
	public static function registerListener( &$l )
	{
		self::$listeners[] = $l;
	}
	
}//end class
//</source>