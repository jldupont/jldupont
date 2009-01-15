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
        for i in t._prefix_methods:
            self.response.out.write(t.renderMethodDocString(i))

class Test(webapi.WebApi):
    """\
    Content
    =======
    
    """    
    def __init__(self):
        webapi.WebApi.__init__(self)
        
    def get(self, name):
        """
        """
        content = self.methodExists(name)
        logging.info( content )
        self._output(200, content)
        
    def method_a(self):
        """\
        Method_a
        --------
        """

    def method_b(self):
        """ method-b
        """
        
    def method_c(self):
        """ method-c
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
