""" MindMeister backup daemon
    @author: Jean-Lou Dupont
    
    Prerequisites:
    - the keys 'secret', 'api_key' and 'file' be properly set in the registry.
      This filesystem path points to the Sqlite database used to
      store the map related information.
      
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import os
import sys

# ASSUME THAT THE REQUIRED LIBS are available
# RELATIVE to this script => simplified install
levelsUp = 3
path = os.path.abspath( __file__ )
while levelsUp>0:
    path = os.path.dirname( path )
    levelsUp = levelsUp - 1    
sys.path.append( path )

# ==============================================
# ==============================================
class mmdDaemon(object):
    """ Daemon
    """
    def __init__(self):
        pass
    
# ==============================================
# ==============================================   
import jld.tools.cmd_ui as ui
class mmdUI(ui.UIBase):
    """ Handles user interface
    """
    _map = {
        'jld.api.ErrorDb':              { 'msg': 'error_db',        'help': 'help_db', },
        'jld.api.ErrorAuth':            { 'msg': 'error_auth',      'help': 'help_auth', },
        'jld.api.ErrorNetwork':         { 'msg': 'error_network',   'help': 'help_network', },
        'jld.api.ErrorAccess':          { 'msg': 'error_access',    'help': 'help_access', },
        'jld.api.ErrorMethod':          { 'msg': 'error_method',    'help': 'help_method', },
        'jld.api.ErrorValidation':      { 'msg': 'error_validation','help': 'help_validation', },
        'jld.api.ErrorProtocol':        { 'msg': 'error_protocol',  'help': 'help_protocol', },
        'jld.api.ErrorInvalidCommand':  { 'msg': 'error_command',   'help': 'help_command', },
        'jld.registry.exception.RegistryException':{ 'msg': 'error_registry',  'help_win': 'help_registry_win', 'help_nix':'help_registry_nix' },
    }

      
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

from   jld.tools.template import ExTemplate
def main():
    """ Entry point
        - Performs command line processing
        -- start:   verifies required configuration
        -- stop:    finds process, sends TERM
        -- restart: performs stop, performs start
    """
    msgs   = mmdMessages()
    ui     = mmdUI()
    
    # == Config UI ==
    # ===============
    ui.setParams( msgs )    

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
    
        _options =[
          #{'o1':'-s', 'var':'secret', 'action':'store',        'help':'config_secret', 'reg': True, 'default': None},
          #{'o1':'-k', 'var':'api_key','action':'store',        'help':'config_key',    'reg': True, 'default': None},
          #{'o1':'-f', 'var':'file',   'action':'store',        'help':'config_file',   'reg': True, 'default': None},
          #{'o1':'-q', 'var':'quiet',  'action':'store_true',   'help':'quiet',         'reg': False, 'default': False },          
        ]
    
    
        ui.handleArguments(usage, _options)

    except Exception,e:
        ui.handleError(e)

# ==============================================
# ==============================================
if __name__ == "__main__":
    main()