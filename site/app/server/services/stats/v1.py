"""
    Stats service
    
    Proxy Marshaller for CheeseShop Pypi's XMLRPC interface
    
    @author Jean-Lou Dupont
"""
import os
import sys
import logging
import xmlrpclib

import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.api import urlfetch

import import_wrapper

import libs.markup as markup
import libs.webapi as webapi


class ServiceStats( webapi.WebApi ):
    """\
    Help
    ====
    
     uri: **/services/stats/[method]/[page]**
    
    - Supported methods: $methods
    
    More information for a method can be obtained, e.g.:
     
     http://$host/services/stats/[method]
     
    Testing
    =======
    
    For a working example, use  http://$host/services/stats/
     
    """
    _png_mime   = "image/png"
    
    def __init__(self):
        webapi.WebApi.__init__(self)
    
    def get( self, method = None, param1=None):

        if method is None or method == '':
            params = {'methods':self._prefix_methods, 'host':os.environ['HTTP_HOST']}
            return self.showServiceHelp( params )
        
        if (method not in self._prefix_methods ):
            self._help_method(method)
            return
        
        resolved_method = "method_%s" % method
        
        try:
            code, res, mime = getattr(self, resolved_method)( param1 )
        except Exception,e:
            self._output(500, e)
            return

        self._output(code, res, mime)


    # =================================================
    # HELP
    # =================================================        
    def _help_method(self, method):
        help =  """\
                **Error**: unsupported method [$method]
                
                For more information, consult Help_
                
                .. _Help: /services/stats/
                """
        params = {'method':method}
        self.showHelp(help, params, True)

    def _help_method_parameters(self, method):
        ""
        doc = self.getDoc(method)
        self._output(200, doc, "text/html")

    # =================================================
    # METHODS
    # =================================================

    def method_pagestats(self, package_name):
        """\
        **Usage**:  /services/stats/pagestats/page-name
        """
        return 200, "method_pagestats", "text/html"
    


_urls = [ 
          ('/services/stats/(.*?)/(.*?)',            ServiceStats),  
          ('/services/stats/(.*?)',                  ServiceStats),          
         ]                        
        
#/**
# *  Initialize http handler
# */
def main():
  application = webapp.WSGIApplication(_urls, debug=True)
  wsgiref.handlers.CGIHandler().run(application)

# Bootstrap
if __name__ == "__main__":
    main()
