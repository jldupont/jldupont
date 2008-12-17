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

import jld.backup.gliffy_db    as glfdb
import jld.backup.delicious_db as dlcdb


# ========================================================================================

class Backup(BaseCmd):
    """Gliffy Backup class
    """
    _regDomain = 'gliffy'
    
    # configuration parameters expected from the Delicious command-line ui
    # used also by the Printer
    _configParams = ['export_path', 'export_maxnum', 'glf_db_path', 'dlc_db_path']
    
    def __init__(self):
        BaseCmd.__init__(self)
        
        self.gliffy = None
        self.logger = None
        self.quiet = False
        self.dlc_db_path = None
        self.glf_db_path = None
        self.dlc_db = None        
        self.glf_db = None
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
    
    def cmd_listdb(self, *args):
        """ Lists the current entries in the database """
        self._initDb()
        all = glfdb.Diagrams.getAll()
        
        pp = printer.Gliffy_Printer_Diagrams( self.msgs )
        if (not self.quiet):
            pp.run( all )
            print 'Total[%s]' % len(all)
    
    def cmd_import(self, *args):
        """ Imports the diagram ids' from the Delicious database (logged) """
        try:    tag = args[0][0]
        except: raise api.ErrorValidation( 'missing_param', {'param':'tag'} )
        print tag
        self._initDb()
        all = dlcdb.Posts.getAll( tag )
        self._doImport(all)        
            
    def cmd_deletedb(self, *args):
        """Deletes the database"""
        self._deleteDb()
        
    # =========================================================
    # HELPERS
    # =========================================================
    def _extractHref(self,list):
        """ Extracts the URI from the HREF entries in the list
        """
        result = []
        list = list if list else []
        for item in list:
            result.append( item['href'] )
        return result
        
    def _doImport(self, list):
        """ Imports the diagram ids' from the list into the database
            @param list: diagram list 
        """
        try:    ids = self._extractHref(list)
        except: raise api.ErrorProtocol('msg:error_expecting_href')
            
        total, updated, created = glfdb.Diagrams.updateFromList(ids)
        msg = self.msgs.render('report_import', {'total':total, 'updated':updated, 'created':created })
        self.logger.info(msg)
    
    def _deleteDb(self):
        path = mos.replaceHome( self.glf_db_path )
        glfdb.Db.deleteDb(path)
        
    # LAZY INITIALIZERS
    # =================

    def _initGliffy(self):
        if (self.gliffy is None):
            self.gliffy = glf.Client()

    def _initDb(self):
        if (self.glf_db is None):
            glf_path = mos.replaceHome( self.glf_db_path )
            self.glf_db = glfdb.Db( glf_path )

        if (self.dlc_db is None):
            dlc_path = mos.replaceHome( self.dlc_db_path )
            self.dlc_db = dlcdb.Db( dlc_path )
