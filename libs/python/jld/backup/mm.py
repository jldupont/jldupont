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
# RELATIVE to this script
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
          {'o1':'-e',    'o2':'--email',   'var':'email',  'action':'store',        'help':'config_email',  'reg': True, 'default': None},
          {'o1':'-s',    'o2':'--secret',  'var':'secret', 'action':'store',        'help':'config_secret', 'reg': True, 'default': None},
          {'o1':'-k',    'o2':'--key',     'var':'api_key','action':'store',        'help':'config_key',    'reg':True, 'default': None},
          {'o1':'-q',    'o2':'--quiet',   'var':'quiet',  'action':'store_true',   'help':'quiet',         'reg':False, 'default': False },          
]

def main():

    ui     = mui.MM_UI()
    msgs   = msg.MM_Messages()
    backup = Backup()
    
    usage_template = """%prog [options] command
version $Id$ by Jean-Lou Dupont

Commands:
^^{commands}
"""
        
    commands_help = backup.genCommandsHelp()
        
    tpl = ExTemplate( usage_template )
    tpl_values = {'commands' : commands_help}
    usage = tpl.substitute( tpl_values )

    parser = OptionParser( usage=usage )
    for o in _options:
        help_msg = msgs.render( o['help'] )
        parser.add_option( o['o1'], o['o2'], dest=o['var'], action=o['action'], help=help_msg, default=o['default'])
    
    (options,args) = parser.parse_args()

        
    # make sure we have SECRET and API_KEY configured in the registry
    # Use conditional 'setKey' if we have valid overriding values i.e. not None
    r = reg.Registry()
    for o in _options:
        if ( not o['reg'] ):
            continue
        try:    
            r.setKey('mindmeister', o['var'], getattr( options, o['var'] ), cond=True)
        except Exception,e: 
            logging.error("error setting registry: is the proper user access in place? [%s]" % e)
            sys.exit(0)
        
    # == configuration ==
    # ===================
    secret  = r.getKey('mindmeister', 'secret')
    api_key = r.getKey('mindmeister', 'api_key') 
    backup.secret = secret
    backup.api_key = api_key
    try:    backup.quiet = options.quiet
    except: pass

    # == simple check ==
    # ==================
    if (secret is None) or (api_key is None):
        print msgs.render( 'configuration' )
        sys.exit(0)

    # == command validation ==
    # ========================
    try:    
        command = args[0]
        if (command not in backup.cmds):
            print msgs.render( 'invalid_command', {'cmd':args[0] } )
            sys.exit(0)
    except:
        print msgs.render('use_help')
        sys.exit(0)
     
    # get rid of command from the arg list
    args.pop(0)
     
    # == DISPATCHER ==
    # ================
    try:
        getattr( backup, "cmd_%s" % command )(args)
    except api.ErrorNetwork,e:
        pass
    except reg.RegistryException,e:
        pass
    except Exception,e:
        pass
    
    # === END ===

# =======================================================================

if __name__== "__main__":   
    main()
