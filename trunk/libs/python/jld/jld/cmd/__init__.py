""" Command Line tools
    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"
__dependencies__ = []

import sys
import jld.api as api
import jld.tools.klass as tclass

class BaseCmd(object):
    """ Base class for command line utilities
    """
    
    _platform_win32 = sys.platform[:3] == 'win'
    
    def __init__(self):
        """ Scans through all the methods of this instance
            and extracts all the ones prefixed with 'cmd_'
        """
        self.cmds, self.commands = tclass.searchForMethods( self, 'cmd_' )
        self.commands_help = ''
        
    def genCommandsHelp(self):
        """ Generates the list of commands and their corresponding docstring.
            Methods with prefix 'test' are ignored.
        """
        if (self.commands_help==''):
            for name, doc in self.commands:
                if (not name.startswith('test')):
                    self.commands_help = self.commands_help + "  " + name + ' :  ' + doc + "\n"

        return self.commands_help
    
    def configure(self):
        """ Configures various parameters
        """

    def validateCommand(self, command):
        """ Validates the specified command
        """ 
        if (command not in self.cmds):
            raise api.ErrorInvalidCommand( 'invalid command', {'cmd':command} )
        

# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """