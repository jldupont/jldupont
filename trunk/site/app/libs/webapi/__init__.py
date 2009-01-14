#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import logging

import libs.markup as markup
import libs.tools.klass  as klass

class WebApi(type):
    """ Metaclass for Web based API handlers
    """
    def __init__(cls, name, bases, ns):
        try:
            cls._convertReSTDoc()
        except Exception,e:
            logging.warn(e)
    
    def _convertReSTDoc(cls):
        """ Converts all the docstrings from ReST format to HTML
        """
        cls.__doc__ = markup.renderReSText( cls.__doc__ )
        
        methods, liste = klass.searchForMethods(cls, '')
        
        for method in methods:
            if not __doc__ in method: 
                continue
            docstring = "%s.__doc__" % method
            doc = getattr(cls, docstring)
            res = markup.renderReSText(doc)
            setattr(cls, docstring, res)

