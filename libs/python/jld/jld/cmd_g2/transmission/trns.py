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

import jld.registry as reg
from jld.tools.ytools import Yattr, Ymsg
from jld.cmd_g2.base_ui import BaseCmdUI 
from   jld.tools.template import ExTemplate
import jld.tools.logger as _logger
from cmd import TransmissionCmd


# ========================================================================================
_options =[
  {'o1':'-s', 'var':'config_server', 'action':'store',        'help':'config_server',  'reg': True, 'default': None},
  {'o1':'-p', 'var':'config_port',   'action':'store',        'help':'config_port',    'reg': True, 'default': None},
  {'o1':'-q', 'var':'config_quiet',  'action':'store_true',   'help':'quiet',          'reg': False, 'default': False },          
  {'o1':'-l', 'var':'config_syslog', 'action':'store_true',   'help':'syslog',         'reg': False, 'default': False },  
]

def main():

    msgs     = Ymsg(__file__)
    defaults = Yattr(__file__)

    # == Config UI ==
    # =============== 
    ui     = BaseCmdUI(msgs)
    
    # all the exceptions are handled by 'ui'
    try:
        cmd = TransmissionCmd()  
        cmd.msgs = msgs
        
        usage_template = """%prog [options] command
    
version $Id$ by Jean-Lou Dupont

*** Interface to Transmission (Bittorent client) ***

Commands:
^^{commands}"""
            
        tpl = ExTemplate( usage_template )
        usage = tpl.substitute( {'commands' : cmd.commands_help} )
    
        # Use OptParse to process arguments
        ui.handleArguments(usage, _options)
                
        # Configure ourselves a logger
        _quiet  = True  if ui.options.config_quiet  else False
        _syslog = False if ui.options.config_syslog else True        
        logger = _logger.logger('trns', include_console = _quiet, include_syslog = _syslog )

        cmd.logger = logger
        ui.logger  = logger

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
        r = reg.Registry('trns')
        ui.updateRegistry(r, _options, ui.options)
        
        params = {}
        
        # integrate options which aren't subjected to the registry
        ui.integrateOptions(ui.options, params, _options)
        
        # integrate default config
        ui.integrateDefaults(defaults, r, _options, params)

        # Verify parameter type
        ui.verifyType(params, _options)
        
        # Configure Backup cmd object
        ui.copyOptions(params, cmd, _options)
        
        # == command validation ==
        # ========================
        if ui.command is None:
            sys.exit(0)
               
        cmd.validateCommand(ui.command)       
                 
        # get rid of command from the arg list
        ui.popArg()
        
        # == DISPATCHER ==
        # ================
        getattr( cmd, "cmd_%s" % ui.command )(ui.args)
        
    except Exception,e:
        ui.handleError( e )
        sys.exit(1)
        
    sys.exit(0)
    # === END ===

# =======================================================================

if __name__== "__main__":   
    main()
