#!/usr/bin/env python
""" Serves as proxy to Pypi

    Caches package release data

    @author: Jean-Lou Dupont
"""
import logging

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

__all__ = ['getPackageReleases', 'getPackageReleaseData']

import datetime as datetime

import api as api
import db as db


class ProxyException(Exception):
    def __init__(self, msg, params = None):
        Exception.__init__(self, msg)
        self.msg = msg
        self.params = params

def getLatestDownloads(name):
    """ Retrieves the latest download count for latest release of package.
    """ 
    latest = getPackageReleases(name)[0]
    downloads = getPackageReleaseData(name, latest)
    return [latest, downloads]

def getPackageReleases(name):
    """ Gets the available releases for a given package.
        The release list is not recorded in the datastore.
    """
    try:
        liste, freshness = api.PypiClient().getPackageReleases(name)
    except Exception,e:
        raise ProxyException("error_package_releases", {"exc":e} )

    return liste
        
def getPackageReleaseData(name, release):
    """ Get the available data for a given [package;version].
        The retrieved data is stored in the datastore.
        
        1) Looks in memcache/datastore
        2) Looks on Pypi directly
        
        @return: downloads count (Integer) or None
    """
    try:
        entity = db.getPackageReleaseData(name, release)
    except Exception,e:
        raise ProxyException("error_package_release_data_datastore_access", {"exc:":e} )
    
    if entity is not None:
        return entity.downloads
    
    try:
        data, freshness = api.PypiClient().getReleaseUrls(name, release)
    except Exception,e:
        raise ProxyException("error_package_release_data", {"exc:":e} )
    
    try:
        downloads = data[0]['downloads']
    except Exception,e:
        raise ProxyException("error_package_release_data_downloads", {"exc:":e} )

    last_update = datetime.datetime.now()
    
    db.setPackageReleaseData(name, release, downloads, last_update)
    
    return downloads

## =======================================================================
## PRIVATE
## =======================================================================

 
