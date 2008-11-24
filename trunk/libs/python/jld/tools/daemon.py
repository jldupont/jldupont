"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import os
import sys
import jld.api as api

class BaseDaemon(object):
    """ Base class for daemon
    """
    _UMASK   = 0
    _WORKDIR = "/"
    _MAXFD   = 1024
    
    _REDIRECT_TO = os.devnull if hasattr(os,"devnull") else "/dev/null"
    
    def __init__(self, name):
        """ 
        """
        self.name = name

    def stop(self):
        """ Tries to stop the daemon
        """
        try:
            import enumprocess
        except Exception,e:
            raise api.ErrorDaemon('cant_stop',{'msg':'missing "enumprocess" package'})



    def _findPid(self, name):
        """ Finds the pid list for process(es) with 'name'
        """
        liste = enumprocess.getPidNames()
        fliste= filter( lambda X: X[1] == name, liste.iteritems() )
        first = fliste[0] if len(fliste) else None
        return first
        
    def daemonize(self):
        """ Creates the daemon
        """
        try:
            pid = os.fork()
        except Exception,e:
            raise api.ErrorDaemon('cant_fork',{'msg':str(e)})
        
        if (pid == 0):
            os.setsid()
            try:
                pid = os.fork()
            except Exception,e:
                raise api.ErrorDaemon('cant_fork',{'msg':str(e)})
            
            if (pid == 0):
                os.chdir( self._WORKDIR )
                os.umask( self._UMASK )
            else:
                os._exit(0)
        else:
            os._exit(0)
            
        import resource
        maxfd - resource.getrlimit( resource.RLIMIT_NOFILE )[1]
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
        
        #strategy
        self.run()
        
    
    