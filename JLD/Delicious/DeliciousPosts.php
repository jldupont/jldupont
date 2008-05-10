<?php
/**
 * DeliciousPosts
 * Handles an RSS feed of posts
 *
 * @author Jean-Lou Dupont
 * @version @@package-version@@
 * @package Delicious
 * @dependencies PEAR::HTTP_Request
 */

require_once "DeliciousPost.php";
require_once 'HTTP/Request.php';

class JLD_DeliciousPosts 
	implements ArrayAccess, ArrayIterator {

	static $service = "http://del.icio.us/rss/";

	var $feed = null;
	var $xml  = null;
	
	var $rep_headers = null;
	var $rep_body = null;
	var $rep_code = null;

	/**
	 * Index for ArrayIterator Interface
	 */
	var $index = null;
	/**
	 * Serves as 'cache'
	 */
	var $post = array();

	/*********************************************************
	 * 						PUBLIC Interface
	 ********************************************************/	
	
	public function __construct( $feed ) {
	
		$this->feed = $feed;
	}
	
	public function run() {
	
		if ( !$this->fetch() )
			return false;
			
		if ( !$this->parse() )
			return false;

		return true;
	}

	public function getXml() {
	
		return $this->xml;
	}
	/*********************************************************
	 * 				ArrayIterator Interface
	 ********************************************************/	
	public function count() {
	
	}
	public function current() {
	
	}
	public function key() {
	
	}
	public function next() {
	
	}
	public function rewind() {
	
	}
	public function valid() {
	
	}
	/*********************************************************
	 * 				ArrayAccess Interface
	 ********************************************************/	
	/**
	 * 
	 * @param $index integer
	 * @return boolean
	 */
	public function offsetExists( $index ) {
	
		// first check the 'cache'
		if ( isset( $this->posts[ $index ] ) )
			return true;
				
		// then the XML aggregate
		if ( isset( $this->xml["item"][$index])) {
			return true;
		}
		
		return false;
	}
	/**
	 * This method assumes 'offsetExists' has been called 
	 * to ensure that the required $index exists
	 */
	public function offsetGet( $index ) {

		// first check the 'cache'
		if ( isset( $this->posts[ $index ] ) )
			return ( $this->posts[$index] );
				
		// then the XML aggregate
		if ( isset( $this->xml["item"][$index])) {
			// 'cache' it
			$post = new JLD_DeliciousPost( $this->xml["item"][$index] );
			return ( $this->posts[ $index ] = $post );
		}
		throw new Exception( __METHOD__.": unset offset" );
	}
	public function offsetSet( $index, $post ) {
	
		if ( $post instanceof JLD_DeliciousPost ) {

			$this->posts[$index] = $post;
			return $this;
		}

		throw new Exception( __METHOD__.": invalid value" );
	}
	public function offsetUnset( $index ) {
	
		if ( isset( $this->posts[ $index ] ) )
			unset( $this->posts[$index] );
	
		return $this;
	}
	/*********************************************************
	 * 						PROTECTED
	 ********************************************************/	
	
	public function parse() {
	
		try {
			$this->xml = new SimpleXMLElement( $this->rep_body );
		}
		catch( Exception $e ) {
			return false;
		}
		return true;
	}
	
	
	/**
	 * 
	 */
	protected function buildUrl() {
	
		return self::$service . $this->feed;
	}

	
	/**
	 * Fetches the feed
	 * 
	 * @return $this
	 */
	protected function fetch() {
	
		$url = $this->buildUrl();
	
		$request =& new HTTP_Request( $url );
										
		// REDIRECTS are a requirement
		$request->_allowRedirects = true;
		
		$request->setMethod( "GET" );

		try
		{
			$exception = false;
			$code = $request->sendRequest();			
		}
		catch(Exception $e)
		{
			$exception = true;
		}
		
		if ( PEAR::isError( $code ) || $exception )
			return false;

	    $this->rep_headers = $request->getResponseHeader();
		$this->rep_body    = $request->getResponseBody();
		$this->rep_code    = $request->getResponseCode();

		return ( $this->rep_code == 200 );		
	}

}
/*
object(SimpleXMLElement)#115 (2) {
  ["channel"]=>
  object(SimpleXMLElement)#114 (4) {
    ["title"]=>
    string(32) "del.icio.us/jldupont/my-diagrams"
    ["link"]=>
    string(39) "http://del.icio.us/jldupont/my-diagrams"
    ["description"]=>
    object(SimpleXMLElement)#102 (0) {
    }
    ["items"]=>
    object(SimpleXMLElement)#101 (0) {
    }
  }
  ["item"]=>
  array(11) {
    [0]=>
    object(SimpleXMLElement)#110 (3) {
      ["title"]=>
      string(13) "Connectivity2"
      ["link"]=>
      string(37) "http://www.gliffy.com/publish/1425400"
      ["description"]=>
      object(SimpleXMLElement)#100 (0) {
      }
    }
    [1]=>
    object(SimpleXMLElement)#111 (3) {
      ["title"]=>
      string(12) "Connectivity"
      ["link"]=>
      string(37) "http://www.gliffy.com/publish/1425286"
      ["description"]=>
      object(SimpleXMLElement)#99 (0) {
      }
    }
    [2]=>
    object(SimpleXMLElement)#112 (3) {
      ["title"]=>
      string(18) "TypesCommunication"
      ["link"]=>
      string(37) "http://www.gliffy.com/publish/1425219"
      ["description"]=>
      object(SimpleXMLElement)#98 (0) {
      }
    }
    [3]=>
    object(SimpleXMLElement)#113 (3) {
      ["title"]=>
      string(13) "TransferModes"
      ["link"]=>
      string(37) "http://www.gliffy.com/publish/1425215"
      ["description"]=>
      object(SimpleXMLElement)#97 (0) {
      }
    }
    [4]=>
    object(SimpleXMLElement)#109 (3) {
      ["title"]=>
      string(19) "NetworkConnectivity"
      ["link"]=>
      string(37) "http://www.gliffy.com/publish/1424697"
      ["description"]=>
      object(SimpleXMLElement)#96 (0) {
      }
    }
    [5]=>
    object(SimpleXMLElement)#108 (3) {
      ["title"]=>
      string(23) "NetworkFunctionalPlanes"
      ["link"]=>
      string(37) "http://www.gliffy.com/publish/1423596"
      ["description"]=>
      object(SimpleXMLElement)#95 (0) {
      }
    }
    [6]=>
    object(SimpleXMLElement)#107 (3) {
      ["title"]=>
      string(13) "Client_Server"
      ["link"]=>
      string(37) "http://www.gliffy.com/publish/1421994"
      ["description"]=>
      object(SimpleXMLElement)#94 (0) {
      }
    }
    [7]=>
    object(SimpleXMLElement)#106 (3) {
      ["title"]=>
      string(19) "MediaWiki_Extension"
      ["link"]=>
      string(37) "http://www.gliffy.com/publish/1422053"
      ["description"]=>
      object(SimpleXMLElement)#93 (0) {
      }
    }
    [8]=>
    object(SimpleXMLElement)#105 (3) {
      ["title"]=>
      string(20) "NetworkProtocolStack"
      ["link"]=>
      string(37) "http://www.gliffy.com/publish/1422012"
      ["description"]=>
      object(SimpleXMLElement)#92 (0) {
      }
    }
    [9]=>
    object(SimpleXMLElement)#104 (3) {
      ["title"]=>
      string(17) "ProtocolStackFlow"
      ["link"]=>
      string(37) "http://www.gliffy.com/publish/1423462"
      ["description"]=>
      object(SimpleXMLElement)#91 (0) {
      }
    }
    [10]=>
    object(SimpleXMLElement)#103 (3) {
      ["title"]=>
      string(14) "TransportModel"
      ["link"]=>
      string(37) "http://www.gliffy.com/publish/1422789"
      ["description"]=>
      object(SimpleXMLElement)#90 (0) {
      }
    }
  }
}

 */