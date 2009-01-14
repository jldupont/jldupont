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

import libs.xmlrpc as gaexmlrpc
import libs.simplejson as json
import libs.markup as markup


class Service( webapp.RequestHandler ):
    """
    """
    def __init__(self):
        pass
    
    def _output(self, mime, code, content):
        self.response.headers["Content-Type"] = mime
        self.response.set_status(code)
        self.response.out.write(content);


class ServicePypi( Service ):
    """ Supported methods:
    """
    _methods = [ 'package_releases', 'release_urls', 'release_data' ]
    _formats = { 'json':'text/javascript' }
    
    _server = xmlrpclib.ServerProxy('http://pypi.python.org/pypi', gaexmlrpc.GAEXMLRPCTransport())
    
    def __init__(self):
        Service.__init__(self)
    
    def get( self, format, method, package_name, version = None ):
        if (format not in self._formats):
            self.response.out.write('unsupported format[%s]' % format);
            return
        
        if (method not in self._methods ):
            self.response.out.write('unsupported method[%s]' % method)
            return
        
        mime = self._formats[format]
        
        ip = self.request.remote_addr
        logging.info("ip[%s] method[%s] pkg[%s] version[%s]" % (ip, method, package_name, version))
        
        try:
            if version:
                raw = getattr(self, method)(package_name, version)
            else:
                raw = getattr(self, method)(package_name)
            
            res = json.dumps( raw )
            
        except Exception,e:
            logging.error( e )
            #self.response.out.write('map with id[%s] not found/available (or timeout occured)' % id);
            self.response.set_status(404)
            return
        
        self._output(mime, 200, res)

    def show_help(self):
        """
        """

    # =================================================
    # METHODS
    # =================================================

    def package_releases(self, pkg):
        """ Usage:  /services/pypi/[format]/package_releases/[package-name]
        """
        return self._server.package_releases(pkg,True)
    
    def release_urls(self, pkg, version):
        """ Usage:  /services/pypi/[format]/release_urls/[package-name]/[package-version]
        """        
        return self._server.release_urls(pkg, version)
    
    def release_data(self, pkg, version):
        """ Usage:  /services/pypi/[format]/release_data/[package-name]/[package-version]
        """        
        return self._server.release_data(pkg, version)


_urls = [ ('/services/pypi/(.*?)/(.*?)/(.*?)/(.*?)', ServicePypi),
          ('/services/pypi/(.*?)/(.*?)/(.*?)', ServicePypi)  
         ]                        
        
#/**
# *  Initialize http handler
# */
def main():
  application = webapp.WSGIApplication([('/services/pypi/(.*?)/(.*?)/(.*?)/(.*?)', ServicePypi)], debug=True)
  wsgiref.handlers.CGIHandler().run(application)

# Bootstrap
#  It all starts here
if __name__ == "__main__":
    main()
