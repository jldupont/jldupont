""" MindMeister backup daemon
    @author: Jean-Lou Dupont
    
    Prerequisites:
    - requires the key 'file' in the registry to be properly set
      This filesystem path points to the Sqlite database used to
      store the map related information.
      
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"


def main():
    """ Entry point
        - Performs command line processing
        -- start:   verifies required configuration
        -- stop:    finds process, sends TERM
        -- restart: performs stop, performs start
    """

# ==============================================
# ==============================================
class mmdDaemon(object):
    """ Daemon
    """
    def __init__(self):
        pass
    
    
    
# ==============================================
# ==============================================
import os.path
from jld.tools.messages import Messages
class mmdMessages(Messages):
    """ Messages
    """
    filepath = os.path.dirname( os.path.abspath( __file__ )) + os.sep + "mmd_messages.yaml"
    def __init__(self):
        Messages.__init__(self, self.filepath)

# ==============================================
# ==============================================

from   jld.cmd import BaseCmd
class CmdLineInterface(BaseCmd):
    """ Handles the command line interface of this daemon
    """
    def __init__(self):
        BaseCmd.__init__(self)

    def cmd_start(self, *args):
        """ Starts the daemon """

    def cmd_stop(self, *args):
        """ Stops the daemon """
        
    def cmd_restart(self, *args):
        """ Restarts the daemon """

# ==============================================
# ==============================================

if __name__ == "__main__":
    main()