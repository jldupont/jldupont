#!/usr/bin/env python
""" Home Monitoring

    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import sys
import logging
import os.path
from types import *
from optparse import OptionParser

import jld.registry       as reg
from   jld.tools.ytools   import Yattr, Ymsg
from   jld.cmd_g2.base_ui import BaseCmdUI 
from   jld.tools.template import ExTemplate
import jld.tools.logger   as _logger

from cmd import HomeMonCmd


# ========================================================================================
_options =[
  {'o1':'-l', 'var':'config_syslog',  'action':'store_true', 'help':'config_syslog',  'reg': False, 'default': False },
]

def main():

    msgs   = Ymsg(__file__)
    config = Yattr(__file__, 'config.yaml')

    # == Config UI ==
    # =============== 
    ui     = BaseCmdUI(msgs)
    
    # all the exceptions are handled by 'ui'
    try:
        cmd = HomeMonCmd()  
        cmd.msgs = msgs
        
        usage_template = """%prog [options] command
    
version $Id$ by Jean-Lou Dupont

*** Home Monitoring ***

Commands:
^^{commands}"""
            
        tpl = ExTemplate( usage_template )
        usage = tpl.substitute( {'commands' : cmd.commands_help} )

        # Use OptParse to process arguments
        ui.handleArguments(usage, _options)
                
        # Configure ourselves a logger
        _syslog  = ui.options.config_syslog
        logger = _logger.logger('homemon', include_console = False, include_syslog = _syslog )

        cmd.logger = logger
        ui.logger  = logger

        # == configuration ==


        
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
