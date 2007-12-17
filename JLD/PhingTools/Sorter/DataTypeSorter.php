<?php
/**
 * PHING task which sorts entries of the data-type 'FileSet'
 *
 * 	<taskdef classname='JLD.PhingTools.SortTask' name='sort' />
 *	
 *  <sort tid='reference-to-object' key='' dir ='' />
 *
 * FileSet => key = [ mtime, ctime ];
 *
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