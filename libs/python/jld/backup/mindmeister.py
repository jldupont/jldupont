""" Backup for MindMeister mindmaps
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"
import sys
import os.path
import logging
from string import Template
try:
    import jld.registry as reg
    import jld.tools.klass as tclass
    import jld.api.mindmeister as mm
    from jld.cmd import BaseCmd
except Exception,e:
    #directory levels to reach libs folder
    levelsUp = 3
    path = os.path.abspath( __file__ )
    while levelsUp>0:
        path = os.path.dirname( path )
        levelsUp = levelsUp - 1    
    sys.path.append( path )
    import jld.registry as reg
    import jld.tools.klass as tclass
    import jld.api.mindmeister as mm
    from jld.cmd import BaseCmd    

from optparse import OptionParser

class Backup(BaseCmd):
    """MindMeister Backup class
    """
    def __init__(self):
        BaseCmd.__init__(self)
        self.secret = None
        self.api_key = None
    
    def cmd_auth(self):
        """Generates an authentication URL and opens a browser instance for the user"""
    
    def cmd_export_all(self):
        """Exports all the maps"""


# ========================================================================================
def main():

    backup = Backup()
    
    usage_template = """%prog [options] command
version $Id$ by Jean-Lou Dupont

Commands:
^^commands
"""
    class MyTemplate(Template):
        delimiter = '^^'
        def __init__(self, init):
            Template.__init__(self, init)
        
    commands_help = backup.genCommandsHelp()
        
    tpl = MyTemplate( usage_template )
    tpl_values = {'commands':commands_help}
    usage = tpl.substitute( tpl_values )

    parser = OptionParser( usage=usage )
    parser.add_option( "-s", "--secret", dest="secret", action="store",
                       help="configure secret" )
    
    parser.add_option( "-k", "--key", dest="api_key", action="store",
                       help="configure api_key" )
    
    (options,args) = parser.parse_args()
    
    # make sure we have SECRET and API_KEY configured in the registry
    r = reg.Registry()
    
    try:    r.setKey(r, 'mindmeister', 'secret', options.secret, cond=True)
    except: pass
    try:    r.setKey(r, 'mindmeister', 'api_key', options.api_key, cond=True)
    except: pass    
        
    # == configuration ==
    secret  = r.getKey('mindmeister', 'secret')
    api_key = r.getKey('mindmeister', 'api_key') 
    backup.secret = secret
    backup.api_key = api_key

    # == command dispatch ==
    try:
        command = args[0]
    except:
        print "use -h for help"
        sys.exit(0)
        
    if (command not in commands):
        print "invalid command [%s]" % args[0]
        sys.exit(0)
        

# =======================================================================

if __name__== "__main__":
        
    main()
