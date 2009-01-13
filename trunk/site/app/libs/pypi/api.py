#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import xmlrpclib


class PypiCall(object):
    def __init__(self, method = None):
        self.method = method
        self._server = xmlrpclib.Server('http://pypi.python.org/pypi')
    
    def __getattr__(self, name):
        try:
            return object.__getattr__(self, name)
        except AttributeError:
            return PypiCall(name)
            
    def __call__(self, *args):
        return getattr(self._server, self.method)( *args )
    
            
class Pypi(PypiCall):
    """
        >>> s = Pypi()
        >>> print s.package_releases("jld") # doctest:+ELLIPSIS
        [...]
    """    
    def __init__(self, method = None):
        PypiCall.__init__(self, method)
        
        
# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    import doctest
    doctest.testmod()
