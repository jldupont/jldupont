""" Backup for MindMeister mindmaps
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"
import sys
import os.path
import logging
import webbrowser

try:
    import jld.registry as reg
    import jld.api.mindmeister as mm
    from jld.cmd import BaseCmd
except Exception,e:
    #directory levels to reach libs folder
    levelsUp = 3
    path = os.path.abspath( __file__ )
    while levelsUp>0:
        path = os.path.dirname( path )
        levelsUp = levelsUp - 1    
    sys.path.append( path )
    import jld.registry as reg
    import jld.api.mindmeister as mm
    from jld.cmd import BaseCmd    

# ========================================================================================

class Backup(BaseCmd):
    """MindMeister Backup class
    """
    def __init__(self):
        BaseCmd.__init__(self)
        self.secret = None
        self.api_key = None
        self.auth_token = None
        self.mm = None
    
    def cmd_auth(self, *args):
        """Generates an authentication URL and opens a browser instance for the user"""
        #get a new 'frob'
        self._initMM()
        raw = self.mm.do(method='mm.auth.getFrob')
        res = mm.MM_Response_getFrob(raw)
        
        #keep this frob in order to retrieve an authentication token later on
        r = reg.Registry()
        try:    
            r.setKey('mindmeister', 'frob', res.frob, cond = True)
        except Exception,e: 
            logging.error("AUTH: unable to update registry")
            sys.exit(0)
        
        url = self.mm.gen_auth_url('read', res.frob)
        webbrowser.open_new(url)
            
    def cmd_export_all(self, *args):
        """Exports all the maps"""
        print "in export_all command"
        print args


    def _initMM(self):
        if (self.mm is None):
            self.mm = mm.MM(self.secret, self.api_key)
