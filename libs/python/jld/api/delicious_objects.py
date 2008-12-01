#!/usr/bin/env python
""" Delicious objects
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"


class Tags(object):
    """ Tag List representation
    """
    __slots__ = ['list',]
    def __init__(self, list = []):
        self.list = list
        
            
class Bundle(object):
    """ Bundle representation
    """
    def __init__(self, list = []):
        self.list = list

