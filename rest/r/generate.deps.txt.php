<?php
/*
	Generates the 'deps.$version.txt' file from
	a valid 'package.$version.xml' file.

	@author: Jean-Lou Dupont
	
	Aptana:  "${project_loc}/rest/r/generate.deps.txt.php"  "${resource_loc}"
	
	- Execute the above Aptana/Eclipse 'external tools' command using PHP.
	- Select target resource e.g. package.0.1.0.xml
*/

@require "PEAR/XMLParser.php";
if (!class_exists('PEAR_XMLParser'))
{
	echo 'This tools requires PEAR/XMLParser library.'."\n";
	die(0);
}

// grab the source file from the command line
$source_file_name = basename( $argv[1],".xml" );

$cdir = dirname( $argv[1] );

echo 'Source directory: '.$cdir."\n";
echo 'Source file name: '.$source_file_name."\n";

// extract version #
$first_dot = strpos( $source_file_name, '.' );

$version = substr(	$source_file_name, 
					$first_dot );
				
// the target file name is of the form
$target_file_name = 'deps'."{$version}".".txt";

echo 'Target file name: '.$target_file_name."\n";

// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
$file_contents = @file_get_contents( $cdir.'/'.$source_file_name.".xml" );
if (empty( $file_contents ))
{
	echo 'File Empty or invalid file name!'."\n";
	die(0);
}

// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
$parser = new PEAR_XMLParser;
$result = $parser->parse( $file_contents );

echo 'Parsing: '.($result ? 'OK':'Fail')."\n";
if (!$result)
	die(0);
	
#var_dump( $parser->getData() ); // debug

// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

$data = $parser->getData();
$deps = $data['dependencies'];
$s_deps = serialize( $deps );
echo 'Serialized dependencies: '.$s_deps."\n";

$bytes_written = file_put_contents( $cdir."/".$target_file_name, $s_deps );

// Make sure that the number of bytes written matches!
$ok = (strlen( $s_deps ) === $bytes_written );

$msg = $ok ? 'Success!':'Failure to write to target file!';

echo $msg;