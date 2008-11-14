""" MindMeister DB class
    @author: Jean-Lou Dupont
    
    Usage:
    import jld.backup.mindmeister_db as dbase
    
    db = dbase.Db(filepath)
    maps = dbase.Maps  #shortcut
    
    maps.select()
    
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
    map = Maps.select(Maps.mapid=='1')
    dir(map)
    m1 = Maps(mapid='1', title='title', created=datetime.datetime.now(), modified=datetime.datetime.now(), tags='', exported=None)
    print m1
    
