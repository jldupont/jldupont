<?php
/**
 *  JLD_MindMeister package unit tests
 *
 *  @author Jean-Lou Dupont
 *  @version @@package-version@@
 */

require_once 'PHPUnit/Framework.php';
require_once dirname(__FILE__)."/../MindMeister.php";

class UnitTest extends PHPUnit_Framework_TestCase
{
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
		$this->assertEquals( $g instanceof JLD_Gliffy, true );
	}

	
}// end UnitTest class