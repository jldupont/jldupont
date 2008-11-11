""" Backup for MindMeister mindmaps
""" 
import sys
import os.path
try:
    import jld.api.mindmeister as mm
    import jld.registry as reg
    import jld.tools.class as tclass
except:
    pass

from optparse import OptionParser

class Backup(object):
    
    def __init__(self, secret, api_key):
        self.secret = secret
        self.api_key = api_key
    
    def cmd_auth(self):
        """
        """
    
    def cmd_export_all(self):
        """
        """

    

def main():
    usage = """%prog [options] command
version $Id$ by Jean-Lou Dupont

Command:
    auth
    export_all
"""

    parser = OptionParser( usage=usage )
    parser.add_option( "-s", "--secret", dest="secret", action="store",
                       help="configure secret" )
    
    parser.add_option( "-k", "--key", dest="api_key", action="store",
                       help="configure api_key" )
    
    (options,args) = parser.parse_args()
    
    print options, args
    
    # make sure we have SECRET and API_KEY configured in the registry
    r = reg.Registry()
    if (options.contains('secret')):
        r.setKey('mindmeister', 'secret', options['secret'])
    if (options.contains('api_key')):
        r.setKey('mindmeister', 'api_key', options['api_key'])
        
    # ==
    secret  = r.getKey('mindmeister', 'secret')
    api_key = r.getKey('mindmeister', 'api_key') 
    b = Backup( secret, api_key )

    # ==
    

# =======================================================================

if __name__== "__main__":

    #directory levels to reach libs folder
    levelsUp = 2
    
    #setup for development environment
    try:
        import jld.registry as reg
    except:
        path = os.path.abspath( __file__ )
        while levelsUp>0:
            path = os.path.dirname( path )
            levelsUp = levelsUp - 1    
        sys.path.append( path )
        
    main()
