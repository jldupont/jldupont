#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import logging
from types import *

import libs.markup as markup

class WebApi(object):
    def getDoc(self, name, prefix = 'method_'):
        return getattr(self, "%s%s" % (prefix, name)).__doc__

class metaWebApi(type):
    """ Metaclass for Web based API handlers
    """
    def __init__(cls, name, bases, ns):
        try:
            cls._convertReSTDoc( ns )
        except Exception,e:
            logging.warn(e)

    def _getMethods(cls, ns, prefix = None):
        """
        """
        prefix_methods = []
        all_methods = []
        for name in ns:
            if type(getattr(cls,name)) is MethodType:
                if (name.startswith(prefix)):
                    prefix_methods.append( name[len(prefix):] )
                else:
                    all_methods.append( name )
                    
        return (all_methods, prefix_methods)
        
    
    def _convertReSTDoc(cls, ns):
        """ Converts all the docstrings from ReST format to HTML
        """
        cls.__doc__ = markup.renderReSText( cls.__doc__ )
        
        cls._all_methods, cls._api_methods = cls._getMethods(ns, 'method_')
        methods = []  
        for name in cls._api_methods:
            if type(getattr(cls,name)) is MethodType:
                methods.append( name )
        
        for method in methods:
            if not __doc__ in method: 
                continue
            docstring = "%s.__doc__" % method
            doc = getattr(cls, docstring)
            res = markup.renderReSText(doc)
            setattr(cls, docstring, res)
