""" Gliffy DB class
    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import os
import datetime

from sqlobject import *
import sqlite3 as sql

import jld.api as api
import jld.tools.db as db

# =============================================
class Diagrams(SQLObject):
    """ Gliffy diagrams database table
    """
    # diagram id
    did      = StringCol()
    #datetime timestamp at which the entry was added to the database
    added    = DateTimeCol()
    #datetime timestamp at which the entry was exported to the filesystem
    exported = DateTimeCol()
    
    _attributesToVerify = ['did']

    @classmethod
    def getToExportList(cls):
        """ Returns a list of entries that aren't exported yet
        """
        return cls.select( cls.q.exported == None )
    
    @classmethod
    def getAll(cls):
        """ Returns all the entries
            @return: SQLObject list 
        """
        list = []
        all = cls.select(orderBy=DESC(cls.q.added))
            
        for one in all:
            entry = cls._formatOne( one )
            list.append( entry )
            
        return list
    
    @classmethod
    def _formatOne(cls, entry):
        """ Format an SQLObject result object (entry)
            to a dictionary object.
        """
        result = {}
        result['did']      = entry.did
        result['added']    = entry.added
        result['exported'] = entry.exported
        return result
    
    @classmethod
    def updateFromList(cls, list):
        """ Updates the database from the specified list
            @param list: the list of dict entries
            @return: tuple( total, updated, created )
        """
        total = len(list);
        updated = 0;  
        created = 0;
        for entry in list:
            did = entry['did']
            diagrams = cls.select( cls.q.did == did )
            
            #post already exists?
            try:    diagram = diagrams[0]
            except: diagram = None
                
            if (diagram is None):
                created = created + 1
                cls._createOne( entry )
            else:
                if (cls._updateOne(entry, post)):
                    updated = updated  + 1
                    
        return (total, updated, created)

    @classmethod
    def _createOne(cls, entry):
        """ Creates one post entry
        """
        Diagrams(did=entry['did'], 
                 exported=None, 
                 added=datetime.datetime.now() )
        
    @classmethod
    def _updateOne(cls, entry, diagram):
        """Processes one entry: verifies if the entry needs updating
            @param entry: the entry from Client API
            @param post:  the sqlobject
            
            @return: True if the entry needed updating
        """
        needsUpdate = False
        for att in cls._attributesToVerify:
            local  = getattr(diagram, att)
            remote = entry[att]
            #print "att[%s] local[%s] remote[%s]" % (att, local, remote)
            if (local != remote):
                needsUpdate = True
                break
            
        if (needsUpdate):
            diagram.set( did=entry['did'],
                         added=entry['added'],
                         exported=datetime.datetime.now() )           
                
        return needsUpdate
            
# ==============================================        

class Db(db.BaseSQLObjectDb):
    def __init__(self, filepath):
        db.BaseSQLObjectDb.__init__(self, filepath)  
    def initTable(self):
        Diagrams.createTable(ifNotExists=True)


# ==============================================
# ==============================================


if __name__ == "__main__":
    """ Tests
    """
    db = Db(':memory:')
