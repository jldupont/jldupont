"""
 @author Jean-Lou Dupont
"""
import os
import sys
import logging
import logging

import wsgiref.handlers
from google.appengine.ext import webapp

class WikiSite( webapp.RequestHandler ):
    
    def __init__(self):
        pass

    def get( self, page ):
        logging.info('Redirecting: page requested: ' + page )
        self.redirect("http://wiki.jldupont.com/" + page )

#/**
# *  Initialize http handler
# */
def main():
  application = webapp.WSGIApplication([('/(.*?)', WikiSite)], debug=True)
  wsgiref.handlers.CGIHandler().run(application)

# Bootstrap
#  It all starts here
if __name__ == "__main__":
    main()