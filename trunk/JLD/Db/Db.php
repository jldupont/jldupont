<?php
/**
 * @author Jean-Lou Dupont
 * @package JLD
 * @subpackage Db
 * @version $Id$
 */
//<source lang=php> 

require 'JLD/Object/Object.php';

class JLD_Db_Manager
{
	
} // JLD_Db_Manager


// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


class JLD_Db extends JLD_Object
{
	const thisVersion = '$Id$';
	
	var $server = null;
	var $name = null;
	var $user = null;
	var $password = null;
	
	var $conn = false;
	var $last_error = null;
	
	public function __construct() 
	{
		if ( !function_exists( 'mysql_connect' ) )
			die( __CLASS__.': requires mysql database module.' );
	}
	/**
	 * Sets the database connection parameters.
	 */
	public function setParameters( $server, $name, $user, $password )
	{
		$this->server = $server;
		$this->name = $name;
		$this->user = $user;
		$this->password = $password;
	}
	/**
	 * Opens a database
	 */
	public function open()
	{
		$this->conn = @mysql_connect(	$this->server, 
										$this->user, 
										$this->password, 
										true );
		
		if ($this->conn === false)
		{
			$this->last_error = mysql_error();
			return false;
		}
		$result = @mysql_select_db( $this->name, $this->conn );
		if ($result !== true )
		{
			$this->last_error = mysql_error();
			return false;			
		}
		
		return true;
	}
	/**
	 * Closes a database
	 */
	public function close()
	{
		if ( $this->conn !== false )
			@mysql_close( $this->conn );
	}
} // JLD_Db



// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



abstract class JLD_Db_Table extends JLD_Object
{
	var $db = null;
	var $table_name = null;
	
	var $fields = array();
	
	/**
	 *
	 */
	public function __construct( $name ) 
	{
		$this->table_name = $name;
		
	}
	/**
	 * Returns the fields of the table.
	 */
	public function & getFields()
	{
		$result = @mysql_query("SHOW COLUMNS FROM ".$this->table_name );
		if ($result === false) 
			return false;
			
		$this->fields = array();
		
		if (@mysql_num_rows($result) > 0) 
		{
		    while ($row = @mysql_fetch_assoc($result)) 
				$this->fields[] = $row;	
		}
		@mysql_free_result($result);		
		return $this->fields;	
	}
	/**
	 *
	 */
	public function getRowById( $id ) 
	{
		$result = @mysql_query("SELECT FROM ".$this->table_name." WHERE id=$id" );
		
		// we are supposed to only get 1 hit.
		$row = @mysql_fetch_assoc($result);
		@mysql_free_result($result);
		
		return $row;
	}

	/**
	 *
	 */
	public function getRowByKey( $key ) {}

	/**
	 * Mimics AmazonS3's get by prefix function.
	 */
	public function getRowsByPrefix( $prefix ) 
	{
		$eprefix = mysql_real_escape_string($prefix).'%';
		
		$result = @mysql_query("SELECT FROM ".$this->table_name." WHERE key=".$eprefix );
		if ($result === false)
			return false;

		$this->rows = array();
		
		if (@mysql_num_rows($result) > 0) 
		{
		    while ($row = @mysql_fetch_assoc($result)) 
				$this->rows[] = $row;	
		}
		@mysql_free_result($result);		
		return $this->rows;	
		
	}
	/**
	 *
	 */
	public function insertRow( &$rowData ) {}
	
	/**
	 *
	 */
	public function deleteRowById( $id ) 
	{
		$result = @mysql_query("DELETE FROM ".$this->table_name." WHERE id=$id" );
		return $result;		
	}

	/**
	 *
	 */
	public function deleteRowByKey( $key ) {}
	
	/**
	 *
	 */
	public function deleteExpired()
	{
		$result = @mysql_query("DELETE FROM ".$this->table_name." WHERE expired=1" );
		return $result;		
	}
	
} // JLD_Db_Table
//</source>