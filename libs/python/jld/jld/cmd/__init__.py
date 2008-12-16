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
        
    # =========================================================
    # Iteration & Dict access interfaces
    #  Used for the command ''listconfig''
    # =========================================================
    def __contains__(self, key):
        return key in self._configParams
    
    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem(self, key, value):
        setattr(self, key, value)
    
    def __iter__(self):
        self.iter = True
        return self
    
    def next(self):
        if (self.iter):
            self.iter = False
            return self
        else:
            raise StopIteration
        
    def genCommandsHelp(self, padding=15):
        """ Generates the list of commands and their corresponding docstring.
            Methods with prefix 'test' are ignored.
        """
        if (self.commands_help==''):
            for name, doc in self.commands:
                if (not name.startswith('test')):
                    line = "%*s : %s\n" % (padding,name,doc)
                    self.commands_help = self.commands_help + line #+ "  " + name + ' :  ' + doc + "\n"

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
