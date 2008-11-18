"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import datetime as datetime

def convertDate( date ):
    """ Converts a date in string format
        to a datastore compatible format
        
        Input format:   YYYY-MM-DD HH:MM:SS.ssssss
        Output format:  datetime
        
        @throws Exception
    """
    sdate = date.split('.')    
    return datetime.datetime.strptime(sdate[0], "%Y-%m-%d %H:%M:%S")
