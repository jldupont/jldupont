""" MindMeister DB class
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import sqlite3 as sql
from string import Template
from types import *

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
    
    _fields = ['mapid', 'created', 'modified', 'title', 'tags', 'exported']
    
    _stm_upd = """INSERT OR REPLACE INTO %s (%s) VALUES(%s)
    """
    
    _stm_select = """SELECT * FROM %s WHERE %s = %s
    """
    
    def __init__(self, filepath, tableName = 'maps'):
        self.filepath = filepath
        self.db = None
        self.table = tableName
        self._fields = sorted( self._fields )
    
    def update(self, entries):
        """ Performs requested updates
            entries: a list of dict entry 
        """
        self._prepare()
        if (entries is None):
            return
        
        for entry in entries:
            assert( type(entry) is DictType )
            s_entry = self._sortDict( entry )
                        
            try:
                self.db.execute( self._stm_upd, s_entry )
            except Exception,e:
                raise MM_db_Exception( e )
            
    
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
        if (mapId is None):
            return None
        
        try:
            self.db.execute()
        except Exception,e:
            raise MM_db_Exception( e )
            
        return
                
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
            self.db.execute( stm )
        except:
            raise MM_db_Exception( "exception whilst creating database table[%s]" % self.table)
        
    
    def _prepareUpdateStatement(self):
        """ Prepares the sqlite statement used
            for the update process. 
            The fields are sorted by alphabetical order.
        """
        fields = ''  ;  holders = ''
        for field in self._fields:
            fields  = fields + field + ','
            holders = holders + '?,'
        fields  = fields.rstrip(',')
        holders = holders.rstrip(',') 
            
        stm = self._stm_upd % (self.table, fields, holders)
        self.stm_upd = Template( stm )
        
    def _sortDict(self, adict):
        """ Sorts a dictionary by key
        """
        keys = adict.keys()
        keys.sort()
        return map(adict.get, keys)