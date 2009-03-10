#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""
import logging

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

from google.appengine.ext import db

import libs.cache as cache


class PackageReleaseData(db.Model):
    name        = db.StringProperty(required=True)
    release     = db.StringProperty(required=True)
    downloads   = db.IntegerProperty(default=0)
    last_update = db.DateTimeProperty()

#cache.memoize('/pypi/db/release_data/', ttl= 15*60, report_freshness=False)
def getPackageReleaseData(name, release):
    """ Database look-up with memcaching
    """
    q = PackageReleaseData.all()
    q.filter("name =", name)
    q.filter("release =", release)
    result = q.fetch(1)
    
    try:
        return result[0]
    except Exception,e:
        pass
        #logging.error(">%s" % e)
    
    return None

def setPackageReleaseData(name, release, downloads, last_update, entity=None):
    """ Stores package release data
    """
    if entity is None:
        d = PackageReleaseData(name=name, release=release, downloads=downloads, last_update=last_update)
        d.put()
    else:
        entity.downloads = downloads
        entity.last_update = last_update
        entity.put()