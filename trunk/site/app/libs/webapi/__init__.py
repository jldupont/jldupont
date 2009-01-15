#!/usr/bin/env python
"""
    WebApi tools
    
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import logging
from types import *
from string import Template

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
            logging.warn("metaWebApi cls[%s] exception[%s]" % (cls, e))

    def _scanMethods(cls, ns, prefix = ''):
        """ 
        """
        cls._all_methods    = map(    lambda X:X if type(getattr(cls,X)) is MethodType else None, ns)
        cls._all_methods    = filter( lambda X: X is not None, cls._all_methods)
        if cls._all_methods:
            cls._prefix_methods = filter( lambda X: X.startswith(prefix), cls._all_methods )
        
        # drop the prefix
        cls._prefix_methods = map( lambda X: X[len(prefix):], cls._prefix_methods)
        
    
    def _convertReSTDoc(cls, ns):
        """ Converts all the docstrings of the
            class from ReST format to HTML
        """
        _classdocstring = getattr(cls, '__doc__')
        cls.__doc__ = cls.renderDocString(_classdocstring )
        
        for method in cls._prefix_methods:           
            docstring = "%s%s" % (method,'.__doc__')
            
            try:    doc = getattr(cls, docstring)
            except: doc = ''
            
            res = cls.renderDocString(doc)
            setattr(cls, docstring, res)

    def renderDocString(cls, string):
        _processed = cls._preprocessDocString(string)
        rendered = markup.renderReSText(_processed)
        return rendered
         

    def _preprocessDocString(cls, doc):
        """ Trims leading spaces according to the first line.
            Helps keep docstring readable in the original python file.
        """
        if not doc:
            return ''
        
        lines = doc.splitlines()
        try:    
            firstline = lines[0].strip()
            spacer_count = len(lines[0]) - len(firstline)
        except: 
            return ''
        
        result = firstline + "\n"
        lines.pop(0)
        
        for line in lines:
            result = result + line[spacer_count:] + "\n"
        
        return result
        

# ===========================================================
# ===========================================================



class WebApi( webapp.RequestHandler ):
    __metaclass__ = metaWebApi
    
    _mime_html = "text/html"
    
    def renderMethodDocString(self, name, prefix='method_'):
        _doc = self.getDoc(name, prefix)
        return WebApi.renderDocString(_doc)
    
    def getDoc(self, name, prefix = 'method_'):
        return getattr(self, "%s%s" % (prefix, name)).__doc__
    
    @classmethod
    def methodExists(cls, name):
        return name in cls._prefix_methods

    def _output(self, code, content, mime = "text/plain" ):
        self.response.headers["Content-Type"] = mime
        self.response.set_status(code)
        self.response.out.write(content);

    def showServiceHelp(self, params = None):
        """
        """
        self.showHelp(self.__doc__, params)
        
    def showHelp(self, doc, params, convert = False):
        if convert:
            doc = WebApi.renderDocString(doc)
        t = Template(doc)
        self._output(200, t.substitute(params), self._mime_html)
        