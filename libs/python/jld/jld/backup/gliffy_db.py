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
import jld.tools.mos as mos
import jld.tools.db as db

# =============================================
class Diagrams(SQLObject):
    """ Gliffy diagrams database table
    """
    did      = StringCol()
    exported = DateTimeCol()
    
    _attributesToVerify = ['id']

    @classmethod
    def getChangedList(cls, dt):
        """ Returns a list of entries changed since 'dt'
            @param dt: the datetime timestamp to compare against
        """
        return cls.select(OR(cls.q.changed > dt, cls.q.changed == None))
    
    @classmethod
    def getAll(cls, tag = None):
        """ Returns all the entries
            @param tag: filters by tag
            @return: SQLObject list 
        """
        list = []
        if (tag):
            all = cls.select(OR( Posts.q.tag1 == tag, Posts.q.tag2 == tag, Posts.q.tag3 == tag ), 
                             orderBy=DESC(Posts.q.changed))
        else:
            all = cls.select(orderBy=DESC(Posts.q.changed))
            
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
        result['href'] = entry.href
        result['hash'] = entry.hash
        result['description'] = entry.description
        result['time'] = entry.time
        result['tag'] = entry.tag
        result['tag1'] = entry.tag1
        result['tag2'] = entry.tag2
        result['tag3'] = entry.tag3
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
            try:    post = posts[0]
            except: post = None
                
            if (post is None):
                created = created + 1
                cls._createOne( entry )
            else:
                if (cls._updateOne(entry, post)):
                    updated = updated  + 1
                    
        return (total, updated, created)

    @classmethod
    def _extractTags(cls, list):
        """ Extracts the first 3 tags from a list
            @param list: string list
            @return: tuple of 3 items
        """
        if (not list):
            return (None, None, None)
        bits  = list.split(' ',3)
        sbits = bits[0:3]
        cbits = ['' for i in range(0,3-len(sbits))]
        if (cbits):
            sbits.extend(cbits)
        return sbits
        
    @classmethod
    def _createOne(cls, entry):
        """ Creates one post entry
        """
        tag1,tag2,tag3 = cls._extractTags( entry['tag'] )
        Posts(   hash=entry['hash'], 
                 href=entry['href'],
                 description=entry['description'], 
                 tag=entry['tag'],
                 tag1=tag1,
                 tag2=tag2,
                 tag3=tag3,
                 time=entry['time'],
                 changed=datetime.datetime.now() )
        
    @classmethod
    def _updateOne(cls, entry, post):
        """Processes one entry: verifies if the entry needs updating
            @param entry: the entry from Delicious Client API
            @param post:  the sqlobject
            
            @return: True if the entry needed updating
        """
        needsUpdate = False
        for att in cls._attributesToVerify:
            local  = getattr(post, att)
            remote = entry[att]
            #print "att[%s] local[%s] remote[%s]" % (att, local, remote)
            if (local != remote):
                needsUpdate = True
                break
            
        if (needsUpdate):
            tag1, tag2, tag3 = cls._extractTags( entry['tag'] )
            post.set( href=entry['href'],
                     hash=entry['hash'], 
                     tag=entry['tag'],
                     tag1=tag1,
                     tag2=tag2,
                     tag3=tag3,                     
                     description=entry['description'],
                     time=entry['time'],
                     changed=datetime.datetime.now() )           
                
        return needsUpdate
            
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
        Diagrams.createTable(ifNotExists=True)
    
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
