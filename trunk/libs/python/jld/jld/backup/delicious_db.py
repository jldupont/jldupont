""" Delicious DB class
    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id: mindmeister_db.py 708 2008-12-04 13:40:35Z JeanLou.Dupont $"

import os
import datetime

from sqlobject import *
import sqlite3 as sql

import jld.api as api
import jld.tools.date as tdate
import jld.tools.mos as mos
import jld.tools.db as db

# =============================================

class Posts(SQLObject):
    """ Delicious Posts database
    """
    # Delicious attributes
    mapid    = StringCol()
    title    = StringCol()
    created  = DateTimeCol()
    modified = DateTimeCol()
    tags     = StringCol()
    # internal attribute
    
    #timestamp of the map exported i.e. corresponds to the
    #'modified' attribute of the mindmeister map attributes
    exported = DateTimeCol() 
    
    _attributesToVerify = ['title', 'modified', 'tags']
    
    @classmethod
    def getToExportList(cls):
        """ Selects the maps for which 
            'exported' < 'modified' 
            i.e. exported datime is older
                OR exported == None
        """
        return cls.select(OR(cls.q.modified != cls.q.exported, cls.q.exported == None))
    
    @classmethod
    def getExportList(cls):
        list = []
        all = cls.getToExportList()
  
        for one in all:
            entry = cls.formatOne(one)
            list.append( entry )
        return list
    
    @classmethod
    def getAll(cls):
        list = []
        all = cls.select()
        for one in all:
            entry = cls.formatOne( one )
            list.append( entry )
            
        return list
    
    @classmethod
    def formatOne(cls, entry):
        result = {}
        result['mapid'] = entry.mapid
        result['title'] = entry.title
        result['created'] = entry.created
        result['modified'] = entry.modified
        result['tags'] = entry.tags
        result['exported'] = entry.exported
        return result
    
    @classmethod
    def updateFromList(cls, list):
        """ Updates the database from the specified list
        """
        total = len(list);
        updated = 0;  
        created = 0;
        for entry in list:
            id = entry['mapid']
            map = Maps.select( Maps.q.mapid == id )
            try:
                mid = map[0].mapid
            except:
                mid = None
                
            cls.formatEntry( entry )
            if (mid is None):
                created = created + 1
                Maps(   mapid=entry['mapid'], 
                         title=entry['title'],
                         modified=entry['modified'], 
                         exported=entry.get('exported'), 
                         tags=entry['tags'],
                         created=entry['created'])
            else:
                if (cls._processOne(entry, map[0])):
                    updated = updated  + 1
                    
        return (total, updated, created)
        
    @classmethod
    def _processOne(cls, entry, map):
        """Processes one entry: verifies if the entry needs updating
            entry
                the map entry
            map
                the map sqlobject
            
            Returns True if the entry needed updating
        """
        updated = False
        for att in cls._attributesToVerify:
            local  = getattr(map, att)
            remote = entry[att]
            #print "att[%s] local[%s] remote[%s]" % (att, local, remote)
            if (local != remote):
                updated = True
                break
            
        if (updated):
            map.set( title=entry['title'],
                     modified=entry['modified'], 
                     tags=entry['tags'],
                     created=entry['created'])           
                
        return updated
    
    @classmethod
    def formatEntry(cls, entry):
        """
        """
        entry['modified'] = tdate.convertDate( entry['modified'] )
        entry['created'] = tdate.convertDate( entry['created'] )
            
# ==============================================        


class Db(object):
    """ Db class: used to bootstrap SQLObject 
    """
    def __init__(self, filepath):
        # verify that the db file exists first
        self._createDb(filepath)

        #on windows, watch-out for the \
        #which are interpreted as escape code by SqlObject
        #also, the : on windows should be switched to |        
        sqlobject_filepath = db.formatSqliteURI(filepath)

        try:
            connection_string = 'sqlite:///' + sqlobject_filepath
            connection = connectionForURI( connection_string )
            sqlhub.processConnection = connection
        except Exception,e:
            raise api.ErrorDb( e, {'file':filepath} )

        #table already exists ... no big deal
        Maps.createTable(ifNotExists=True)
    
    @classmethod
    def deleteDb(cls, filepath):
        """ Deletes the corresponding filesystem db file
        """
        try:
            os.remove(filepath)
        except:
            pass
    
    def _createDb(self, filepath):
        """ Handles the creation, if necessary,
            of the database file. The tricky part
            being the creation of the folder hierarchy
            (if required).
        """
        try:
            mos.createPathIfNotExists(filepath)
        except Exception,e:
            raise api.ErrorDb( e, {'file':filepath} )
        
        # lastly, try to create the db
        try:
            dbfile = sql.connect( filepath )
            dbfile.close()
        except Exception,e:
            raise api.ErrorDb( e, {'file':filepath} )

    
# ==============================================
# ==============================================


if __name__ == "__main__":
    """ Tests
    """
    db = Db(':memory:')
