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
    
    # configuration parameters expected from the coDeliciousand-line ui
    _configParams = ['username', 'password', 'export_path', 'export_maxnum', 'db_path']
    
    def __init__(self):
        BaseCmd.__init__(self)
        self.logger = None
        self.quiet = False
        self.export_path_init = None
        self.export_path = None
        self.export_maxnum = None
        self.db_path = None        
        self.db = None
        
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
        """ Updates the local database (logged) """
        all = self.mm.getAllMaps()
        
        self._initDb()
        report = db.Maps.updateFromList( all )
        msg=self.msgs.render('report_update', {'total':report[0],'updated': report[1], 'new': report[2]})
        self.logger.info( msg )
        
    def cmd_listdb(self, *args):
        """List the database content"""
        self._initDb()
        all = db.Maps.getAll()
        pp = printer.MM_Printer_Maps( self.msgs )
        if (not self.quiet):
            pp.run( all )   
            print self.msgs.render('report_maps', {'total':len(all)})     
        
    def cmd_exportlist(self, *args):
        """Lists the complete export list"""
        self._initDb()
        full_list = db.Maps.getExportList()
        pp = printer.MM_Printer_Maps( self.msgs )
        if (not self.quiet):
            pp.run( full_list )
        
    def cmd_export(self, *args):
        """Export (retrieves from MindMeister) up to 'export_maxnum' mindmaps which need refreshing (logged) """
        self._initDb()
        full_list = db.Maps.getToExportList()

        self._init_export_folder()
        
        cnt = self.export_maxnum
        self._prepareAuthorizedCommand()
        stack_result = []
        success = 0
        failure = 0
        total = 0
        for map in full_list:
            self.logger.info('Exporting title[%s] mapid[%s]' % (map.title, map.mapid))
            #SqlObject SelectResults has no 'len' method...
            total = total + 1
            ts = datetime.datetime.now()
            timestamp = "%s%s%s%s%s%s" % (ts.year, ts.month, ts.day, ts.hour, ts.minute, ts.second)                            
            res = self._exportOne( map.mapid, ts, timestamp )

            if (res is True):
                success = success + 1
                self._updateDbOne( map )
            else:
                failure = failure + 1
            
            # record result
            stack_result.append((map.mapid, res))
            
            cnt = cnt - 1
            if (cnt==0):
                break
                
        msg = self.msgs.render('report_export', {'total': total, 'successes': success, 'failures': failure} )
        self.logger.info(msg)
                 
    def cmd_deletedb(self, *args):
        """Deletes the database"""
        self._deleteDb()
        
    # =========================================================
    # =========================================================

    def _updateDbOne(self, map ):
        """ Updates the database
        """
        try:
            map.exported = map.modified
        except Exception,e:
            raise api.ErrorDb('msg:error_update_db',{})
        
    # =========================================================
    # =========================================================
    def _create_map_export_folder(self, dir):
        """
        """
        mos.createDirIfNotExists(dir)
    
    
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
    def _deleteDb(self):
        path = mos.replaceHome( self.db_path )
        db.Db.deleteDb(path)
        
    # LAZY INITIALIZERS
    # =================

    def _initMM(self):
        if (self.mm is None):
            self.mm = mm.MM_Client(self.secret, self.api_key)

    def _initDb(self):
        if (self.db is None):
            path = mos.replaceHome( self.db_path )
            self.db = db.Db( path )

