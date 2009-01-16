#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import sys
import logging
import os.path
from types import *
from optparse import OptionParser

from jld.tools.ytools import Yattr, Ymsg 

# ========================================================================================
_options =[
  {'o1':'-s', 'var':'server',        'action':'store',        'help':'config_server',  'reg': True, 'default': None},
  {'o1':'-p', 'var':'port',          'action':'store',        'help':'config_port',    'reg': True, 'default': None}, 
]

def main():
    
    msgs     = Ymsg(__file__)
    defaults = Yattr(__file__)
    
    ui     = mui.MM_UI()
    
    # == Config UI ==
    # ===============
    ui.setParams( msgs )    
    
    # all the exceptions are handled by 'ui'
    try:
        backup = Backup()
        usage_template = """%prog [options] command
    
version $Id$ by Jean-Lou Dupont

*** Interface to Transmission (Bittorent client) ***

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
        logger = mlogger.logger('mm', include_console = _quiet, include_syslog = _syslog )

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
        r = reg.Registry('mindmeister')
        ui.updateRegistry(r, _options, ui.options)
        
        params = {}
        
        # integrate options which aren't subjected to the registry
        ui.integrateOptions(ui.options, params, _options)
        
        # integrate default config
        defs = mdef.MM_Defaults()
        ui.integrateDefaults(defs, r, _options, params)

        # Verify parameter type
        ui.verifyType(params, _options)
        
        # Configure Backup cmd object
        ui.copyOptions(params, backup, _options)
        
        # == command validation ==
        # ========================
        try: command = ui.args[0]
        except: command = None
        
        if command is None:
            sys.exit(0)
               
        backup.validateCommand(command)       
                 
        # get rid of command from the arg list
        ui.popArg()
        
        # == DISPATCHER ==
        # ================
        getattr( backup, "cmd_%s" % command )(ui.args)
        
    except Exception,e:
        ui.handleError( e )
        sys.exit(1)
        
    sys.exit(0)
    # === END ===

# =======================================================================

if __name__== "__main__":   
    main()
