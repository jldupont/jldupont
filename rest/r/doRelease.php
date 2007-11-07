<?php
/*
	Releases a PEAR package.
	
	@author: Jean-Lou Dupont
	
	Aptana:  "${project_loc}/$DIR/doRelease.php"  "${resource_loc}"
	
	- Execute the above Aptana/Eclipse 'external tools' command using PHP.
	- Select target resource
	
	IMPORTANT:
	- This file assumes to be located in {project_dir}/rest/r
	  the channel file must be located in {project_dir}
*/

// PEAR dependancy
require 'JLD/Directory/Directory.php';
require 'JLD/PearTools/Channel.php';
require 'JLD/PearTools/Categories.php';

if (!isset( $argv[1]))
{
	echo "Requires a directory path as input!\n";	
	die(0);
}

$sdir = $argv[1];

if (!is_dir( $sdir ))
{
	echo "Requires a valid directory path as input!\n";	
	die(0);
}

// we need the parent directory path too in order to properly
// place the source files in the local PEAR directory.
$pname = basename( $sdir );

echo 'Source directory: '.$sdir."\n";
echo 'Assuming Package Name: '.$pname."\n";

$thisDir = dirname( __FILE__ );
// we need to go up...
$prjRoot = dirname( dirname( $thisDir ) );

 // init channel object.
$c = JLD_PearTools_Channel::singleton();
$c->init( $prjRoot );
echo 'Channel name: '.$c->getURI()."\n";

$cs = JLD_PearTools_Categories::singleton();
$cs->init( $c );

$cname = $cs->findCategoryNameForPackageName( $pname, $msg );
if ($cname === false)
{
	echo '* Error: category name not found!'."\n";
	die (0);
}
echo 'Category name: '.$cname."\n";
