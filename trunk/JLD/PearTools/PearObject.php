<?php
/**
 * @author Jean-Lou Dupont
 * @package JLD
 * @subpackage Directory
 * @version $Id$
 */
//<source lang=php> 
require_once 'JLD/Object/Object.php';

abstract class JLD_PearObject extends JLD_Object
{
	var $vars = array();
	
	static $std_magic_words = array(
		'$tab$'		=> "\t",
		'$newline$' => "\n",
	);
	
	public function getVar( $var ) { return @$this->vars[$var]; }
	public function setVar( $var, $value ) { return $this->vars[$var] = $value; }
	
	public function __set( $nm, $val )
	{
		return $this->vars[ $nm ] = $val;
	}
	public function __get( $nm )
	{
		return @$this->vars[ $nm ];
	}
	protected function getTemplate( $tpl )
	{
		return @file_get_contents(dirname(__FILE__).$tpl );
	}
	protected function replaceMagicWords( &$tpl, &$magic_words )
	{
		foreach ( $magic_words as $mg => $varname )
			$tpl = str_replace( $mg, $this->getVar( $varname ), $tpl );

		foreach ( self::$std_magic_words as $mg => $value )
			$tpl = str_replace( $mg, $value, $tpl );
	}
	protected function replaceMagicWords2( $tpl, &$magic_words )
	{
		foreach ( $magic_words as $mg => $varname )
			$tpl = str_replace( $mg, $this->getVar( $varname ), $tpl );

		foreach ( self::$std_magic_words as $mg => $value )
			$tpl = str_replace( $mg, $value, $tpl );
		
		return $tpl;
	}
	/**
	 * Generates an XML file from a XML-ish array structure.
	 */
	protected function toXML( $top, &$s, $level = 0 )
	{
		echo __METHOD__." top=".$top." level=".$level."\n";
		
		if ($level === 0)
			$r .= '<?xml version="1.0" encoding="UTF-8" ?>'."\n";
		else
			$r = null;

		// terminal node?
		if (!is_array( $s ))
			return $s;

		do
		{
			$_attribs = null;
			$_content = null;			
			
			if (empty( $s ))
				break;

			reset( $s );
				
			// <tag attribs...>
			if ( key($s) === 'attribs')
			{
				$_attribs = current( $s );
				
				array_shift( $s );
				$r .= $this->openTag( $top, $level, $_attribs );
				$top = key( $s );				
			}

			// <tag attribs ...>contents</tag>
			if (key($s) === '_content')
			{
				$_content = current( $s );
				array_shift( $s );
				$r .= $_content;
				$r .= $this->closeTag( $top, $level );
				continue;
			}
			else
				$r .= $this->openTag( $top, $level );
				
			$t = key( $s );
			$v = current( $s );
			array_shift( $s );
			
			$r .= $this->toXML( $t, $v, $level+1 );
			$r .= $this->closeTag( $top, $level );
			
			$top = key( $s );

		} while( true ); 
		
		return $r;
	}//function
	protected function openTag( $tag, $level, $attribs = null )
	{
		echo __METHOD__." tag=".$tag."\n";
		$r  = "\n".str_repeat("\t", $level );	
		$r .= '<'.$tag;
		if (!empty( $attribs ))
			foreach( $attribs as $key => &$value )
				$r .= " $key='$value'";
		$r .= '>';		
		return $r;
	}
	protected function openAndCloseTag( $tag, $level, $attribs, $content )
	{
		echo __METHOD__." tag=".$tag." content=".$content."\n";
		$r  = "\n".str_repeat("\t", $level );	
		$r .= '<'.$tag;		
		if (!empty( $attribs ))
			foreach( $attribs as $key => &$value )
				$r .= " $key='$value'";
		$r .= '>'.$content;
		$r .= '</'.$tag.'>';
		return $r;
	}
	protected function closeTag( $tag, $level )
	{
		echo __METHOD__." tag=".$tag."\n";		
		$r .= '</'.$tag.'>';
		return $r;
	}
}//end class
//</source>
/*
array(2) {
  ["attribs"]=>
  array(4) {
    ["xmlns"]=>
    string(48) "http://pear.php.net/dtd/rest.categorypackageinfo"
    ["xmlns:xsi"]=>
    string(41) "http://www.w3.org/2001/XMLSchema-instance"
    ["xmlns:xlink"]=>
    string(28) "http://www.w3.org/1999/xlink"
    ["xsi:schemaLocation"]=>
    string(105) "http://pear.php.net/dtd/rest.categorypackageinfo     http://pear.php.net/dtd/rest.categorypackageinfo.xsd"
  }
  ["pi"]=>
  &array(2) {
    ["p"]=>
    array(7) {
      ["n"]=>
      string(9) "Directory"
      ["c"]=>
      string(27) "jldupont.googlecode.com/svn"
      ["ca"]=>
      array(2) {
        ["attribs"]=>
        array(1) {
          ["xlink:href"]=>
          string(18) "/rest/c/Filesystem"
        }
        ["_content"]=>
        string(10) "Filesystem"
      }
      ["l"]=>
      string(0) ""
      ["s"]=>
      string(50) "Helper class for manipulating directory structures"
      ["d"]=>
      string(0) ""
      ["r"]=>
      array(1) {
        ["attribs"]=>
        array(1) {
          ["xlink:href"]=>
          string(17) "/rest/r/directory"
        }
      }
    }
    ["a"]=>
    array(1) {
      ["r"]=>
      array(3) {
        [0]=>
        array(2) {
          ["v"]=>
          string(5) "1.0.2"
          ["s"]=>
          string(6) "stable"
        }
        [1]=>
        array(2) {
          ["v"]=>
          string(5) "1.0.1"
          ["s"]=>
          string(6) "stable"
        }
        [2]=>
        array(2) {
          ["v"]=>
          string(5) "1.0.0"
          ["s"]=>
          string(6) "stable"
        }
      }
    }
  }
}
*/