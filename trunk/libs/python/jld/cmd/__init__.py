"""Command Line tools
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import jld.tools.klass as tclass

class BaseCmd(object):
    """ Base class for command line utilities
    """
    
    def __init__(self):
        """ Scans through all the methods of this instance
            and extracts all the ones prefixed with 'cmd_'
        """
        self.cmds, self.commands = tclass.searchForMethods( self, 'cmd_' )
        self.commands_help = None
        
    def genCommandsHelp(self):
        """ Generates the list of commands and their corresponding docstring
        """
        if (self.commands_help is None):
            self.commands_help = ''
            for name, doc in self.commands:
                self.commands_help = self.commands_help + "\t" + name + ' : ' + doc + "\n"

        return self.commands_help