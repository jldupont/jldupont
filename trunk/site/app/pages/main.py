"""
 @author Jean-Lou Dupont
"""
import os
import sys
import logging

import wsgiref.handlers
from google.appengine.api import users
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
        user = users.get_current_user()
        logx_href  = users.create_logout_url("/") if user else users.create_login_url("/")
        logx_title = "Logout" if user else "Login"
        params = { 'content':'some content',
                   'logx_href':  logx_href,
                   'logx_title': logx_title,
                  }
        res = mydjango.render( self._base_tpl, params )
        
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
