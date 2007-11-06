<?php
/*
	@author: Jean-Lou Dupont
	$Id$
*/
//<source lang=php>
require 'JLD/PearTools/Channel.php';
require 'JLD/PearTools/Categories.php';

$c = JLD_PearTools_Channel::singleton();

// DON'T CHANGE THE DIRECTORY PATH OF THIS FILE OR ELSE THIS WON'T WORK
$root = dirname( dirname( dirname( dirname( __FILE__ ) ) ) );

$c->init( $root );

echo 'Channel name: '.$c->getURI()."\n";

$cs = JLD_PearTools_Categories::singleton();
$cs->init( $c );

$cats = $cs->getAll();

#var_dump( $cats );
try
{
	$cs->addRelease( 'Amazon', 'AmazonS3', '2.0' );
}
catch (PEAR_Exception $e) 
{
	print $e;
}

//</source>