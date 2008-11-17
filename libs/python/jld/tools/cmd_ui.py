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
                'help':     OS_independent_help_key  #OPTIONAL and only used if help_win nor help_nix present
                'help_win': win_dependent_help_key,  #OPTIONAL
                'help_nix': nix_dependent_help_key,  #OPTIONAL
             }
        }
    
    """
    _platform_win32 = sys.platform[:3] == 'win'
    
    def __init__(self, msgs = None):
        self.msgs = msgs
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
            print self.msgs.render( 'unhandled_exception', {'exc': str( exc ) } )
            sys.exit(0)

        _entry = self._map[classe]
        
        msg_key  = _entry['msg']
        help_key = self._resolveHelp( _entry )
        
        msg = self.msgs.render( msg_key )
        if (help_key is not None):
            msg = msg + ': ' + self.msgs.render( help_key )
        
        print msg
        
    def _resolveHelp(self, entry):
        if (self._platform_win32):
            if (entry.has_key('help_win')):
                return entry['help_win']

        if (not self._platform_win32):
            if (entry.has_key('help_nix')):
                return entry['help_nix']
            
        if (entry.has_key('help')):
            return entry['help']
        
        return None
                

    