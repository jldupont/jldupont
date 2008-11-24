"""
 @author Jean-Lou Dupont
"""
import os
import sys
import logging

import wsgiref.handlers
from google.appengine.api import urlfetch

import libs.django as mydjango

_loaders = (    'libs.django.filesystem_template_loader.load_template_source',
                )
_dir = os.path.dirname( __file__ ) + os.sep + 'templates'
_dirs = ( _dir, )

mydjango.setLoaders( _loaders )
mydjango.setDirs( _dirs )

from google.appengine.ext import webapp

class Main( webapp.RequestHandler ):
    
    _base_tpl = 'base.html'
    
    def __init__(self):
        pass

    def get( self ):
        
        res = mydjango.render( self._base_tpl, {'content':'some content here'} )
        
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
