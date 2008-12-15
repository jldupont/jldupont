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
    """ Replaces the '~' string with
        the configured $HOME or $HOMEDRIVE+$HOMEPATH environment variables
    """
    try:
        home      = os.environ['HOME']      if ('HOME' in os.environ ) else None
        homedrive = os.environ['HOMEDRIVE'] if ('HOMEDRIVE' in os.environ ) else None
        homepath  = os.environ['HOMEPATH']  if ('HOMEPATH' in os.environ ) else None

        if (home):
            return path.replace('~', home)
        
        if (homepath):
            return path.replace('~', homedrive + homepath)
    except:
        pass
    
    return path

def createPathIfNotExists(path):
    """ Creates the required path
        IF it does not already exists.
        If the path is a directory => create directory hierarchy
        
        Does not attempt to trap/process exceptions.
    """
    # exists already... bail out
    if (os.path.exists(path)):
        return
    
    # does the folder hierarchy exists?
    dir = os.path.dirname(path)
    if (os.path.exists(dir)):
        return    
    
    if (not os.path.exists(path)):
        os.makedirs( dir )


def createDirIfNotExists(dir):
    """ Creates the specified directory path
        if it does not exist already.
    """
    if (os.path.exists(dir)):
        return

    if (not os.path.exists(dir)):
        os.makedirs( dir )
    

# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    assert( existsPath('C:\\') )
    
    assert( existsDir('C:\\') )
    
    #MUST SET HOME in run configurations...
    home = replaceHome('~')
    assert( existsPath(home) )
    