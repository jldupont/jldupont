<?php
/**
 *  JLD_MindMeister package unit tests
 *
 *  @author Jean-Lou Dupont
 *  @version @@package-version@@
 */

require_once 'PHPUnit/Framework.php';
require_once dirname(__FILE__)."/../MindMeister.php";
require_once dirname(__FILE__).'/config.php';

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
	public function testGetList()
	{
		$r = JLD_MindMeister::callMethod( 'getList', array() );
		
		var_dump( $r->body );
		
		$this->assertEquals( $r, true );
	}

	
}// end UnitTest class