""" MindMeister DB class
    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import datetime
from sqlobject import *
import sqlite3 as sql

import jld.api as api
import jld.tools.date as tdate

# =============================================

class Maps(SQLObject):
    """ MindMeister Maps database
        Used to store map related information
    """
    mapid    = StringCol()
    title    = StringCol()
    created  = DateTimeCol()
    modified = DateTimeCol()
    tags     = StringCol()
    exported = DateTimeCol()
    
    @classmethod
    def getToExportList(cls):
        """ Selects the maps for which 
            'exported' < 'modified' 
            i.e. exported datime is older
                OR exported == None
        """
        return cls.select(OR(cls.q.modified > cls.q.exported, cls.q.exported == None))
    
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
        updated = 0;  created = 0;
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
                updated = updated  + 1
                map.set( title=entry['title'],
                         modified=entry['modified'], 
                         exported=entry['exported'], 
                         tags=entry['tags'],
                         created=entry['created'])
            
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
        try:
            connection_string = 'sqlite:/' + filepath
            connection = connectionForURI( connection_string )
            sqlhub.processConnection = connection
        except Exception,e:
            raise api.ErrorDb( e, {'file':filepath} )

        #table already exists ... no big deal
        Maps.createTable(ifNotExists=True)
    
    
# ==============================================
# ==============================================


if __name__ == "__main__":
    """ Tests
    """
    db = Db(':memory:')
    #Maps._connection.debug = True
    
    before = datetime.datetime(1971, 03, 31)
    now = datetime.datetime.now()
    after = datetime.datetime(2030, 03, 31)
    
    #print 'before: %s' % before
    #print 'now: %s' % now
    
    m1 = Maps(mapid='1', modified=now, tags='', exported=before, title='title', created=datetime.datetime.now(), )
    m2 = Maps(mapid='2', modified=now, tags='', exported=None, title='title', created=datetime.datetime.now(), )
    m3 = Maps(mapid='3', modified=now, tags='', exported=after, title='title', created=datetime.datetime.now(), )    
    
    list = Maps.getToExportList()
    for item in list:
        print item
    
    print Maps.select(Maps.q.mapid=="4").count()

    m4  = Maps(mapid='4', modified=now, tags='', exported=None, title='title4', created=datetime.datetime.now(), )
    m4_ = Maps(mapid='4', modified=now, tags='', exported=None, title='title4_', created=datetime.datetime.now(), )
    
    print Maps.select(Maps.q.mapid=="4")[0].title
    
    print "####################"
    m5  = Maps(mapid='5', modified=now, tags='', exported=None, title='title5', created=datetime.datetime.now(), )
    m5.set(title='title5__')
    print Maps.select(Maps.q.mapid=="5")[0].title
    
    print Maps.select(Maps.q.mapid=="6").count()
    
    print "####################"
    d = { 'mapid': '6', 'modified':now, 'tags':'', 'exported':None, 'title':"map 6", 'created':now }
    m6 = Maps(d)
    print m6