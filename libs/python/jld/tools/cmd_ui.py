""" Cmd Line User Interface
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import re
import sys

class UIBase(object):
    """ Base class for Command Line UI
        This class expects a _map dict with the following format:
        {    exception_class : {
                'msg':      message_key,
                'help':     OS_independent_help_key
                'help_win': win_dependent_help_key,  #OPTIONAL
                'help_nix': nix_dependent_help_key,  #OPTIONAL
             }
        }
    
    """
    _platform_win32 = sys.platform[:3] == 'win'
    
    def __init__(self):
        self.msgs = None
        self.params = {}
    
    def setParams(self, msgs, params):
        """ Generic parameter setting interface
        """
        self.msgs = msgs
        self.params = params

    def handleError( self, exc ):
        """ Displays, if required, an appropriate user message
            corresponding to an error condition.
            Also generates logging and/or email messages as appropriate.
        """
        classe = re.compile("\'(.*)\'").search( str( exc.__class__ ) ).group(1)
        if (not self._map.has_key( classe )):
            self.msgs.render( 'unhandled_exception', {'exc:': exc} )
            sys.exit(0)

    