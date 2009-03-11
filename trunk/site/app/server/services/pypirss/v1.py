"""
    Service Pypi RSS
    
    @author Jean-Lou Dupont
    
    Conditions to account for:
    ==========================
    * network error
    * Pypi RPC error
    * package not found
    * package with no releases
    * package with no release X
    * Pypi RPC API change eg. the 'downloads' attribute is not found
    * Wrong format requested
    * ALL OTHERS
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
import libs.system as system
from libs.system.datetimeutils import datetimeToRFC822

import services.pypirss.rss as feed
import services.pypirss.messages as msg

class ServiceMessageOutput(object):
    """ Wrapper used along with Exception Handler
    """
    def __init__(self, msg_output, code_output, code=500):
        self.code = code
        self.msg_output = msg_output
        self.code_output = code_output
        
    def out(self, msg):
        self.msg_output(msg)
        
    def after_out(self):
        """ Called after the 'out' method has been used.
        """
        self.code_output(self.code)


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
    
    _feedTemplate = feed.prepareFeedTemplate()
    
    
    
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

    def method_rss(self, package):
        """\
        **Usage**:  /services/pypirss/rss/[package-name]
        """
        try:
            latest, downloads, last_update = proxy.getLatestDownloads(package)           
        except Exception,e:
            self._handleException(e)
            return

        itemGUID = "%s-%s-%downloads" % (package, latest, downloads)
        pubDate = datetimeToRFC822(last_update)

        params = {'package':package, 
                  'release':latest, 
                  'downloads':downloads,
                  'itemPubDate': pubDate,
                  'itemGUID': itemGUID
                  }
        res = self._feedTemplate.produce(params, [params])       
        return res


    # =================================================
    # HANDLERS
    # =================================================
    def _handleException(self, exc):
        msgOutput = ServiceMessageOutput(self.response.out.write, 
                                              self.response.set_status)
        
        #setup an exception handler... just in case
        excHandler = system.ExceptionHandler(msg.messages, 
                                             msg.message_template, 
                                             output=msgOutput)
        
        excHandler.handleException(exc)
      

_urls = [ 
          ('/services/pypirss/(.*?)/(.*?)', ServicePypiRss),
          ('/services/pypirss/(.*?)',       ServicePypiRss),  
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
