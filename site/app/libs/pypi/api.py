#!/usr/bin/env python
""" Pypi API

    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import logging

import xmlrpclib

import libs.xmlrpc as gaexmlrpc
import libs.cache as cache

class PypiCall(object):
    
    _server = xmlrpclib.ServerProxy('http://pypi.python.org/pypi', gaexmlrpc.GAEXMLRPCTransport())
    
    def __init__(self, method=None):
        self.method = method
    
    def __getattr__(self, name):
        try:
            return object.__getattr__(self, name)
        except AttributeError:
            return PypiCall(name)
            
    def __call__(self, *args, **kargs):
        return getattr(self._server, self.method)( *args, **kargs )


_package_releases_ttl     = 60*60
_package_release_data_ttl = 5*60
_package_release_urls_ttl = 5*60 
    
            
class PypiClient(object):
    """
        >>> s = PypiClient()
        >>> print s.package_releases("jld") # doctest:+ELLIPSIS
        [...]
    """
    _server = PypiCall()
    
    @cache.memoize('/pypi/package_releases/', report_freshness = True, ttl = _package_releases_ttl)
    def getPackageReleases(self, package_name):
        ""
        return self._server.package_releases(package_name, True)
    
    @cache.memoize('/pypi/release_data/', report_freshness = True, ttl = _package_release_data_ttl)
    def getReleaseData(self, package_name, version):
        ""
        return self._server.release_data(package_name, version)
    
    @cache.memoize('/pypi/release_urls/', report_freshness = True, ttl = _package_release_urls_ttl)
    def getReleaseUrls(self, package_name, version):
        ""
        return self._server.release_urls(package_name, version)
        

# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    import doctest
    doctest.testmod()
