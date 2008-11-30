""" Backup for MindMeister mindmaps
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"
__msgs__ = ['error_init_folder', 'error_create_folder', 'frob_not_acquired', '', ]

import sys
import os
import logging
import webbrowser
import datetime
from stat import *

import jld.api as api
from   jld.cmd import BaseCmd
import jld.registry as reg
import jld.api.mindmeister as mm
import jld.api.mindmeister_response as mmr
import jld.backup.mindmeister_messages as msg
import jld.backup.mindmeister_printer as printer
import jld.backup.mindmeister_db as db
import jld.tools.mos as mos

# ========================================================================================

class Backup(BaseCmd):
    """MindMeister Backup class
    """
    _regDomain = 'mindmeister'
    
    def __init__(self):
        BaseCmd.__init__(self)
        self.secret = None
        self.api_key = None
        self.auth_token = None
        self.export_path_init = None
        self.export_path = None
        self.export_maxnum = None
        self.mm = None
        self.file = None        
        self.db = None
        
        self.msgs = msg.MM_Messages()
        self.r = reg.Registry()
        
    
    def cmd_auth(self, *args):
        """Generates an authentication URL and opens a browser instance for the user"""
        #get a new 'frob'
        self._initMM()
        raw = self.mm.do(method='mm.auth.getFrob')
        res = mmr.MM_Response_getFrob(raw)
        
        #keep this frob in order to retrieve an authentication token later on
        self.r.setKey(self._regDomain, 'frob', res.frob, cond = True)
        
        url = self.mm.gen_auth_url('read', res.frob)
        webbrowser.open_new(url)
            
    def cmd_umaps(self, *args):
        """ Updates the local database with the latest list of maps """
        self._prepareAuthorizedCommand()
        all = self.mm.getAllMaps()
        
        self._initDb()
        db.Maps.updateFromList( all )
        
    def cmd_listmaps(self, *args):
        """ List the latest maps """
        self._prepareAuthorizedCommand()
        all = self.mm.getAllMaps()
        pp = printer.MM_Printer_Maps( self.msgs )
        pp.run( all )
        
    def cmd_listdb(self, *args):
        """List the database content"""
        self._initDb()
        all = db.Maps.getAll()
        pp = printer.MM_Printer_Maps( self.msgs )
        pp.run( all )        
        
    def cmd_test(self, *args):
        """Test: for development/debugging purpose only"""
        self._initDb()

    def cmd_getexport(self, *args):
        """List the export details of one mapid"""
        try:
            mapid=args[0][0]
        except:
            raise api.ErrorValidation( 'missing_param', {'param':'mapid'} )
        self._prepareAuthorizedCommand()      
        details = self.mm.getMapExport(mapid)
        pp = printer.MM_Printer_Export( self.msgs )       
        pp.run( details )

    def cmd_exportlist(self, *args):
        """Lists the complete export list
        """
        self._initDb()
        full_list = db.Maps.getExportList()
        pp = printer.MM_Printer_Maps( self.msgs )
        pp.run( full_list )
        
    def cmd_export(self, *args):
        """Export (retrieves from MindMeister) up to 'maxnum' mindmaps which need refreshing.
        """
        self._initDb()
        full_list = db.Maps.getToExportList()

        self._init_export_folder()
        
        cnt = self.export_maxnum
        print cnt
        while cnt > 0:
            item = full_list.pop(0) if len(full_list) else None
            if item is None:
                break
            cnt = cnt - 1
        
    # =========================================================
    # =========================================================
    def _init_export_folder(self):
        """ Creates the export folder IF it does not
            already exists
        """
        if (not self.export_path_init):
            self.export_path_init = mos.replaceHome( self.export_path )

        rep = mos.existsDir(self.export_path_init)
        if (rep):
            return
               
        if (rep is False):
            self._create_export_folder()
                    
        rep = mos.existsDir(self.export_path_init)       
        if (rep is False):
            raise api.ErrorConfig('msg:error_init_folder')            
            
    def _create_export_folder(self):
        """ Creates the export folder
        """
        try:    
            os.makedirs(self.export_path_init)
        except: 
            print 'os.makedirs'
            raise api.ErrorConfig('msg:error_create_folder')
        return  True
            
    # =========================================================
    # =========================================================
    
    def _prepareAuthorizedCommand(self):
        """Prepares for an authorized command.
            Existing auth_token in registry
                1a) valid?  then proceed
                1b) else: remove frob & token from registry
            Existing frob?
                2b) try to get a token
                    inform user to auth
        """
        self._initMM()
        auth_token = self.r.getKey(self._regDomain, 'auth_token')
        
        #If there is no auth_token,
        # check for an existing frob and try to retrieve a token
        if (auth_token is None):
            frob = self.r.getKey(self._regDomain, 'frob')
            if (frob is None):
                raise api.ErrorAuth("msg:frob_not_acquired")
            auth_token = self._getAuthToken(frob)
        
        # token turns out to be invalid, help kickstart a re-authentication
        if (not self.mm.checkToken(auth_token)):   
            self.r.setKey(self._regDomain, 'auth_token', None)
            self.r.setKey(self._regDomain, 'frob', None)
            return

        self.mm.auth_token = auth_token
        
    def _getAuthToken(self, frob = None):
        """ Retrieves an authentication token.
            This method can only provide meaningful result
            when valid secret, api_key and frob are handy.
        """
        self._initMM()

        if (frob is None):
            frob = self.r.getKey(self._regDomain, 'frob')
        raw = self.mm.do(method='mm.auth.getToken', frob=frob)
        res = mmr.MM_Response_getAuthToken(raw)
           
        self.r.setKey(self._regDomain, 'auth_token', res.auth_token)
        
        return res.auth_token
        
    # LAZY INITIALIZERS
    # =================

    def _initMM(self):
        if (self.mm is None):
            self.mm = mm.MM_Client(self.secret, self.api_key)

    def _initDb(self):
        if (self.db is None):
            self.db = db.Db( self.file )
