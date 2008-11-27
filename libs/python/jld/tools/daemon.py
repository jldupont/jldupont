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

# ASSUME THAT THE REQUIRED LIBS are available
# RELATIVE to this script => simplified install
levelsUp = 3
path = os.path.abspath( __file__ )
while levelsUp>0:
    path = os.path.dirname( path )
    levelsUp = levelsUp - 1    
sys.path.append( path )

import jld.api as api

class BaseDaemon(object):
    """ Base class for daemon
    """
    _UMASK   = 0
    _WORKDIR = "/"
    _MAXFD   = 1024
    
    _REDIRECT_TO = os.devnull if hasattr(os,"devnull") else "/dev/null"
    
    def __init__(self, name, logger = None):
        """ 
        """
        self.name = name
        self.logger = logger
        self.pidfile = "/var/run/%s.pid" % name

    def loginfo(self, msg):
        if (self.logger):
            self.logger.info(msg)
    def logwarning(self, msg):
        if (self.logger):
            self.logger.warning(msg)
    def logerror(self, msg):
        if (self.logger):
            self.logger.error(msg)

    def findPID(self):
        try:
            pf = open(self.pidfile,'r')
            pid = int( pf.read().strip() )
            pf.close()
        except Exception,e:
            pid = None

        return pid

    def _writePID(self):
        pid = str( os.getpid() )
        try:
            pf = open(self.pidfile,'w+')
            pf.write('%s\n' % pid)
            pf.close()
        except Exception,e:
            self.logerror("cannot write to pidfile [%s]" % self.pidfile)

    def _delPID(self):
        try:
            os.remove(self.pidfile)
        except:
            pass

    def start(self):
        """ Tries to start the daemon
        """
        pid = self.findPID()
        if (pid):
            raise api.ErrorDaemon('daemon_exists',{'pid':pid})
        
        self.daemonize()
        #=== from this point, all parent resources are closed:
        #=== no more file handlers etc.
        #=== need to grab a logger of our own
        self._writePID()
        self.run()

    def stop(self):
        """ Tries to stop the daemon
        """
        pid = self.findPID()
        if (pid):
            self.loginfo('stopping [%s] pid[%s]' % (self.name, pid))
            self._kill( pid )
            self._delPID()
        else:
            self.logwarning('cannot find [%s]' % self.name)
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
                self.loginfo('killed [%s]' % pid)
            else:
                self.logerror('cannot kill pid[%s]' % pid)
                sys.exit(0)

    def daemonize(self):
        """ Creates the daemon
        """
        try:
            pid = os.fork()
        except Exception,e:
            self.logerror('daemonize: cannot fork')
            raise api.ErrorDaemon('cant_fork',{'msg':str(e)})
        
        if (pid == 0):
            os.setsid()
            try:
                pid = os.fork()
            except Exception,e:
                self.logerror('daemonize: cannot fork 2nd')
                raise api.ErrorDaemon('cant_fork',{'msg':str(e)})
            
            if (pid == 0):
                os.chdir( self._WORKDIR )
                os.umask( self._UMASK )
            else:
                os._exit(0)
        else:
            os._exit(0)
            
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
        """ Run
            Pattern "Strategy"
        """
        self.loginfo('default run')        
        while True:
            signal.pause()

    
# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    if (len(sys.argv) != 2):
        print "usage: daemon cmd"
        sys.exit(0)
    
    _logfile = '/var/log/daemon_test.log'
    
    if (not os.path.exists(_logfile) ):
        fp = open(_logfile,'w+')
        fp.close()
        
    
    import logging
    import logging.handlers
    hdlr = logging.handlers.TimedRotatingFileHandler( _logfile )
    logger = logging.Logger('daemon_test')
    logger.addHandler(hdlr)
    
    cmds = ['start', 'stop', 'restart']
    daemon = BaseDaemon( 'daemon_test', logger )
    
    cmd = sys.argv[1]
    if (not cmd in cmds):
        print "unknown command"
        sys.exit(0)
    
    try:
        getattr( daemon, cmd )()
    except Exception,e:
        print "msg: [%s]" % e
    