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
import jld.tools.mos as mos
import jld.tools.db as db

# =============================================

class Posts(SQLObject):
    """ Delicious Posts database
    """
    # Delicious attributes
    #_posts_fields = ['href', 'hash', 'description', 'tag', 'time', 'extended']
    href         = StringCol()
    hash         = StringCol()
    description  = StringCol()
    time         = StringCol() #don't want to have conversion here...
    tags         = StringCol()
    # internal attribute
    changed      = DateTimeCol() #timestamp of last detected modification
    
    _attributesToVerify = ['href', 'hash', 'description','time', 'tags']

    @classmethod
    def getChangedList(cls, dt):
        """ Returns a list of entries changed since 'dt'
            @param dt: the datetime timestamp to compare against
        """
        return cls.select(OR(cls.q.changed > dt, cls.q.changed == None))
    
    @classmethod
    def getAll(cls):
        """ Returns all the entries
        """
        list = []
        all = cls.select()
        for one in all:
            entry = cls._formatOne( one )
            list.append( entry )
            
        return list
    
    @classmethod
    def _formatOne(cls, entry):
        result = {}
        result['href'] = entry.href
        result['hash'] = entry.hash
        result['description'] = entry.description
        result['time'] = entry.time
        result['tags'] = entry.tags
        result['changed'] = entry.changed
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
            hash = entry['hash']
            posts = cls.select( cls.q.hash == hash )
            
            #post already exists?
            try:
                post = posts[0]
            except:
                post = None
                
            cls.formatEntry( entry )
            if (post is None):
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
        Posts(   hash=entry['hash'], 
                 href=entry['href'],
                 description=entry['description'], 
                 tags=entry['tags'], 
                 time=entry['time'],
                 changed=datetime.datetime.now() )
        
    @classmethod
    def _updateOne(cls, entry, post):
        """Processes one entry: verifies if the entry needs updating
            @param entry: the entry
            @param post:  the sqlobject
            
            @return: True if the entry needed updating
        """
        needsUpdate = False
        for att in cls._attributesToVerify:
            local  = getattr(map, att)
            remote = entry[att]
            #print "att[%s] local[%s] remote[%s]" % (att, local, remote)
            if (local != remote):
                needsUpdate = True
                break
            
        if (needsUpdate):
            post.set( href=entry['href'],
                     hash=entry['hash'], 
                     tags=entry['tags'],
                     description=entry['description'],
                     time=entry['time'],
                     changed=datetime.datetime.now() )           
                
        return needsUpdate
            
# ==============================================
class Updates(SQLObject):
    """ Table for keeping track of the I{last update} indicator from Delicious """
    username = StringCol()
    last     = StringCol()

    @classmethod
    def getLatest(cls, username):
        result = cls.select( cls.q.username == username )
        try:
            entry = result[0]
        except:
            entry = None
        
        if entry:
            return entry.last
        
        return None

# ==============================================        


class Db(object):
    """ Db class; used to bootstrap SQLObject 
    """
    def __init__(self, filepath):
        # verify that the db file exists first
        self._createDb(filepath)

        #on windows, watch-out for the \
        #which are interpreted as escape code by SqlObject
        #also, the : on windows should be switched to |        
        sqlobject_filepath = db.formatSqliteURI(filepath)

        try:
            if (filepath == ':memory:'):
                connection_string = 'sqlite:/:memory:'
            else:
                connection_string = 'sqlite:///' + sqlobject_filepath
            connection = connectionForURI( connection_string )
            sqlhub.processConnection = connection
        except Exception,e:
            raise api.ErrorDb( e, {'file':filepath} )

        #table already exists ... no big deal
        Posts.createTable(ifNotExists=True)
        Updates.createTable(ifNotExists=True)
    
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
        if (filepath != ':memory:'):
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
