<?php
/**
 * Gliffy
 * Handles 
 *
 * @author Jean-Lou Dupont
 * @version @@package-version@@
 * @package Gliffy
 * @dependencies [optional] JLD/Delicious
 * @example
 * 		$posts = new JLD_DeliciousPosts( 'jldupont/Mediawiki' );
 * 		$posts->run();
 * 		foreach( $o as $post )
 *			$this->assertEquals( $post instanceof JLD_DeliciousPost, true );		
 * 
 */
/*******************************************************************
	<item rdf:about="http://www.gliffy.com/publish/1422789/">
	<title>TransportModel</title>
	<link>http://www.gliffy.com/publish/1422789/</link>
	<description></description>
	<dc:creator>jldupont</dc:creator>
	<dc:date>2008-05-12T00:15:15Z</dc:date>
	<dc:subject>my-diagrams</dc:subject>
	<taxo:topics>
	  <rdf:Bag>
	    <rdf:li resource="http://del.icio.us/tag/my-diagrams" />
	  </rdf:Bag>
	</taxo:topics>
	</item>
 */

require_once 'Gliffy_Delicious.php';

class JLD_Gliffy { 

	var $title = null;
	var $link  = null;

	/**
	 * API end-point
	 */
	static $service = "http://www.gliffy.com/";
	
	/**
	 * Supported representations
	 */
	static $repr = array(
		'page'		=> self::$service.'publish/%id%',
		'jpg_large'	=> self::$service.'publish/%id%/L.jpg',
		'jpg_medium'=> self::$service.'publish/%id%/M.jpg',
		'jpg_small'	=> self::$service.'publish/%id%/S.jpg',
		'jpg_thumb'	=> self::$service.'publish/%id%/T.jpg',	
	);

	var $id = null;
	
	/*********************************************************
	 * 						PUBLIC Interface
	 ********************************************************/	
	
	public function __construct( $id = null ) {
	
		$this->id = $id;
	}
	/**
	 * FACTORY instance from DeliciousPost instance
	 * 
	 * @return JLD_Gliffy object instance
	 */
	public static function newFromDeliciousPost( $obj ) {
	
		if !( $obj instanceof JLD_DeliciousPost )
			throw new Exception( "requires an instance of JLD_DeliciousPost class" );

		$id = JLD_Gliffy_Delicious::extractId( $obj );

		return new JLD_Gliffy( $id );
	}
	/**
	 * Returns an URL pointing to the requested
	 * representation
	 * 
	 * @param $repType string: representation type
	 * @return $url string
	 */
	public function getUrl( $repType = null ) {
	
		if ( is_null( $this->id ) )
			throw new Exception( "diagram id not initialized" );
	
		if !( array_key_exists( $repType, self::$repr ) )
			throw new Exception( "representation type not supported" );

		return $this->formatForRepresentationType( $repType );
	}
	/**
	 * Actually performs the formatting based on the required
	 * representation type.
	 * 
	 * @param $repType string
	 * @return $url string
	 */
	protected function  formatForRepresentationType( $repType ) {
	
		$format = self::$repr[ $repType ];
		
		return str_replace( '%id%', $this->id, $format );
	}
	
} // end class definition

/*
<?xml version="1.0" encoding="UTF-8"?>

<rdf:RDF
 xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
 xmlns="http://purl.org/rss/1.0/"
 xmlns:cc="http://web.resource.org/cc/"
 xmlns:content="http://purl.org/rss/1.0/modules/content/"
 xmlns:taxo="http://purl.org/rss/1.0/modules/taxonomy/"
 xmlns:dc="http://purl.org/dc/elements/1.1/"
 xmlns:syn="http://purl.org/rss/1.0/modules/syndication/"
 xmlns:admin="http://webns.net/mvcb/"
>

<channel rdf:about="http://del.icio.us/jldupont/my-diagrams">
<title>del.icio.us/jldupont/my-diagrams</title>
<link>http://del.icio.us/jldupont/my-diagrams</link>
<description></description>
<cc:license rdf:resource="http://creativecommons.org/licenses/publicdomain/" />
<items>
 <rdf:Seq>
  <rdf:li rdf:resource="http://www.gliffy.com/publish/1422789/" />
  <rdf:li rdf:resource="http://www.gliffy.com/publish/1423462/" />
  <rdf:li rdf:resource="http://www.gliffy.com/publish/1422012/" />
  <rdf:li rdf:resource="http://www.gliffy.com/publish/1422053/" />
  <rdf:li rdf:resource="http://www.gliffy.com/publish/1421994/" />
  <rdf:li rdf:resource="http://www.gliffy.com/publish/1423596/" />
  <rdf:li rdf:resource="http://www.gliffy.com/publish/1424697/" />
  <rdf:li rdf:resource="http://www.gliffy.com/publish/1425215/" />
  <rdf:li rdf:resource="http://www.gliffy.com/publish/1425219/" />
  <rdf:li rdf:resource="http://www.gliffy.com/publish/1425286/" />
  <rdf:li rdf:resource="http://www.gliffy.com/publish/1425400/" />
 </rdf:Seq>
</items>
</channel>

<item rdf:about="http://www.gliffy.com/publish/1422789/">
<title>TransportModel</title>
<link>http://www.gliffy.com/publish/1422789/</link>
<description></description>
<dc:creator>jldupont</dc:creator>
<dc:date>2008-05-12T00:15:15Z</dc:date>
<dc:subject>my-diagrams</dc:subject>
<taxo:topics>
  <rdf:Bag>
    <rdf:li resource="http://del.icio.us/tag/my-diagrams" />
  </rdf:Bag>
</taxo:topics>
</item>

<item rdf:about="http://www.gliffy.com/publish/1423462/">
<title>ProtocolStackFlow</title>
<link>http://www.gliffy.com/publish/1423462/</link>
<description></description>
<dc:creator>jldupont</dc:creator>
<dc:date>2008-05-12T00:15:01Z</dc:date>
<dc:subject>my-diagrams</dc:subject>
<taxo:topics>
  <rdf:Bag>
    <rdf:li resource="http://del.icio.us/tag/my-diagrams" />
  </rdf:Bag>
</taxo:topics>
</item>

<item rdf:about="http://www.gliffy.com/publish/1422012/">
<title>NetworkProtocolStack</title>
<link>http://www.gliffy.com/publish/1422012/</link>
<description></description>
<dc:creator>jldupont</dc:creator>
<dc:date>2008-05-12T00:14:50Z</dc:date>
<dc:subject>my-diagrams</dc:subject>
<taxo:topics>
  <rdf:Bag>
    <rdf:li resource="http://del.icio.us/tag/my-diagrams" />
  </rdf:Bag>
</taxo:topics>
</item>

<item rdf:about="http://www.gliffy.com/publish/1422053/">
<title>MediaWiki_Extension</title>
<link>http://www.gliffy.com/publish/1422053/</link>
<description></description>
<dc:creator>jldupont</dc:creator>
<dc:date>2008-05-12T00:14:37Z</dc:date>
<dc:subject>my-diagrams</dc:subject>
<taxo:topics>
  <rdf:Bag>
    <rdf:li resource="http://del.icio.us/tag/my-diagrams" />
  </rdf:Bag>
</taxo:topics>
</item>

<item rdf:about="http://www.gliffy.com/publish/1421994/">
<title>Client_Server</title>
<link>http://www.gliffy.com/publish/1421994/</link>
<description></description>
<dc:creator>jldupont</dc:creator>
<dc:date>2008-05-12T00:14:23Z</dc:date>
<dc:subject>my-diagrams</dc:subject>
<taxo:topics>
  <rdf:Bag>
    <rdf:li resource="http://del.icio.us/tag/my-diagrams" />
  </rdf:Bag>
</taxo:topics>
</item>

<item rdf:about="http://www.gliffy.com/publish/1423596/">
<title>NetworkFunctionalPlanes</title>
<link>http://www.gliffy.com/publish/1423596/</link>
<description></description>
<dc:creator>jldupont</dc:creator>
<dc:date>2008-05-12T00:14:08Z</dc:date>
<dc:subject>my-diagrams</dc:subject>
<taxo:topics>
  <rdf:Bag>
    <rdf:li resource="http://del.icio.us/tag/my-diagrams" />
  </rdf:Bag>
</taxo:topics>
</item>

<item rdf:about="http://www.gliffy.com/publish/1424697/">
<title>NetworkConnectivity</title>
<link>http://www.gliffy.com/publish/1424697/</link>
<description></description>
<dc:creator>jldupont</dc:creator>
<dc:date>2008-05-12T00:13:52Z</dc:date>
<dc:subject>my-diagrams</dc:subject>
<taxo:topics>
  <rdf:Bag>
    <rdf:li resource="http://del.icio.us/tag/my-diagrams" />
  </rdf:Bag>
</taxo:topics>
</item>

<item rdf:about="http://www.gliffy.com/publish/1425215/">
<title>TransferModes</title>
<link>http://www.gliffy.com/publish/1425215/</link>
<description></description>
<dc:creator>jldupont</dc:creator>
<dc:date>2008-05-12T00:13:31Z</dc:date>
<dc:subject>my-diagrams</dc:subject>
<taxo:topics>
  <rdf:Bag>
    <rdf:li resource="http://del.icio.us/tag/my-diagrams" />
  </rdf:Bag>
</taxo:topics>
</item>

<item rdf:about="http://www.gliffy.com/publish/1425219/">
<title>TypesCommunication</title>
<link>http://www.gliffy.com/publish/1425219/</link>
<description></description>
<dc:creator>jldupont</dc:creator>
<dc:date>2008-05-12T00:12:57Z</dc:date>
<dc:subject>my-diagrams</dc:subject>
<taxo:topics>
  <rdf:Bag>
    <rdf:li resource="http://del.icio.us/tag/my-diagrams" />
  </rdf:Bag>
</taxo:topics>
</item>

<item rdf:about="http://www.gliffy.com/publish/1425286/">
<title>Connectivity</title>
<link>http://www.gliffy.com/publish/1425286/</link>
<description></description>
<dc:creator>jldupont</dc:creator>
<dc:date>2008-05-12T00:12:30Z</dc:date>
<dc:subject>my-diagrams</dc:subject>
<taxo:topics>
  <rdf:Bag>
    <rdf:li resource="http://del.icio.us/tag/my-diagrams" />
  </rdf:Bag>
</taxo:topics>
</item>

<item rdf:about="http://www.gliffy.com/publish/1425400/">
<title>Connectivity2</title>
<link>http://www.gliffy.com/publish/1425400/</link>
<description></description>
<dc:creator>jldupont</dc:creator>
<dc:date>2008-05-12T00:12:05Z</dc:date>
<dc:subject>my-diagrams</dc:subject>
<taxo:topics>
  <rdf:Bag>
    <rdf:li resource="http://del.icio.us/tag/my-diagrams" />
  </rdf:Bag>
</taxo:topics>
</item>

</rdf:RDF>

 */