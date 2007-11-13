<?php
/**
 * @author Jean-Lou Dupont
 * @package JLD
 * @version $Id$
 */
//<source lang=php> 
class JLD_PhingTools_Path
{
	/**
	 * Resolves a path where there can be /../ links
	 * in the path construction. Only works when the /../ link
	 * is present at the END of the path.
	 */
	public static function resolve( $path )
	{
		$f = strpos($path, '/../' );
		if ($f === false)
			return $path;
			
		// ugly I know...
		$p = substr( $path, 0, strlen( $path) - strlen('/../') );
		return dirname( $p );
	}
}
//</source>