""" Backup for MindMeister mindmaps
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"
import sys
import os.path
from string import Template
import logging
try:
    import jld.registry as reg
    from jld.backup.mindmeister import Backup
    from jld.tools.template import ExTemplate
except Exception,e:
    #directory levels to reach libs folder
    levelsUp = 3
    path = os.path.abspath( __file__ )
    while levelsUp>0:
        path = os.path.dirname( path )
        levelsUp = levelsUp - 1    
    sys.path.append( path )
    import jld.registry as reg
    from jld.backup.mindmeister import Backup
    from jld.tools.template import ExTemplate    

from optparse import OptionParser

# ========================================================================================


def main():

    backup = Backup()
    
    usage_template = """%prog [options] command
version $Id$ by Jean-Lou Dupont

Commands:
^^{commands}
"""
        
    commands_help = backup.genCommandsHelp()
        
    tpl = ExTemplate( usage_template )
    tpl_values = {'commands':commands_help}
    usage = tpl.substitute( tpl_values )

    parser = OptionParser( usage=usage )
    parser.add_option( "-s", "--secret", dest="secret", action="store", help="configure secret" )
    parser.add_option( "-k", "--key", dest="api_key", action="store", help="configure api_key" )
    
    (options,args) = parser.parse_args()
    
    # make sure we have SECRET and API_KEY configured in the registry
    # Use conditional 'setKey' if we have valid overriding values i.e. not None
    r = reg.Registry()
    
    try:    r.setKey('mindmeister', 'secret', options.secret, cond=True)
    except Exception,e: logging.error("error setting registry, msg[%s]" %e)
    try:    r.setKey('mindmeister', 'api_key', options.api_key, cond=True)
    except Exception,e: logging.error("error setting registry, msg[%s]" %e)
        
    # == configuration ==
    # ===================
    secret  = r.getKey('mindmeister', 'secret')
    api_key = r.getKey('mindmeister', 'api_key') 
    backup.secret = secret
    backup.api_key = api_key

    # == simple check ==
    # ==================
    if (secret is None) or (api_key is None):
        print "please configure 'secret' and 'api_key'"
        sys.exit(0)

    # == command validation ==
    # ========================
    try:    
        command = args[0]
        if (command not in backup.cmds):
            print "invalid command [%s]" % args[0]
            sys.exit(0)
    except:
        print "use -h for help"
        sys.exit(0)
     
    # get rid of command from the arg list
    args.pop(0)
     
    # == DISPATCHER ==
    # ================
    getattr( backup, "cmd_%s" % command )(args)
    
    # === END ===

# =======================================================================

if __name__== "__main__":   
    main()
