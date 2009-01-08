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
from google.appengine.api import memcache

import libs.cache  as cache
import libs.django as mydjango

#path setup for libs.
import import_wrapper

# restructuredText
import libs.markup as markup

# My Django configuration
# =======================
_loaders = (    'libs.django.filesystem_template_loader.load_template_source',
                'libs.django.url_template_loader.load_template_source',
                )
_thisPath = os.path.dirname( __file__ )
_dirTpl   = os.path.join( _thisPath, 'templates' ) 
_dirSite  = os.path.join( _thisPath, 'site' )      

_dirs = ( _dirSite, 
          _dirTpl, 
        )
_urls = ( "http://jldupont.googlecode.com/svn/trunk/site/app/pages/site/%s", 
          "http://jldupont.googlecode.com/svn/trunk/site/app/pages/templates/%s",
        )
_extensions = ['.html',]

mydjango.setConfig( 'TEMPLATE_URL_BASES', _urls ) #not django standard
mydjango.setConfig( 'TEMPLATE_ALLOWED_EXTENSIONS', _extensions ) #not django standard
mydjango.setConfig( 'TEMPLATE_LOADERS', _loaders )
mydjango.setConfig( 'TEMPLATE_DIRS', _dirs )
mydjango.setConfig( 'INSTALLED_APPS', ('django.contrib.markup',) )

# === GLOBAL VARS ===
# ===================
IS_REMOTE = not os.environ.get('SERVER_SOFTWARE').startswith('Dev')

class Base( webapp.RequestHandler ):
    """
    """
    _MAX_AGE  = "600"
    _base_tpl = 'base.html'
    
    _page_error = 'main'
    _page_main  = 'main'
    
    def _dolog(self, page):
        ua = self.request.headers['User-Agent']
        ip = self.request.remote_addr
        logging.info('ip[%s] page[%s] ua[%s]' %(ip,page,ua))

    def _getlogx(self):
        user = users.get_current_user()
        logx_href  = users.create_logout_url("/") if user else users.create_login_url("/")
        logx_title = "Logout" if user else "Login"
        return (logx_href, logx_title)

    def getPage(self, page, params = None):
        """ Retrieves and renders the specified page
        """
        try:
            page = mydjango.render( page, params )
            return (page,200)
        except:
            try:
                page = mydjango.render( 'not_found.html' , params )
                return (page,404)                
            except:
                logging.error('Default page "not_found.html" error')
        return (None,500)

    def _output(self, content, code):
        """
        """
        if (code == 200):
            self.response.headers["Cache-Control"] = self._MAX_AGE
            self.response.out.write( content );
            
        self.response.headers["Content-Type"] = "text/html"
        self.response.set_status( code )

    def _output_page(self, page):
        if (page is None):
            page = 'main'        
        
        self._dolog(page)

        content,code = self.getPage(page, {'page': page} )

        self._render_content(content, code)
                        
    def _render_content(self, content, code):
        
        (logx_href, logx_title) = self._getlogx()        
        params = { 'content':    content,
                   'logx_href':  logx_href,
                   'logx_title': logx_title,
                   'is_remote':  IS_REMOTE
                  }
        
        res = mydjango.render( self._base_tpl, params )       
        self._output(res, code)
        
        

class Main( Base ):
    """ Default handler for the url fragement /page/
    """
    def __init__(self):
        Base.__init__(self)

    def get( self, page = None ):
        self._output_page(page)

                
class Doc( Base ):
    """ ReSTructuredTEXT page handler
    """
    def __init__(self):
        Base.__init__(self)
        
    def get(self, base_name = None):
        
        page = base_name + '.rst'
        
        try:
            content = markup.getReSText(_dirs, page)
            self._render_content(content, 200)
        except Warning, w:
            logging.warn("Doc: [%s]" % w)
            self._output_page( self._page_error )
            return            
        except Exception,e:
            logging.error("Doc: [%s]" % e)
            self._output_page( self._page_error )
            return

        
        
        
#/**
# *  Initialize http handler
# */

_URLS = [   ('/', Main),
            ('/page/(.*)', Main),
            ('/doc/(.*)',  Doc),
         ]

def main():
  application = webapp.WSGIApplication(_URLS, debug=True)
  wsgiref.handlers.CGIHandler().run(application)

# Bootstrap
#  It all starts here
if __name__ == "__main__":
    main()
