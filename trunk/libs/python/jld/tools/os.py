#!/usr/bin/env python
""" OS tools
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import os
from stat import *

def existsPath(path):
    """ Verifies the existence of 'path'
    """
    path = replaceHome(path)
    print path
    try:    info  = os.stat(path)
    except: return False    
    return  info

def existsDir(path):
    """ Verifies the existence of 'path'
        and verifies it corresponds to a 'directory'
    """
    info = existsPath(path)
    if (info is False):
        return False
    
    try:
        mode  = info[ST_MODE]
        isdir = S_ISDIR(mode)
    except:
        return False
    
    return True

def replaceHome(path):
    print os.environ['HOME']
    home = os.environ['HOME'] if ('HOME' in os.environ ) else None
    if (home is None):
        return path
    return path.replace('~', home)

# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    print existsPath('C:\\')
    
    print existsDir('C:\\')
    
    #MUST SET HOME in run configurations...
    print existsPath('~')
    