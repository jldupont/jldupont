""" Cmd Line User Interface
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import re
import sys
from string import Template
from optparse import OptionParser

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
        self.options = None
        self.args = None
    
    def setParams(self, msgs):
        """ Generic parameter setting interface
        """
        self.msgs = msgs

    def popArg(self):
        """ Pops one argument from the list
        """
        return self.args.pop(0)

    def handleError( self, exc ):
        """ Displays, if required, an appropriate user message
            corresponding to an error condition.
        """
        try:
            params = exc.params
        except:
            params = None
            
        #TODO: Also generates logging and/or email messages as appropriate.
        classe = re.compile("\'(.*)\'").search( str( exc.__class__ ) ).group(1)
        if (classe not in self._map):
            print self.msgs.render( 'unhandled_exception', {'exc': str( exc ) } )
            return

        _entry = self._map[classe]
        
        msg_key  = _entry['msg']
        help_key = self._resolveHelp( _entry )
        
        msg = self.msgs.render( msg_key, params )
        
        if (help_key is not None):
            help = self.msgs.render( help_key, params )
            msg = msg + ': ' + help
        
        print msg
        
    def _resolveHelp(self, entry):
        if (self._platform_win32):
            if ('help_win' in entry):
                return entry['help_win']

        if (not self._platform_win32):
            if ('help_nix' in entry):
                return entry['help_nix']
            
        if ('help' in entry):
            return entry['help']
        
        return None
                
    def handleArguments(self, usage, _options):
        """ Processes command line options
        """ 
        parser = OptionParser( usage=usage )
        for o in _options:
            help_msg = self.msgs.render( o['help'] )
            parser.add_option( o['o1'], 
                               dest=o['var'], 
                               action=o['action'], 
                               help=help_msg, 
                               default=o['default'] )

        (self.options,self.args) = parser.parse_args()
        
