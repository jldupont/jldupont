""" Backup for Gliffy diagrams
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

__msgs__ = ['error_init_folder', 'error_create_folder', 'frob_not_acquired', 'error_cant_write', ]

import sys
import os
import logging
import datetime
import urllib2
from stat import *

import jld.api as api
from   jld.cmd import BaseCmd
import jld.registry as reg
import jld.tools.mos as mos

import jld.api.gliffy as glf

import jld.backup.gliffy_messages as msg
import jld.backup.gliffy_printer as printer
import jld.backup.gliffy_db as db


# ========================================================================================

class Backup(BaseCmd):
    """Gliffy Backup class
    """
    _regDomain = 'gliffy'
    
    # configuration parameters expected from the Delicious command-line ui
    # used also by the Printer
    _configParams = ['export_path', 'export_maxnum', 'db_path']
    
    def __init__(self):
        BaseCmd.__init__(self)
        
        self.gliffy = None
        self.logger = None
        self.quiet = False
        self.db_path = None        
        self.db = None
        self.export_path = None
        self.export_maxnum = None
        
        self.msgs = msg.Gliffy_Messages()
        self.r = reg.Registry()

    # =========================================================
    # COMMANDS
    # =========================================================
        
    def cmd_listconfig(self, *args):
        """Lists the configuration"""
        pp = printer.Gliffy_Printer_Config( self.msgs, self )
        if (not self.quiet):
            pp.run( self )
    
    def cmd_updatedb(self, *args):
        """Updates the local database with the most recent entries"""
        remote = self._getRemoteUpdate()
        
        if (not self._shouldUpdate(remote)):
            msg = self.msgs.render('report_update_none')
            self.logger.info(msg)
            return
        
        posts = self.delicious.getRecentPosts()
        self._doUpdate(posts, remote, False)   #don't update Updates table, only the Posts table
    
    def cmd_listdb(self, *args):
        """ Lists the current entries in the database, optional filter by tag"""
        try:    tag = args[0]
        except: tag = None
        
        self._initDb()
        all = db.Posts.getAll(tag)
        
        pp = printer.Gliffy_Printer_Diagrams( self.msgs )
        if (not self.quiet):
            pp.run( all )
    
    def cmd_deletedb(self, *args):
        """Deletes the database"""
        self._deleteDb()
        
    # =========================================================
    # HELPERS
    # =========================================================
    def _doUpdate(self, list, remote, record_last = True):
        """ Performs an update cycle """
        total, updated, created = db.Posts.updateFromList( list )
        if (record_last):
            db.Updates.update( self.username, remote )
        if (not self.quiet):
            msg = self.msgs.render('report_updatedb', {'total':total, 'updated':updated, 'created':created } )
            self.logger.info(msg)
        
    def _deleteDb(self):
        path = mos.replaceHome( self.db_path )
        db.Db.deleteDb(path)
        
    # LAZY INITIALIZERS
    # =================

    def _initGliffy(self):
        if (self.gliffy is None):
            self.gliffy = glf.Client()

    def _initDb(self):
        if (self.db is None):
            path = mos.replaceHome( self.db_path )
            self.db = db.Db( path )
