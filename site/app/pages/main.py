"""
 @author Jean-Lou Dupont
"""
import os
import sys
import logging

import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.api import urlfetch

import libs.django as mydjango

# My Django configuration
# =======================
_loaders = (    'libs.django.filesystem_template_loader.load_template_source',
                'libs.django.url_template_loader.load_template_source',
                )
_dir = os.path.dirname( __file__ ) + os.sep + 'templates'
_dirs = ( _dir, )
_urls = ( "http://jldupont.googlecode.com/svn/trunk/site/templates/%s", )

mydjango.setConfig( 'TEMPLATE_LOADERS', _loaders )
mydjango.setConfig( 'TEMPLATE_DIRS', _dirs )
mydjango.setConfig( 'TEMPLATE_URL_BASES', _urls )

# === GLOBAL VARS ===
# ===================
IS_REMOTE = not os.environ.get('SERVER_SOFTWARE').startswith('Dev')

class Main( webapp.RequestHandler ):
    
    _base_tpl = 'base.html'
    
    def __init__(self):
        pass

    def get( self, page = None ):
        user = users.get_current_user()
        logx_href  = users.create_logout_url("/") if user else users.create_login_url("/")
        logx_title = "Logout" if user else "Login"
        params = { 'content':'some content',
                   'logx_href':  logx_href,
                   'logx_title': logx_title,
                   'is_remote':IS_REMOTE
                  }
        res = mydjango.render( self._base_tpl, params )
        
        self.response.headers["Content-Type"] = "text/html"
        self.response.set_status(200)
        self.response.out.write( res );
        
    def getPage(self, page):
        """ Retrieves and renders the specified page
        """
        
#/**
# *  Initialize http handler
# */

_URLS = [   ('/', Main),
            ('/page/(.*)', Main),
         ]

def main():
  application = webapp.WSGIApplication(_URLS, debug=True)
  wsgiref.handlers.CGIHandler().run(application)

# Bootstrap
#  It all starts here
if __name__ == "__main__":
    main()
