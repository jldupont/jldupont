#!/usr/bin/env python
""" 
    Base class for daemons
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import os
import sys
import signal
import time

# =================================================
try:
    import jld.api as api
except:
    # ASSUME THAT THE REQUIRED LIBS are available
    # RELATIVE to this script => simplified install
    levelsUp = 3
    path = os.path.abspath( __file__ )
    while levelsUp>0:
        path = os.path.dirname( path )
        levelsUp = levelsUp - 1    
    sys.path.append( path )
    # =============================================
    import jld.api as api
# =================================================



def defaultLogger(name):
    """ Default logger factory
    """
    import logging
    import logging.handlers
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    
    _file = "/var/log/%s.log" % name
    hdlr = logging.handlers.TimedRotatingFileHandler( _file )
    hdlr.setFormatter( formatter )
    logger = logging.Logger( name )
    logger.addHandler(hdlr)
    return logger
    
# ==============================================

class BaseDaemon(object):
    """ Base class for daemon
        Implements commands: start, stop, restart, run
        Writes PID info in /var/run/$name.log
    """
    _UMASK   = 0
    _WORKDIR = "/"
    _MAXFD   = 1024
    
    _REDIRECT_TO = os.devnull if hasattr(os,"devnull") else "/dev/null"
    
    def __init__(self, name, loggerFactory = defaultLogger):
        """ name:  name of the daemon
            loggerFactory: a function acting as factory
                            that creates a logger instance
        """
        self.name = name
        self.loggerFactory = loggerFactory
        self.logger = None
        self.pidfile = "/var/run/%s.pid" % name

    def _createLogger(self):
        if (self.logger):
            return
        self.logger = self.loggerFactory(self.name)

    def _format(self, msg):
        """ Performs as first pass formatting
            of log messages.
        """
        return "[%s] - %s" % (self.name, msg)

    def logdebug(self, msg):
        self._createLogger()
        msg = self._format(msg)
        if (self.logger):
            self.logger.debug(msg)
    def loginfo(self, msg):
        self._createLogger()
        msg = self._format(msg)
        if (self.logger):
            self.logger.info(msg)
    def logwarning(self, msg):
        self._createLogger()
        msg = self._format(msg)
        if (self.logger):
            self.logger.warning(msg)
    def logerror(self, msg):
        self._createLogger()
        msg = self._format(msg)
        if (self.logger):
            self.logger.error(msg)

    def findPID(self):
        pf = None
        try:
            pf = open(self.pidfile,'r')
            pid = int( pf.read().strip() )
        except Exception,e:
            pid = None
        finally:
            if (pf):
                pf.close()            
        return pid

    def _writePID(self):
        pf = None
        pid = str( os.getpid() )
        try:
            pf = open(self.pidfile,'w+')
            pf.write('%s\n' % pid)
        except Exception,e:
            self.logerror("cannot write to pidfile [%s]" % self.pidfile)
        finally:
            if (pf):
                pf.close()            

    def _delPID(self):
        try:
            os.remove(self.pidfile)
        except:
            pass

    def start(self):
        """ Tries to start the daemon
        """
        print 'daemon.start(): name[%s]' % self.name
        pid = self.findPID()
        if (pid):
            raise api.ErrorDaemon('daemon_exists',{'pid':pid})

        #===============
        self.daemonize()
        #=== from this point, all parent resources are closed:
        #=== no more file handlers etc.
        #=== need to grab a logger of our own
        self._createLogger()
        self._writePID()
        self.loginfo('Issuing run()')
        self.run()

    def stop(self):
        """ Tries to stop the daemon
        """
        pid = self.findPID()
        if (pid):
            self.loginfo('Stopping pid[%s]' % pid)
            self._kill( pid )
            self._delPID()
        else:
            raise api.ErrorDaemon('cant_find_pid',{})

    def restart(self):
        self.stop()
        self.start()

    def _kill(self, pid):
        try:
            while True:
                os.kill(pid, signal.SIGTERM)
                time.sleep(0.1)
        except OSError,e:
            if ('No such process' in str(e)):
                self.loginfo('Killed pid[%s]' % pid)
            else:
                self.logerror('Cannot kill pid[%s]' % pid)

    def daemonize(self):
        """ Creates the daemon
        """
        try:
            pid = os.fork()
        except Exception,e:
            raise api.ErrorDaemon('cant_fork',{'msg':str(e)})
        
        self._createLogger()
        
        if (pid == 0):
            os.setsid()
            try:
                pid = os.fork()
            except Exception,e:
                self.logerror('Daemonize: cannot fork 2nd time')
                raise api.ErrorDaemon('cant_fork',{'msg':str(e)})
            
            self._createLogger()
            
            if (pid == 0):
                os.chdir( self._WORKDIR )
                os.umask( self._UMASK )
            else:
                os._exit(0)
        else:
            os._exit(0)
        
        self._createLogger()
        
        import resource
        maxfd = resource.getrlimit( resource.RLIMIT_NOFILE )[1]
        if (maxfd == resource.RLIM_INFINITY):
            maxfd = self._MAXFD
                
        for fd in range(0, maxfd):
            try:
                os.close(fd)
            except:
                pass
            
        os.open(self._REDIRECT_TO, os.O_RDWR)
        os.dup2(0,1)
        os.dup2(0,2)
        
    def run(self):
        """ Run - to subclass
        """
        self.loginfo('Default run()')        
        while True:
            signal.pause()


# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    import logging
    import logging.handlers
    
    if (len(sys.argv) != 2):
        print "usage: daemon cmd"
        sys.exit(0)
    
    _logfile = '/var/log/daemon_test.log'
        
    cmds = ['start', 'stop', 'restart']
    daemon = BaseDaemon( 'daemon_test', defaultLogger )
    
    cmd = sys.argv[1]
    if (not cmd in cmds):
        print "unknown command"
        sys.exit(0)
    
    try:
        getattr( daemon, cmd )()
    except Exception,e:
        print "msg: [%s]" % e
    