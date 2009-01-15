"""
    @author Jean-Lou Dupont
"""
import os
import sys
import logging

import wsgiref.handlers
from google.appengine.ext import webapp

import import_wrapper

import libs.webapi as webapi

class Service( webapp.RequestHandler ):
    """
    """
    def __init__(self):
        pass
    
    def _output(self, mime, code, content):
        self.response.headers["Content-Type"] = mime
        self.response.set_status(code)
        self.response.out.write(content);

    def get(self, *args):
        """
        """
        t = Test()
        self.response.out.write(t.__doc__)
        for i in t._api_methods:
            self.response.out.write(t.getDoc(i))

class Test(webapi.WebApi):
    """\
Content
=======
    """
    __metaclass__ = webapi.metaWebApi
    
    def __init__(self):
        """\
Initialization:
        """
        webapi.WebApi.__init__(self)
        
    def method_a(self):
        """ method-a
        """

    def method_b(self):
        """ method-b
        """

# ===================================================
# ===================================================



_urls = [ ('/services/test/(.*?)', Service), 
         ]                        
        
#/**
# *  Initialize http handler
# */
def main():
  application = webapp.WSGIApplication(_urls, debug=True)
  wsgiref.handlers.CGIHandler().run(application)

# Bootstrap
#  It all starts here
if __name__ == "__main__":
    main()
