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
require 'JLD/PearTools/Releases.php';
require 'JLD/PearTools/Package.php';

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

// CATEGORIES

$cs = JLD_PearTools_Categories::singleton();
$cs->init( $c );

$cname = $cs->findCategoryNameForPackageName( $pname, $msg );
if ($cname === false)
{
	echo '* Error: category name not found: '.$msg."\n";
	die (0);
}
echo 'Category name: '.$cname."\n";

// package.xml file must be in the source directory.
$package_file = $sdir.'/package.xml';
$package_file_contents = @file_get_contents( $package_file );
if (empty( $package_file_contents ))
{
	echo '* Error: reading "package.xml" file from source directory!'."\n";
	die(0);
}
$package = new JLD_PearTools_Package( $package_file_contents, $package_file );
$version = $package->getVersion();

#var_dump( $package->getData() );

echo 'Assuming release version: '.$version."\n\n";

// $version.xml FILE
$r = JLD_PearTools_Releases::singleton();
$r->init( $c );

echo 'Creating '."$version.xml file ... ";
$result = $r->createVersionFile( $pname, $version, 'stable', &$msg );
if ($result === false)
{
	echo '* Error: '.$msg."\n";	
	die(0);
}
echo 'success!'."\n";

// deps.$version.txt FILE
$deps = $package->getSerializedDependencies();

echo 'Creating '."deps.$version.txt file ... ";
$result = $r->generateDepsFile( $pname, $version, $deps, $msg );
if ($result === false)
{
	echo '* Error: '.$msg."\n";	
	die(0);
}
echo 'success!'."\n";

// Updating source package.xml
echo "Updating 'package.xml' file ... ";
$result = $package->updateFile();
if ($result === false)
{
	echo '* Error: '.$msg."\n";	
	die(0);
}
echo 'success!'."\n";

// Copying package.xml FILE to /r/$pname directory --> $file = package.$version.xml
$btarget = "package.$version.xml";
$target = $r->genFilePath( $pname ) . '/' . $btarget;
echo "Copying 'package.xml' file to $btarget ... ";
$result = @copy( $package_file, $target );
if ($result === false)
{
	echo '* Error: '.$msg."\n";	
	die(0);
}
echo 'success!'."\n";

// UPDATING packagesinfo.xml in /c
echo 'Updating "packagesinfo.xml" of category: '.$cname.' ... ';
$pif = $cs->getPackageInfoObject( $cname );
if (!is_object( $pif ))
{
	echo "* Error: accessing 'packagesinfo.xml' \n";	
	die(0);
}
$pif->addRelease( $pname, $version );
$result = $cs->updatePackageInfoFile( $pif );
if (!$result)
{
	echo "* Error: updating 'packagesinfo.xml' \n";	
	die(0);
}
echo 'success!'."\n";

// UPDATE 'allreleases.xml' FILE
echo 'Updating "allreleases.xml" ... ';
$r->updateAllReleasesFile( $pname, $version, 'stable', &$msg );
if ($result === false)
{
	echo '* Error: '.$msg."\n";	
	die(0);
}
echo 'success!'."\n";
