""" Command Line tools, generation2

    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"
__dependencies__ = []

__all__ = ['BaseCmd', 'Hook', 'BaseCmdException']

import os
import sys
import subprocess

class BaseCmdException(Exception):
    def __init__(self, msg, params = None):
        Exception.__init__(self, msg)
        self.msg = msg
        self.params = params

class metaBaseCmd(type):
    
    _prefix = 'cmd_'
    
    def __init__(cls, name, bases, ns):
        cls._extractCommands(ns)

    def _extractCommands(cls, ns):
        ""
        cls.commands = filter( lambda X: str(X).startswith(cls._prefix), ns )
        cls.cmds = map( lambda X: str(X)[len(cls._prefix):], cls.commands )


class BaseCmd(object):
    """ Base class for command line utilities
    
    >>> c = TestCmd()
    >>> print c.commands
    ['cmd_a', 'cmd_b']
    """

    __metaclass__ = metaBaseCmd
    
    _platform_win32 = sys.platform[:3] == 'win'
    _prefix = 'cmd_'
    
    def __init__(self):
        """ Scans through all the methods of this instance
            and extracts all the ones prefixed with 'cmd_'
        """
        self._genCommandsHelp()

    def _genCommandsHelp(self, padding=15):
        """ Generates the list of commands and their corresponding docstring.
            Methods with prefix 'test' are ignored.
        """
        self.commands_help = ''
        for cmd in self.commands:
            if (cmd.startswith('test')):
                continue

            name = str(cmd)[len(self._prefix):]
            method = getattr(self, cmd)
            try:    doc = getattr(method, '__doc__')
            except: doc = ''

            line = "%*s : %s\n" % (padding,name,doc)
            self.commands_help = self.commands_help + line


    def validateCommand(self, command):
        """ Validates the specified command
        """ 
        if (command not in self.cmds):
            raise BaseCmdException( 'error_invalid_command', {'cmd':command} )

    def _fireEvent(self, path, environ):
        """ Fires the associated Event Manager
        
            @return: (True, None) if the path is not available
            @raise ErrorPopen 
        """
        try:
            em = EventMgr(path, environ)
            if not em.exists():
                return True
            return em.run()
        except:
            raise BaseCmdException('error_eventmgr', {'path':path, 'environ':environ})


# ==============================================
# ==============================================

class BaseCmdUI(object):
    """ Base class for Command Line UI
    
        @see: trns.py for example
    """
    _platform_win32 = sys.platform[:3] == 'win'
    
    def __init__(self, msgs, logger = None):
        self.logger = logger
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
            
            @param exc: Exception being raised
        """
        try:    params = exc.params
        except: params = None
            
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
        try:    self.logger.error( result_msg )
        except: pass
        
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

            @param source: the source dictionary
            @param target: the target object with dictionary access
            @param _options: the reference options list
        """
        for o in _options:
            key = o['var']
            val = source[key]
            setattr( target, key, val )

    def integrateDefaults(self, defs, reg, _options, params):
        """Integrates the default values for each option if
            no value can be found in the registry.
            
            @param defs: the defaults dictionary
            @param reg: the registry dictionary
            @param _options: the options list
            @param params: the result dictionary
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
        
            @param options: the current options as parsed from the command line
            @param params: the result dictionary
            @param _options: the reference options list
        """
        for o in _options:
            key = o['var']
            if (not o['reg']):
                val = getattr(options, key)
                params[key] = val

    def verifyType(self, params, _options):
        """ Performs type verification
        """
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



# ==============================================
# ==============================================

class EventMgr(object):
    """ For dispatching events to Event Manager scripts
    
        Windows Test, change to $HOOK_VAR for Linux
        >> h = EventMgr("echo %HOOK_VAR%", {"HOOK_VAR":"test!"} , shell=True)
        >> h.run()
        0
        >> h.exists()
        False
    """
    def __init__(self, path, env_vars, shell = False):
        ""
        self.shell    = shell        
        self.env_vars = self._adjustEnvVars( env_vars )
        self.path     = os.path.expanduser(path)
    
    def _adjustEnvVars(self, vars):
        """ All environment variables must be string
        """
        for k,v in vars.iteritems():
            vars[k] = str(v)
        return vars
    
    def exists(self):
        """ Verifies if the target shell command exists.
            Note that this method only verifies the existence
            of filesystem path and not shell built-in commands
            e.g. *echo*
        """
        return os.path.exists(self.path)
    
    def run(self):
        return subprocess.call(self.path, env=self.env_vars, shell=self.shell)


# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    class TestCmd(BaseCmd):
        def __init__(self):
            BaseCmd.__init__(self)
            
        def cmd_a(self):
            """help cmd_a"""

        def cmd_b(self):
            """help cmd_b"""
            
    
    import doctest
    doctest.testmod()

