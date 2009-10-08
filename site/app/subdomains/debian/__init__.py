# @author: Jean-Lou Dupont

import os
import sys
import logging
import wsgiref.handlers

from google.appengine.ext import webapp

__all__=["main"]


class Debian( webapp.RequestHandler ):
    
    def get(self, page=None):
        logging.info("debian: page: %s" % page)
        
        #self.response.headers["Content-Type"] = "text/html"
        #self.response.set_status( 200 )
        #self.response.out.write("")
        return self.response
    

#/**
# *  Initialize http handler
# */

_URLS = [   ('/(.*)', Debian),
         ]

def main():
    application = webapp.WSGIApplication(_URLS, debug=False)
    wsgiref.handlers.CGIHandler().run(application)

# Bootstrap
#  It all starts here
if __name__ == "__main__":
    main()

