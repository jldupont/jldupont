#!/usr/bin/python
""" Backup for MindMeister mindmaps

    Dependencies:
        module yaml   (available @ http://pyyaml.org/wiki/PyYAML)

"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import sys
import logging
import os.path
from string import Template
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
from   jld.tools.template import ExTemplate

# ========================================================================================
_options =[
  {'o1':'-s', 'var':'secret', 'action':'store',        'help':'config_secret', 'reg': True, 'default': None},
  {'o1':'-k', 'var':'api_key','action':'store',        'help':'config_key',    'reg': True, 'default': None},
  {'o1':'-f', 'var':'file',   'action':'store',        'help':'config_file',   'reg': True, 'default': None},
  #{'o1':'-q', 'var':'quiet',  'action':'store_true',   'help':'quiet',         'reg': False, 'default': False },          
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
    
        parser = OptionParser( usage=usage )
        for o in _options:
            help_msg = msgs.render( o['help'] )
            parser.add_option( o['o1'], 
                               dest=o['var'], 
                               action=o['action'], 
                               help=help_msg, 
                               default=o['default'] )
        
        (options,args) = parser.parse_args()
    
        # make sure we have SECRET and API_KEY configured in the registry
        # Use conditional 'setKey' if we have valid overriding values i.e. not None
        r = reg.Registry()
        for o in _options:
            if ( o['reg'] ): 
                r.setKey('mindmeister', o['var'], getattr( options, o['var'] ), cond=True)
    
        # == configuration ==
        # ===================
        params = {}
        
        #params['quiet'] = options.quiet
        
        file    = params['file']    = r.getKey('mindmeister', 'file')
        secret  = params['secret']  = r.getKey('mindmeister', 'secret')
        api_key = params['api_key'] = r.getKey('mindmeister', 'api_key')
         
        backup.file    = file
        backup.secret  = secret
        backup.api_key = api_key
    
        # == command validation ==
        # ========================
        command = args[0] if (0 in args) else None
        if (command not in backup.cmds):
            raise api.ErrorInvalidCommand( 'invalid command', {'cmd':command} )
         
        # get rid of command from the arg list
        args.pop(0)
         
        # == DISPATCHER ==
        # ================
        getattr( backup, "cmd_%s" % command )(args)
        
    except Exception,e:
        ui.handleError( e )
        
    # === END ===

# =======================================================================

if __name__== "__main__":   
    main()
