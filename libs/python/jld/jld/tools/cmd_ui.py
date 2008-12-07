""" Cmd Line User Interface
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"
__msgs__ = ['unhandled_exception',]

import re
import sys
from types import *
from string import Template
from optparse import OptionParser

import jld.api as api

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
        self.logger = None
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
        try:    params = exc.params
        except: params = None
            
        #TODO: Also generates logging and/or email messages as appropriate.
        classe = re.compile("\'(.*)\'").search( str( exc.__class__ ) ).group(1)
        if (classe not in self._map):
            print self.msgs.render( 'unhandled_exception', {'exc': str( exc ) } )
            return

        #Additional 'postfix' message?
        try:    
            possible_msg = exc.msg
            if (possible_msg.startswith('msg:')):
                msgid = possible_msg[4:]
            pmsg = self.msgs.render( msgid )
        except: 
            pmsg = ''

        _entry = self._map[classe]
        
        msg_key  = _entry['msg']
        help_key = self._resolveHelp( _entry )
        
        msg = self.msgs.render( msg_key, params )
        
        if (help_key is not None):
            help = self.msgs.render( help_key, params )
            msg = msg + ': ' + help
        
        result_msg = msg + ' ' + pmsg
        self.logger.error( result_msg )
        
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
        
    def updateRegistry(self, reg, options, args):
        """Updates the registry from the command-line args"""
        for o in options:
            #if we are told to update the registry
            if ( o['reg'] ):
                key = o['var']
                val = getattr( args, key )
                if (val is not None):
                    reg[key] = val 

    def copyOptions(self, source, target, _options):
        """ Copies all options from source to target
            source
                the source dictionary
            target
                the target object with dictionary access
            _options
                the reference options list
        """
        for o in _options:
            key = o['var']
            val = source[key]
            setattr( target, key, val )

    def integrateDefaults(self, defs, reg, _options, params):
        """Integrates the default values for each option if
            no value can be found in the registry.
            defs
                the defaults dictionary
            reg
                the registry dictionary
            _options
                the options list
            params
                the result dictionary
        """
        for o in _options:
            key = o['var']
            # only options subjected to the registry!
            if (o['reg']):
                val = reg[key]
                if val is None:
                    val = defs.defaults[key] if (key in defs.defaults) else None                    
                params[key] = val

    def integrateOptions(self, options, params, _options):
        """Integrate options that aren't subjected to the registry
            options
                the current options as parsed from the command line
            params
                the result dictionary
            _options
                the reference options list
        """
        for o in _options:
            key = o['var']
            if (not o['reg']):
                val = getattr(options, key)
                params[key] = val

    def verifyType(self, params, _options):
        for o in _options:
            if ('type' in o):
                key  = o['var']
                tipe = o['type']
                value = params[key]
                #print "key[%s] type[%s] value[%s] type value[%s]" % (key,tipe, value, type(value))
                                
                if (tipe is 'int') and (type(value) is not IntType):
                    try:
                        intVal = int(value)
                        params[key] = intVal
                    except:
                        raise api.ErrorConfig('msg:error_config_type', {'key':key, 'type':tipe})
