""" Command Line tools
    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import sys
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
        """ Generates the list of commands and their corresponding docstring
        """
        if (self.commands_help==''):
            for name, doc in self.commands:
                self.commands_help = self.commands_help + "\t" + name + ' :  ' + doc + "\n"

        return self.commands_help
    
    def configure(self):
        """ Configures various parameters
        """



# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
