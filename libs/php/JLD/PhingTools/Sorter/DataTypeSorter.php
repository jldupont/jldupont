<?php
/**
 * @author Jean-Lou Dupont
 * @package PhingTools
 * @version @@package-version@@
 * @Id $Id$
 */
//<source lang=php> 
abstract class DataTypeSorter
{
	var $ref = null;
	var $key = null;
	var $dir = null;
	
	abstract public function checkKey( $key );
	
	abstract public function sort( &$obj, $key, $dir );
}
//</source>