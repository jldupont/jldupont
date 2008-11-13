""" MindMeister DB class
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import sqlite3 as sql

class MM_db_Exception(Exception):
    """ MindMeister DB Exception class
    """ 
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return str(self.msg)

    
# =============================================
# =============================================


class MM_db(object):
    """ MindMeister DB class
        Used to store maps related information
    """
    
    # mapid:      id
    # created:    creation date of map through MindMeister
    # modified:    date of last modification of map
    # title:        title
    # tags:        text tags
    # exported:    date stamp of last export performed
    #                This should correspond to the 'modified' stamp when in sync
    #                i.e. when the latest version of the map is exported
    _schema = """(mapid text, created text, modified text, title text, tags text, exported text)
    """
    
    def __init__(self, filepath, tableName = 'maps'):
        self.filepath = filepath
        self.db = None
        self.table = tableName
    
    def update(self, list):
        """ Performs requested updates
            
        """
        self._prepare()
    
    def getOutOfDate(self):
        """ Returns a list of out-of-date mapId
            i.e. the 'modified' date does not correspond
            to the 'exported' date
        """
        self._prepare()
        
    
    def getRow(self, mapId):
        """ Retrieves an entry by mapId
            Returns None OR entry (dict)
        """
        self._prepare()
                
    def deleteRow(self, mapId):
        """ Deletes a specific row by mapId
            If row does not exists, return with None
        """
        self._prepare()
                
    def close(self):
        """ Closes the database IF already opened
        """
        if (self.db is not None):
            self.db.close()
            
    # ============================
    # PRIVATE
    # ============================
    def _prepare(self):
        """ Preparation
        
            Creates the table if it does
            not already exists
        """
        try:
            self.db = sql.connect( self.filepath, isolation_level = None )
        except:
            raise MM_db_Exception( "can't connect to database file [%s]" % self.filepath)
        
        # prepare Create-Table statement
        stm = """create table IF NOT EXISTS %s %s
        """ % (self.table, self.schema)
        
        try:
            r = self.db.execute( stm )
        except:
            raise MM_db_Exception( "exception whilst creating database table[%s]" % self.table)
        
    