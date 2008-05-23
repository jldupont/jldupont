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
	var $mm;
	
	/*
	 * GENERIC setup and teardown
	 */		
    protected function setUp()
    {
    	global $api_key, $secret_key;
    	$this->mm = new JLD_MindMeister( $api_key, $secret_key );
    }
 	protected function tearDown()
	{
	}
	public function testGetList()
	{
		$r = $this->mm->getList( );
		
		var_dump( $r->body );
		
		$this->assertEquals( $r, true );
	}

	
}// end UnitTest class