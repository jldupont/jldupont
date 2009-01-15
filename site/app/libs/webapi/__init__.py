#!/usr/bin/env python
"""
    WebApi tools
    
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import logging
from types import *

from google.appengine.ext import webapp

import libs.markup as markup

class metaWebApi(type):
    """ Metaclass for Web based API handler classes
    """
    def __init__(cls, name, bases, ns):
        cls._scanMethods(ns, 'method_')
        try:
            cls._convertReSTDoc( ns )
        except Exception,e:
            logging.warn(e)

    def _scanMethods(cls, ns, prefix = None):
        """ 
        """
        cls._all_methods    = map( lambda X:X if type(getattr(cls,X)) is MethodType else None, ns)
        cls._all_methods    = filter( lambda X: X is not None, cls._all_methods)
        cls._prefix_methods = filter( lambda X: X.startswith(prefix), cls._all_methods )
        
        # drop the prefix
        cls._prefix_methods = map( lambda X: X[len(prefix):], cls._prefix_methods)
        
    
    def _convertReSTDoc(cls, ns):
        """ Converts all the docstrings from ReST format to HTML
        """
        cls.__doc__ = markup.renderReSText( cls.__doc__ )
        
        for method in cls._prefix_methods:
            if not __doc__ in method: 
                continue
            docstring = "%s.__doc__" % method
            doc = getattr(cls, docstring)
            res = markup.renderReSText(doc)
            setattr(cls, docstring, res)


# ===========================================================
# ===========================================================



class WebApi( webapp.RequestHandler ):
    __metaclass__ = metaWebApi
    
    def getDoc(self, name, prefix = 'method_'):
        return getattr(self, "%s%s" % (prefix, name)).__doc__
    
    @classmethod
    def methodExists(cls, name):
        """ 
        """
        return name in cls._prefix_methods

    def _output(self, code, content, mime = "text/plain" ):
        self.response.headers["Content-Type"] = mime
        self.response.set_status(code)
        self.response.out.write(content);

