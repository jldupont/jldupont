<?php
/**
 * @author Jean-Lou Dupont 
 */
echo "IP address updater - Jean-Lou Dupont\n";

if (!isset( $argv[1] ))
{
	echo "Requires a username as parameter 1";	
	die(0);
}

$username = $argv[1];

if (!isset( $argv[2] ))
{
	echo "Requires a password as parameter 2";	
	die(0);
}

$password = $argv[2];

// =============================================

require "HTTP/Request.php";

$username = str_replace("\"", '', $username );
$password = str_replace("\"", '', $password );

$authorization = base64_encode( $username.":".$password );

// FIRST, get the ip address from our "echo" service
$request =& new HTTP_Request( "http://www.jldupont.com/services/echo/jldupont/" );

$request->setMethod( 'GET' );



// SECOND, send the update
$request =& new HTTP_Request( "http://members.dyndns.org/nic/update?hostname=yourhostname&myip=ipaddress&wildcard=NOCHG&mx=NOCHG&backmx=NOCHG" );

$request->setMethod( 'GET' );
$request->addHeader( 'Authorization', 'Basic '.$authorization );
$request->addHeader( 'User-Agent', 'jldupont.com' );

$code = null;
try
{
	$code = $request->sendRequest();			
}
catch(Exception $e)
{
	$code = false;
}

if ( PEAR::isError( $code ) )
	return false;
