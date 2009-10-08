"""
 @author Jean-Lou Dupont
"""
import os
import sys
import logging
import wsgiref.handlers

from google.appengine.ext import webapp

class Demux( webapp.RequestHandler ):
    """
    Demultiplexes the request based on the sub-domain
    
    'www' being the default sub-domain
    """
    default="main"
    
    def get(self, page=None):
        """
        """
        host=self.request.environ["HTTP_HOST"]
        (subdomain,_sep, domain)=host.partition(".")
        response=self.dispatch(subdomain, page)
        self.response=response
        
    
    def dispatch(self, subdomain, page):
        """
        Tries to import the 'subdomain' handler
        and dispatch the request to it
        """    
        try:
            #logging.info("subdomain: %s" % subdomain)
            #print sys.path
            handler=__import__(subdomain, fromlist=["subdomains"])
            handler.main()
        except Exception,e:
            logging.error("subdomain not found: %s, Exception<%s>" % (subdomain, str(e)))
            return (None, 404)
        
        
            
        
#/**
# *  Initialize http handler
# */

_URLS = [   ('/(.*)', Demux),
         ]

### DO NOT MODIFY BELOW THIS LINE ###
### ----------------------------- ###

def main():
    root = os.path.split(__file__)[0]
    sys.path.insert(0, os.path.join(root, 'subdomains'))
    sys.path.insert(0, os.path.join(root, 'libs'))
    sys.path.insert(0, os.path.join(root, 'server'))

    host=os.environ["HTTP_HOST"]
    (subdomain,_sep, domain)=host.partition(".")
    try:
        #logging.info("subdomain: %s" % subdomain)
        #print sys.path
        handler=__import__(subdomain, fromlist=["subdomains"])
        return handler.main()
    except Exception,e:
        logging.error("subdomain not found: %s, Exception<%s>" % (subdomain, str(e)))
        return (None, 404)

if __name__ == "__main__":
    main()

