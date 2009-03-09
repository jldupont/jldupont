#!/usr/bin/env python
""" Serves as proxy to Pypi

    Caches package release data

    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

__all__ = ['getPackageReleases', 'getPackageReleaseData']

import api as api


class ProxyException(Exception):
    def __init__(self, msg, params = None):
        Exception.__init__(self, msg)
        self.msg = msg
        self.params = params

def getPackageReleases(name):
    """ Gets the available releases for a given package.
        The release list is not recorded in the datastore.
    """
    try:
        liste = api.PypiClient().getPackageReleases(name)
    except Exception,e:
        raise ProxyException("error_package_releases", {"exc":e} )
    
    return liste
        
def getPackageReleaseData(name, version):
    """ Get the available data for a given [package;version].
        The retrieved data is stored in the datastore.
        
        1) 
    """
    

## =======================================================================
## PRIVATE
## =======================================================================

 
