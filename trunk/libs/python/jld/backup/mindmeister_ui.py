""" MindMeister User Interface
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import re
import sys
import jld.api as api
import jld.registry as reg

class MM_UI(object):
    """ Handles user interface
    """
    _map = {
        'ErrorNetwork':     (),
        'ErrorAccess':      (),
        'ErrorObject':      (),
        'ErrorMethod':      (),
        'ErrorValidation':  (),
        'ErrorProperty':    (),
        'ErrorProtocol':    (),
        'RegistryException':(),
    }
    
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
        

# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
