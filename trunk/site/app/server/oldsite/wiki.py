"""
 @author Jean-Lou Dupont
"""
import os
import sys
import logging

import wsgiref.handlers
import xml.dom.minidom
import time
from time import strftime, strptime

from google.appengine.ext           import webapp
from google.appengine.ext.webapp    import template
from google.appengine.api           import urlfetch

import pprint

class WikiSite( webapp.RequestHandler ):
    
    def __init__(self):
        pass

    def get( self, feed_id ):
        
        self.redirect("http://wiki.jldupont.com")

#/**
# *  Initialize http handler
# */
def main():
  application = webapp.WSGIApplication([('/(.*?)/', WikiSite)], debug=True)
  wsgiref.handlers.CGIHandler().run(application)

# Bootstrap
#  It all starts here
if __name__ == "__main__":
    main()