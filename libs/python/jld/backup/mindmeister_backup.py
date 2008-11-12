""" Backup for MindMeister mindmaps
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"
import sys
import os.path
import logging
import webbrowser

import jld.registry as reg
import jld.api.mindmeister as mm
import jld.api.mindmeister_response as mmr
from jld.cmd import BaseCmd
import jld.backup.mindmeister_messages as msg

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
        self.msgs = msg.MM_Messages()
    
    def cmd_auth(self, *args):
        """Generates an authentication URL and opens a browser instance for the user"""
        #get a new 'frob'
        self._initMM()
        raw = self.mm.do(method='mm.auth.getFrob')
        res = mmr.MM_Response_getFrob(raw)
        
        #keep this frob in order to retrieve an authentication token later on
        r = reg.Registry()
        try:    
            r.setKey('mindmeister', 'frob', res.frob, cond = True)
        except Exception,e: 
            logging.error( self.msgs.render('reg_update_error') )
            sys.exit(0)
        
        url = self.mm.gen_auth_url('read', res.frob)
        webbrowser.open_new(url)
            
    def cmd_export_all(self, *args):
        """Exports all the maps"""
        print "in export_all command"
        print args

    def cmd_listmaps(self, *args):
        """Lists all the maps"""
        token = self._getAuthToken()
        if (token is None):
            print self.msgs.render('do_auth')
            sys.exit(0)
        
        all = self._getAllMaps(token)
        print all
        
    # =========================================================
    # =========================================================
    def _getAllMaps(self, auth_token):
        """ Retrieves all maps
        """
        run = True
        per_page = 100;  pages = 0
        total = 0;  count = 0;  page = 1;  maps = []
        while run:
            batch = self._getOnePage(auth_token, page, per_page)
            maps.append( batch.maps )
            pages = int( batch.pages )
            count = count + int( batch.count )
            total = int( batch.total )
            page = page + 1
            #print "total [%s]  count[%s] pages[%s]" % (total, count, pages)
            if (count>=total):
                run = False
                
        return maps
        
    def _getOnePage(self, auth_token, page, per_page):
        """Retrieves one page of the map list"""
        self._initMM()
        raw = self.mm.do(method='mm.maps.getList', auth_token = auth_token, page = page, per_page = per_page)
        res = mmr.MM_Response_getList(raw)
        return res
        
        
    def _getAuthToken(self):
        """ Retrieves an authentication token.
            This method can only provide meaningful result
            when valid secret, api_key and frob are handy.
        """
        self._initMM()
        r = reg.Registry()
        frob = r.getKey('mindmeister', 'frob')
        raw = self.mm.do(method='mm.auth.getToken', frob=frob)
        res = mmr.MM_Response_getAuthToken(raw)
        return res.auth_token
        

    def _initMM(self):
        if (self.mm is None):
            self.mm = mm.MM(self.secret, self.api_key)
