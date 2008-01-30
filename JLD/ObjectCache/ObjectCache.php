<?php
/**
 * ObjectCache class definition
 * 
 *
 * @author Jean-Lou Dupont
 * @version @@package-version@@
 * @package ObjectCache
 */

require 'JLD/ObjectCache/Interface.php';
require 'JLD/ObjectCache/Exception.php';
require 'PEAR.php';
require 'MDB2.php';

class ObjectCache 
	implements	ObjectCache_Interface,
				ObjectCache_ManagementInterface
{
	/**
	 * The 'expiry' timeout (in seconds)
	 */
	var $expiry = null;
	/**
	 * The DSN for the required database
	 */	
	var $dsn = null;
	/**
	 * The database name
	 */		 
	var $db = null;	 
	/**
	 * The table name in the database
	 */	
	var $table = null;	 

	
// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// PRODUCTION INTERFACE	
// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	public function setExpiry( $expiry );
	
	public function set( $key, $value );

	public function get( $key );	 
	
	public function delete( $key );	 

	public function clear( );

// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// MANAGEMENT INTERFACE	
// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	public function setDatabaseParameters( $dsn, $databaseName, $tableName );
	
	public function initDatabaseStructure( );

	public function deleteDatabaseStructure( );	 
	
	public function checkDatabaseStructure( );
	

// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// ERROR HANDLING
// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    /**
     * This method is used to communicate an error and invoke error
     * callbacks etc.  Basically a wrapper for PEAR::raiseError
     * without the message string.
     *
     * @param   mixed  int error code
     *
     * @param   int    error mode, see PEAR_Error docs
     *
     * @param   mixed  If error mode is PEAR_ERROR_TRIGGER, this is the
     *                 error level (E_USER_NOTICE etc).  If error mode is
     *                 PEAR_ERROR_CALLBACK, this is the callback function,
     *                 either as a function name, or as an array of an
     *                 object and method name.  For other error modes this
     *                 parameter is ignored.
     *
     * @param   string Extra debug information.  Defaults to the last
     *                 query and native error code.
     *
     * @return PEAR_Error instance of a PEAR Error object
     *
     * @access  private
     * @see     PEAR_Error
     */
    private function &raiseError($code = null, $mode = null, $options = null, $userinfo = null)
    {
        $err =& PEAR::raiseError(null, $code, $mode, $options, $userinfo, 'ObjectCache_Error', true);
        return $err;
    }
    /**
     * Tell whether a value is a ObjectCache error.
     *
     * @param   mixed   the value to test
     * @param   int     if is an error object, return true
     *                        only if $code is a string and
     *                        $db->getMessage() == $code or
     *                        $code is an integer and $db->getCode() == $code
     *
     * @return  bool    true if parameter is an error
     *
     * @access  public
     */
    function isError($data, $code = null)
    {
        if (is_a($data, 'ObjectCache_Error')) {
            if (is_null($code)) {
                return true;
            } elseif (is_string($code)) {
                return $data->getMessage() === $code;
            } else {
                $code = (array)$code;
                return in_array($data->getCode(), $code);
            }
        }
        return false;
    }

}//end class