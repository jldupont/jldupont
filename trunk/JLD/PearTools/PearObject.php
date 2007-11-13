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
	}

}
//</source>