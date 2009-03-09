#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

from google.appengine.ext import db

import libs.cache as cache


class PackageReleaseData(db.Model):
    name        = db.StringProperty(required=True)
    release     = db.StringProperty(required=True)
    downloads   = db.IntegerProperty(default=0)
    last_update = db.DateTimeProperty()

@cache.memoize('/pypi/db/release_data/', ttl= 15*60, report_freshness=True)
def getPackageReleaseData(name, release):
    """ Database look-up with memcaching
    """
    q = PackageReleaseData.all()
    q.filter("name =", name)
    q.filter("release =", release)
    result = q.fetch(1)
    
    
    