#!/usr/bin/env python
"""
    Process tools
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import enumprocess

def findPid(name):
    """ Finds the pid list for process(es) with 'name'.
        Returns the first off the list.
    """
    liste = enumprocess.getPidNames()
    fliste= filter( lambda X: X[1] == name, liste.iteritems() )
    first = fliste[0] if len(fliste) else None
    return first
