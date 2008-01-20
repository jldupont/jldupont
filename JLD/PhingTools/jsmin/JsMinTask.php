<?php
/**
 * PHING task to 'minify' a Javascript script
 *
 * 	<taskdef classname='JLD.PhingTools.jsmin.JsMinTask' name='jsmin' />
 *	<jsmin	input="input_string"
 *			output="property_name_for_output_result" />
 * 
 * 
 * @author Jean-Lou Dupont
 * @package PhingTools
 * @version @@package-version@@
 * @Id $Id$
 */
//<source lang=php> 

include_once 'jsmin.php';
include_once 'phing/filters/BaseParamFilterReader.php';

class JsMinTask extends BaseParamFilterReader
{
    function read($len = null) 
	{
        // Read XML
        $_jsfile = null;
        while ( ($data = $this->in->read($len)) !== -1 )
            $_jsfile .= $data;

        if ($_jsfile === null ) { // EOF?
            return -1;
        }

        if(empty($_jsfile)) {
            $this->log("JS file is empty!", Project::MSG_WARN);
            return ''; // return empty string
        }
       
        $out = '';
        try 
		{
			$code = JSMin::minify( $_jsfile );
        } 
		catch (Exception $e) 
		{
            throw new BuildException($e);
        }

        return $out;
    }

}
//</source>