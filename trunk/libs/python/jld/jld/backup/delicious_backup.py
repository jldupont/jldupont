""" Backup for Delicious bookmarks
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

__msgs__ = ['error_init_folder', 'error_create_folder', 'frob_not_acquired', 'error_cant_write', ]

import sys
import os
import logging
import webbrowser
import datetime
import urllib2
from stat import *

import jld.api as api
from   jld.cmd import BaseCmd
import jld.registry as reg
import jld.tools.mos as mos

import jld.api.delicious as dlc
import jld.api.delicious_objects as dlco

import jld.backup.delicious_messages as msg
import jld.backup.delicious_printer as printer
import jld.backup.delicious_db as db


# ========================================================================================

class Backup(BaseCmd):
    """Delicious Backup class
    """
    _regDomain = 'delicious'
    
    # configuration parameters expected from the Delicious command-line ui
    # used also by the Printer
    _configParams = ['username', 'password', 'db_path' ] #'export_path', 'export_maxnum', 'db_path']
    
    def __init__(self):
        BaseCmd.__init__(self)
        
        self.delicious = None
        self.logger = None
        self.quiet = False
        self.db_path = None        
        self.db = None
        self.username = None
        self.password = None
        
        self.msgs = msg.Delicious_Messages()
        self.r = reg.Registry()

    # =========================================================
    # Iteration & Dict access interfaces
    #  Used for the command ''listconfig''
    # =========================================================
    def __contains__(self, key):
        return key in self._configParams
    
    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem(self, key, value):
        setattr(self, key, value)
    
    def __iter__(self):
        self.iter = True
        return self
    
    def next(self):
        if (self.iter):
            self.iter = False
            return self
        else:
            raise StopIteration
    
    # =========================================================
    # =========================================================
        
    def cmd_listconfig(self, *args):
        """Lists the configuration"""
        pp = printer.Delicious_Printer_Config( self.msgs, self )
        if (not self.quiet):
            pp.run( self )
    
    def cmd_updatedb(self, *args):
        """Updates the local database with the most recent information"""
        self._validateAuthParams()
        self._initDelicious()
        
        lastUpdate = self.delicious.getLastUpdate()
        print lastUpdate
    
    def cmd_deletedb(self, *args):
        """Deletes the database"""
        self._deleteDb()
        
    # =========================================================
    # =========================================================
    def _validateAuthParams(self):
        """ Performs basic validation of the authentication parameters """
        
        if (not self.username):
            raise api.ErrorConfig('', {'param':'username'})
        
        if (not self.password):
            raise api.ErrorConfig('', {'param':'password'})
        
    
    # =========================================================
    # =========================================================

    def _deleteDb(self):
        path = mos.replaceHome( self.db_path )
        db.Db.deleteDb(path)
        
    # LAZY INITIALIZERS
    # =================

    def _initDelicious(self):
        if (self.delicious is None):
            self.delicious = dlc.Client(self.username, self.password)

    def _initDb(self):
        if (self.db is None):
            path = mos.replaceHome( self.db_path )
            self.db = db.Db( path )

