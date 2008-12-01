#!/usr/bin/env python
""" Delicious API
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import os
import sys
import base64
import time
import urllib2

# ASSUME THAT THE REQUIRED LIBS are available
# RELATIVE to this script => simplified install
levelsUp = 3
path = os.path.abspath( __file__ )
while levelsUp>0:
    path = os.path.dirname( path )
    levelsUp = levelsUp - 1    
sys.path.append( path )

import jld.api as api
import jld.api.delicious_objects as delObjects


# =================================================================            
# ================================================================= 


class Waiter(object):
    """ Serves as throttle to play nice with the terms of use.
    """
    def __init__(self):
        self.lastAccess = None
        
    def wait(self, secondsToWait = 1):
        #first time around... don't need to way :-)
        if (self.lastAccess is None):
            self.lastAccess = time.time()
            return
        
        now = time.time()
        diff = now = self.lastAccess 
        
        if (diff < secondsToWait):
            time.sleep( diff )
            
        self.lastAccess = time.time()
            
# =================================================================            
# ================================================================= 
        
        
class Api(object):
    """
    """
    _API = 'https://api.del.icio.us/v1/%s'
    
    def __init__(self, username, password):
        """
        """
        self.waiter = Waiter()
        self.username = username
        self.password = password
        self.auth = "Basic %s" % ( base64.encodestring("%s:%s" % (self.username, self.password)).strip() )
        
    def method_update(self):
        """ posts/update
        """
        query = "posts/update"
        rep = self._get(query)
        return rep
        
    def method_bundles_all(self):
        query = "tags/bundles/all"
        rep = self._get(query)
        return rep
    
    def method_bundle(self, name):
        query = "tags/bundles/all?bundle=%s" % name
        rep = self._get(query)
        return rep
        
    def do_method(self, query, **args):
        """ Generic method handler
        """

        
    def _get(self, query):
        """ All GET operations go through here
        """
        url = self._API % query

        # respect terms of use i.e. throttle
        self.waiter.wait()
        
        try:
            req = urllib2.Request(url)
            req.add_header('Authorization', self.auth)
            response = urllib2.urlopen(req)
        except Exception,e:
            raise api.ErrorNetwork(e) 
        return response.read()


# =================================================================            
# ================================================================= 



class Client(object):
    """ Higher level interface to Delicious
    """
    def __init__(self, username, password):
        self.api = Api(username, password)

    def getLastUpdate(self):
        """ Retrieves the time of the last update
            Method: https://api.del.icio.us/v1/posts/update
        """

    def getAllBundles(self):
        """ Retrieves all bundles
            Returns a list of bundles
            Method: https://api.del.icio.us/v1/tags/bundles/all
        """
        
    def getBundle(self, name):
        """ Returns a specific bundle
            Method: https://api.del.icio.us/v1/tags/bundles/all?bundle=NAME
        """
        
    def getAllTags(self):
        """ Retrieves all tags
            Method: https://api.del.icio.us/v1/tags/get
        """

    def getAllPosts(self, tag = None):
        """ Retrieves all posts
            Returns a list of posts
            Method: https://api.del.icio.us/v1/posts/all
        """ 

    def getPosts(self, tag = None, url = None, hash = None, dt = None):
        """ Retrieves a specific post
            Method: https://api.del.icio.us/v1/posts/get
        """

    def getRecentPosts(self, tag = None, count = 100):
        """ Retrieves the recent posts up to COUNT
            and filtered by TAG.
            Method: https://api.del.icio.us/v1/posts/recent
        """

    def getAllHashes(self):
        """ Retrieves the list of all hashes
            Method: https://api.del.icio.us/v1/posts/all?hashes
        """

# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    import os
    username = os.environ['DELICIOUS_USERNAME']
    password = os.environ['DELICIOUS_PASSWORD']
    d = Api(username, password)
    print d.method_update()
    
    print d.method_bundles_all()