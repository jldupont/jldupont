"""
 @author Jean-Lou Dupont
"""
import os
import sys
import logging

import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.api import urlfetch

import libs.django.template as tpl

class Main( webapp.RequestHandler ):
    
    main_tpl = '/templates/main.html'
    
    def __init__(self):
        pass

    def get( self ):
        
        tpl_path = os.path.dirname( __file__ ) + self.main_tpl
        res = tpl.render( tpl_path, {} )
        logging.info( tpl_path )
        
        self.response.headers["Content-Type"] = "text/html"
        self.response.set_status(200)
        self.response.out.write( res );
        
#/**
# *  Initialize http handler
# */
def main():
  application = webapp.WSGIApplication([('/', Main)], debug=True)
  wsgiref.handlers.CGIHandler().run(application)

# Bootstrap
#  It all starts here
if __name__ == "__main__":
    main()
