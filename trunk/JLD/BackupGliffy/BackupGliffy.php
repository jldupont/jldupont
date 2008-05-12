<?php
/**
 *  JLD_BackupGliffy
 *
 *  @author Jean-Lou Dupont
 *  @version @@package-version@@
 */

require_once 'JLD/Delicious/DeliciousPosts.php';
require_once 'JLD/Gliffy/Gliffy.php';
require_once 'JLD/BackupGliffy/BackupGliffy.php';

// configuration
require_once "JLD/BackupGliffy/config.php";

// gets posts
$posts = new JLD_DeliciousPosts( $feed );
$posts->run();

// main loop
foreach( $posts as $post ) {

	$g = JLD_Gliffy::newFromDeliciousPost( $post );
	assert( $g instanceof JLD_Gliffy );

	$i = $g->getPictureIterator();
	$title = $g->title;
	
	foreach( $i as $index => $repr ) {

		assert( is_string( $repr ) );
		echo "\n* Represention of $title: $index: $repr";	

		$contents = file_get_contents( $repr );
		if ( $contents === false )
			echo ": error fetching";
		else {
			echo ": fetching OK";
			#file_put_contents( $dest . $title . );
		}
	}
	
	
}
