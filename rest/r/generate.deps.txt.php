<?php
/*
	Generates the 'deps.$version.txt' file from
	a valid 'package.$version.xml' file.

	@author: Jean-Lou Dupont
	
	Aptana:  "${project_loc}/rest/r/generate.deps.txt.php"  "${resource_loc}"
*/

@require "PEAR/XMLParser.php";
if (!class_exists('PEAR_XMLParser'))
{
	echo 'This tools requires PEAR/XMLParser library.'."\n";
	die(0);
}

// grab the source file from the command line
$source_file_name = basename( $argv[1],".xml" );

echo 'Source file name: '.$source_file_name."\n";

// extract version #
$first_dot = strpos( $source_file_name, '.' );

$version = substr(	$source_file_name, 
					$first_dot );
				

// the target file name is of the form
$target_file_name = 'deps'."{$version}".".txt";

echo 'Target file name: '.$target_file_name."\n";
