<?php
/**
 *  WB_S3 package unit tests
 *
 *  @author Jean-Lou Dupont
 *  @version @@package-version@@
 */

require_once 'PHPUnit/Framework.php';
require_once dirname(__FILE__)."/../DeliciousPosts.php";
require_once dirname(__FILE__)."/../DeliciousPost.php";

class UnitTest extends PHPUnit_Framework_TestCase
{
	static $feed = "jldupont/my-diagrams";
	
	/*
	 * GENERIC setup and teardown
	 */		
    protected function setUp()
    {
    }
 	protected function tearDown()
	{
	}
	public function test1()
	{
		$o = new JLD_DeliciousPosts( self::$feed );
		$r = $o->run();
		
		$x = $o->getXml();
		
		var_dump( $x );
		
		$this->assertEquals( $r , true );				
	}

}// end UnitTest class