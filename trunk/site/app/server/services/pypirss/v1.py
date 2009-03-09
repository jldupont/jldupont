"""
    Service Pypi RSS
    
    @author Jean-Lou Dupont
"""
import os
import sys
import logging
import xmlrpclib
from types import *

import wsgiref.handlers
from google.appengine.ext import webapp

import import_wrapper

import libs.webapi as webapi

import libs.pypi.proxy as proxy

class ServicePypiRss( webapi.WebApi ):
    """\
    Help
    ====
    
     uri: **/services/pypirss/[format]/[package-name]**
    
    - Supported formats: $formats
    
    More information for a method can be obtained, e.g.:
     
     http://$host/services/pypirss/rss/jld/
     
    Testing
    =======
    
    For a working example, use  http://$host/services/pypirss/rss/jld
     
    """
    _formats = [ 'rss' ]
    
    def __init__(self):
        webapi.WebApi.__init__(self)
    
    def get( self, format = None, package_name = None ):

        if format is None or format == '':
            params = {'formats':self._formats, 'host':os.environ['HTTP_HOST']}
            return self.showServiceHelp( params )
        
        if (format not in self._formats):
            self._help_format(format)
            return
                
        if package_name is None:
            self._help_package()
            return
        
        # I know this is confusing...
        resolved_method = "method_%s" % format
        
        ip = self.request.remote_addr
            
        try:
            result = getattr(self, resolved_method)( package_name )
        
        except Exception, e:
            logging.error( "EXCEPTION type[%s] [%s]" % (type(e),e) )
            self.response.set_status(500)
            return

        self._output(200, result, "application/rss+xml")
        logging.info("ip[%s] pkg[%s]" % (ip, package_name))        

    # =================================================
    # HELP
    # =================================================
    def _help_format(self, format):
        help =  """\
                **Error**: unsupported format [$format]
                
                For more information, consult Help_
                
                .. _Help: /services/pypirss/
                """
        params = {'format':format}
        self.showHelp(help, params, True)

    def _help_package(self):
        help =  """\
                **Error**: package name must be specified
                
                For more information, consult Help_
                
                .. _Help: /services/pypirss/
                """
        self.showHelp(help, convert=True)

        
    # =================================================
    # METHODS
    # =================================================

    def method_rss(self, package_name):
        """\
        **Usage**:  /services/pypirss/rss/[package-name]
        """
        return proxy.getLatestDownloads(package_name)


_urls = [ 
          ('/services/pypirss/(.*?)/(.*?)',             ServicePypiRss),
          ('/services/pypirss/(.*?)',                   ServicePypiRss),  
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
