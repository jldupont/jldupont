#!/usr/bin/env python
""" Delicious API
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import os
import sys
import base64
import datetime
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
        
    def wait(self):
        
        #first time around... don't need to way :-)
        if (self.lastAccess is None):
            self.lastAccess = datetime.datetime.now()
            return
        
        
# =================================================================            
# ================================================================= 
        
        
class Api(object):
    """
    """
    _API = 'https://api.del.icio.us/v1/%s'
    
    def __init__(self, username, password):
        """
        """
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


# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    d = Api('', '')
    print d.method_update()
    
    print d.method_bundles_all()