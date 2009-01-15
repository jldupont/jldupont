"""
    Service Pypi
    
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

import libs.xmlrpc as gaexmlrpc
import libs.simplejson as json
import libs.markup as markup
import libs.webapi as webapi


class ServicePypi( webapi.WebApi ):
    """\
    Help
    ====
    
     uri: **/services/pypi/[format]/[method]/[package-name]/[package-version]**
    
    - Supported methods: $methods
    - Supported formats: $formats
    """
    _formats = [ 'json' ]
    _mimes   = { 'json':'text/javascript' }
    
    _server = xmlrpclib.ServerProxy('http://pypi.python.org/pypi', gaexmlrpc.GAEXMLRPCTransport())
    
    def __init__(self):
        webapi.WebApi.__init__(self)
    
    def get( self, format = None, method = None, package_name = None, version = None ):

        if format is None or format == '':
            params = {'methods':self._prefix_methods, 'formats':self._formats}
            return self.showServiceHelp( params )
        
        if (format not in self._formats):
            self._help_format(format)
            return
        
        if (method not in self._prefix_methods ):
            self._help_method(method)
            return
        
        mime = self._mimes[format]
        
        ip = self.request.remote_addr
        logging.info("ip[%s] method[%s] pkg[%s] version[%s]" % (ip, method, package_name, version))
        
        resolved_method = "method_%s" % method
        try:
            if version:
                raw = getattr(self, resolved_method)(package_name, version)
            else:
                raw = getattr(self, resolved_method)(package_name)
            
            res = json.dumps( raw )
            
        except Exception,e:
            logging.error( e )
            #self.response.out.write('map with id[%s] not found/available (or timeout occured)' % id);
            self.response.set_status(404)
            return
        
        self._output(200, res, mime)


    # =================================================
    # HELP
    # =================================================
    def _help_format(self, format):
        help =  """\
                **Error**: unsupported format [$format]
                
                For more information, consult Help_
                
                .. _Help: /services/pypi/
                """
        params = {'format':format}
        self.showHelp(help, params, True)
        
    def _help_method(self, method):
        help =  """\
                **Error**: unsupported method [$method]
                
                For more information, consult Help_
                
                .. _Help: /services/pypi/
                """
        params = {'method':method}
        self.showHelp(help, params, True)

        

    # =================================================
    # METHODS
    # =================================================

    def method_package_releases(self, pkg):
        """ Usage:  /services/pypi/[format]/package_releases/[package-name]
        """
        return self._server.package_releases(pkg,True)
    
    def method_release_urls(self, pkg, version):
        """ Usage:  /services/pypi/[format]/release_urls/[package-name]/[package-version]
        """        
        return self._server.release_urls(pkg, version)
    
    def method_release_data(self, pkg, version):
        """ Usage:  /services/pypi/[format]/release_data/[package-name]/[package-version]
        """        
        return self._server.release_data(pkg, version)


_urls = [ 
          ('/services/pypi/(.*?)/(.*?)/(.*?)/(.*?)', ServicePypi),
          ('/services/pypi/(.*?)/(.*?)/(.*?)', ServicePypi),
          ('/services/pypi/(.*?)', ServicePypi),  
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
