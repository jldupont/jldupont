<?php
/**
 * System Class includes
 *
 * @author Jean-Lou Dupont
 * @package System
 * @version @@package-version@@
 * @Id $Id$
 */
//<source lang=php>

interface Messaging
{
	/**
	 * Method used to 'sink' a message down an object.
	 */
	public function sinkMessage( $msg, &$params = null );
}

//</source>