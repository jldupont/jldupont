<?php
/*
	Copies the source directory to the local PEAR directory.
	
	@author: Jean-Lou Dupont
	
	Aptana:  "${project_loc}/$DIR/copyToLocalPear.php"  "${resource_loc}"
	
	- Execute the above Aptana/Eclipse 'external tools' command using PHP.
	- Select target resource
*/

// PEAR dependancy
require 'JLD/Directory.php';

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
$pdir = dirname( $sdir );

echo 'Source directory: '.$sdir."\n";
echo 'Parent directory: '.$pdir."\n";

// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
$file_contents = @file_get_contents( $cdir.'/'.$source_file_name.".xml" );
if (empty( $file_contents ))
{
	echo 'File Empty or invalid file name!'."\n";
	die(0);
}

// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
$p_date = '/\<'.'date\>'.'.*'.'\<\/date\>'.'/siU';
$p_time = '/\<'.'time\>'.'.*'.'\<\/time\>'.'/siU';

$date = '<'.'date'.'>'.gmdate("Y-m-d").'</date'.'>';
$time = '<'.'time'.'>'.gmdate("H:i:s").'</time'.'>';

$file_contents = preg_replace( $p_date, $date, $file_contents );
$file_contents = preg_replace( $p_time, $time, $file_contents );

// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

echo "Current date: ".$date."\n";
echo "Current time: ".$time."\n";

$bytes_written = file_put_contents( $cdir.'/'.$source_file_name.".xml", $file_contents );

// Make sure that the number of bytes written matches!
$ok = (strlen( $file_contents ) === $bytes_written );

echo "Update of ".$source_file_name." ";
$msg = $ok ? 'Success!':'Failure to write to target file!';

echo $msg;

// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// Part2: generate deps.$version.txt file

@require "PEAR/XMLParser.php";
if (!class_exists('PEAR_XMLParser'))
{
	echo 'This tools requires PEAR/XMLParser library.'."\n";
	die(0);
}

// extract version #
$first_dot = strpos( $source_file_name, '.' );

$version = substr(	$source_file_name, 
					$first_dot );
				
// the target file name is of the form
$target_file_name = 'deps'."{$version}".".txt";

echo 'Target file name: '.$target_file_name."\n";

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