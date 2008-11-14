""" MindMeister DB class
    @author: Jean-Lou Dupont
    
    Usage:
    ======
    import jld.backup.mindmeister_db as dbase
    
    db = dbase.Db(filepath)
    maps = dbase.Maps  #shortcut
    
    liste = maps.getToExportList()
    
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import datetime
from sqlobject import *
import sqlite3 as sql

# =============================================
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

class Db(object):
    """ Db class: used to bootstrap SQLObject 
    """
    def __init__(self, filepath):
        connection_string = 'sqlite:' + filepath
        connection = connectionForURI( connection_string )
        sqlhub.processConnection = connection

        #table already exists ... no big deal
        Maps.createTable(ifNotExists=True)
    
# ==============================================
# ==============================================


if __name__ == "__main__":
    """ Tests
    """
    db = Db('/:memory:')
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
    
    
    
