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
        self.response.out.write(t.__doc__);
        self.response.out.write(t.__init__.__doc__);

class Test(object):
    """\
Content
=======
    """
    __metaclass__ = webapi.WebApi
    
    def __init__(self):
        """\
Initialization:
        """
        
    def method(self):
        pass


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
