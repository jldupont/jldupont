"""
 @author Jean-Lou Dupont
"""
import os
import sys
import logging

import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.api import urlfetch

import xmlrpclib

class Service( webapp.RequestHandler ):
    """
    """
    def _output(self, mime, code, content):
        self.response.headers["Content-Type"] = mime
        self.response.set_status(code)
        self.response.out.write(content);
        

import libs.xmlrpc as gaexmlrpc

class ServicePypi( Service ):
    
    _methods = [ 'package_releases', 'release_urls', 'release_data' ]
    _formats = { 'json':'text/javascript' }
    
    _server = xmlrpclib.ServerProxy('http://pypi.python.org/pypi', gaexmlrpc.GAEXMLRPCTransport())
    
    def get( self, format, method, package_name, version = None ):
        if (format not in self._formats):
            self.response.out.write('unsupported format[%s]' % format);
            return
        
        if (method not in self._methods ):
            self.response.out.write('unsupported method[%s]' % method)
            return
        
        mime = self._formats[format]
        
        logging.info("method[%s] pkg[%s] version[%s]" % (method, package_name, version))
        
        #try:
        if True:
            if version:
                res = getattr(self, method)(package_name, version)
            else:
                res = getattr(self, method)(package_name)
                
        #except Exception,e:
        """
            logging.error( e )
            #self.response.out.write('map with id[%s] not found/available (or timeout occured)' % id);
            self.response.set_status(404)
            return
        """
        
        ip = self.request.remote_addr
        logging.info('ip[%s] mm format[%s] id[%s]' % (ip, format, id))
        
        self._output(mime, 200, res)

    def package_releases(self, pkg):
        return self._server.package_releases(pkg,True)
    
    def release_urls(self, pkg, version):
        return self._server.release_urls(pkg, version)
    
    def release_data(self, pkg, version):
        return self._server(pkg, version)


_urls = [ ('/services/pypi/(.*?)/(.*?)/(.*?)/(.*?)', ServicePypi),
          ('/services/pypi/(.*?)/(.*?)/(.*?)', ServicePypi)  
         ]                        
        
#/**
# *  Initialize http handler
# */
def main():
  application = webapp.WSGIApplication([('/services/pypi/(.*?)/(.*?)/(.*?)', ServicePypi)], debug=True)
  wsgiref.handlers.CGIHandler().run(application)

# Bootstrap
#  It all starts here
if __name__ == "__main__":
    main()
