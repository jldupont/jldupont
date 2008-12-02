#!/usr/bin/env python
""" Backup for MindMeister mindmaps

    Dependencies:
        module yaml   (available @ http://pyyaml.org/wiki/PyYAML)

"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import sys
import logging
import os.path
from optparse import OptionParser

# ASSUME THAT THE REQUIRED LIBS are available
# RELATIVE to this script => simplified install
levelsUp = 3
path = os.path.abspath( __file__ )
while levelsUp>0:
    path = os.path.dirname( path )
    levelsUp = levelsUp - 1    
sys.path.append( path )

import jld.api as api
import jld.registry as reg
from   jld.backup.mindmeister_backup import Backup
import jld.backup.mindmeister_messages as msg
import jld.backup.mindmeister_ui as mui
import jld.backup.mindmeister_defaults as mdef
from   jld.tools.template import ExTemplate

# ========================================================================================
_options =[
  {'o1':'-s', 'var':'secret',        'action':'store',        'help':'config_secret', 'reg': True, 'default': None},
  {'o1':'-k', 'var':'api_key',       'action':'store',        'help':'config_key',    'reg': True, 'default': None},
  {'o1':'-f', 'var':'db_path',       'action':'store',        'help':'config_file',   'reg': True, 'default': None},
  {'o1':'-p', 'var':'export_path',   'action':'store',        'help':'config_path',   'reg': True, 'default': None},
  {'o1':'-m', 'var':'export_maxnum', 'action':'store',        'help':'config_maxnum', 'reg': True, 'default': None},
  #{'o1':'-q', 'var':'quiet',  'action':'store_true',   'help':'quiet',        'reg': False, 'default': False },          
]

def main():

    msgs   = msg.MM_Messages()
    ui     = mui.MM_UI()
    
    # == Config UI ==
    # ===============
    ui.setParams( msgs )    
    
    # all the exceptions are handled by 'ui'
    try:
        backup = Backup()
        usage_template = """%prog [options] command
    
version $Id$ by Jean-Lou Dupont

*** Interface to MindMeister (http://www.mindmeister.com/) ***
This command-line utility requires valid 'API_KEY' and 'SECRET' parameters
obtained from MindMeister. In order to use this tool, the 'auth' command
must first be called with the said valid parameters.

The '-f' option is required for running 'mmd' daemon. This option configures
the local Sqlite database used for storing map related information. 

Commands:
^^{commands}"""
            
        commands_help = backup.genCommandsHelp()
            
        tpl = ExTemplate( usage_template )
        usage = tpl.substitute( {'commands' : commands_help} )
    
        ui.handleArguments(usage, _options)

        # == configuration ==
        # PRECEDENCE:
        #  1) Command Line
        #  2) Registry
        #  3) Defaults
        # ===================

        # Process options from the command line:
        #  If an option is missing from the command line, look for it
        #  in the registry.Use conditional 'setKey' if we have valid 
        #  overriding values (i.e. not None) to update the registry.
        #  Finally, for missing parameters, look for defaults.
        r = reg.Registry()
        for o in _options:
            if ( o['reg'] ): 
                r.setKey('mindmeister', o['var'], getattr( ui.options, o['var'] ), cond=True)

        params = {}
            
        # integrate default config
        defs = mdef.MM_Defaults()
        for o in _options:
            key = o['var']
            val = r.getKey('mindmeister', key)
            if val is None:
                val = defs.defaults[key] if (key in defs.defaults) else None
            params[key] = val
        
        # Configure Backup cmd object
        for o in _options:
            key = o['var']
            val = params[key]
            setattr( backup, key, val )
        
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
