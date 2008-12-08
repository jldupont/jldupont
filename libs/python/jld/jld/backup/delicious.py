#! /usr/bin/env python
""" Backup for Delicious bookmarks
    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import sys
import logging
import os.path
from types import *
from optparse import OptionParser

# ASSUME THAT THE REQUIRED LIBS are available
# RELATIVE to this script => simplified install
# TODO good for testing in dev environment,
#      bad for eggs...
levelsUp = 3
path = os.path.abspath( __file__ )
while levelsUp>0:
    path = os.path.dirname( path )
    levelsUp = levelsUp - 1    
sys.path.append( path )

import jld.api as api
import jld.registry as reg

from   jld.backup.delicious_backup import Backup
import jld.backup.delicious_messages as msg
import jld.backup.delicious_ui as dui
import jld.backup.delicious_defaults as ddef

from   jld.tools.template import ExTemplate
import jld.tools.logger as dlogger

# ========================================================================================
_options =[
  {'o1':'-s', 'var':'username',      'action':'store',        'help':'config_username', 'reg': True, 'default': None},
  {'o1':'-k', 'var':'password',      'action':'store',        'help':'config_password', 'reg': True, 'default': None},
   
  {'o1':'-f', 'var':'db_path',       'action':'store',        'help':'config_db_file',       'reg': True, 'default': None},
  {'o1':'-p', 'var':'export_path',   'action':'store',        'help':'config_export_path',   'reg': True, 'default': None},
  {'o1':'-m', 'var':'export_maxnum', 'action':'store',        'help':'config_export_maxnum', 'reg': True, 'default': None, 'type':'int'},
  
  {'o1':'-q', 'var':'quiet',         'action':'store_true',   'help':'quiet',         'reg': False, 'default': False },          
  {'o1':'-l', 'var':'syslog',        'action':'store_true',   'help':'syslog',        'reg': False, 'default': False },  
]

def main():
    
    msgs   = msg.Delicious_Messages()
    ui     = dui.Delicious_UI()
    
    # == Config UI ==
    # ===============
    ui.setParams( msgs )    
    
    # all the exceptions are handled by 'ui'
    try:
        backup = Backup()
        usage_template = """%prog [options] command
    
version $Id$ by Jean-Lou Dupont

*** Interface to Delicious (http://www.delicious.com/) ***

Usage:
 Step 1) Update local database: use the 'updatedb' command to retrieve/update the local database
 Step 2) Export: use the 'export' command to ...  

The commands which generate log entries are flagged with (logged) below.

Commands:
^^{commands}"""
            
        commands_help = backup.genCommandsHelp()
            
        tpl = ExTemplate( usage_template )
        usage = tpl.substitute( {'commands' : commands_help} )
    
        # Use OptParse to process arguments
        ui.handleArguments(usage, _options)
        
        # Configure ourselves a logger
        _quiet  = True  if ui.options.quiet  else False
        _syslog = False if ui.options.syslog else True        
        logger = dlogger.logger('delicious', include_console = _quiet, include_syslog = _syslog )

        backup.logger = logger
        ui.logger = logger

        # == configuration ==
        #
        # Process options from the command line:
        #  If an option is missing from the command line, look for it
        #  in the registry.Use conditional 'setKey' if we have valid 
        #  overriding values (i.e. not None) to update the registry.
        #  Finally, for missing parameters, look for defaults.
        #
        # PRECEDENCE:
        #  1) Command Line
        #  2) Registry
        #  3) Defaults
        # ===================
        r = reg.Registry('delicious')
        ui.updateRegistry(r, _options, ui.options)
        
        params = {}
        
        # integrate options which aren't subjected to the registry
        ui.integrateOptions(ui.options, params, _options)
        
        # integrate default config
        defs = ddef.Delicious_Defaults()
        ui.integrateDefaults(defs, r, _options, params)

        # Verify parameter type
        ui.verifyType(params, _options)
        
        # Configure Backup cmd object
        ui.copyOptions(params, backup, _options)
        
        # == command validation ==
        # ========================
        try: command = ui.args[0]
        except: command = None       
        backup.validateCommand(command)       
                 
        # get rid of command from the arg list
        ui.popArg()
        # == DISPATCHER ==
        # ================
        getattr( backup, "cmd_%s" % command )(ui.args)
        
    except Exception,e:
        ui.handleError( e )
        
    # === END ===

# =======================================================================

if __name__== "__main__":   
    main()
