"""
    Cross-platform logger
    @author: Jean-Lou Dupont
    
    *nix system:  uses SysLog
    NT/Win32:     uses EventLog
    
    import logging
    import logging.handlers
    
    logger = logging.getLogger('MyLogger')
    handler = logging.handlers.NTEventLogHandler('MyLogger')
    logger.addHandler(handler)
    
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import sys
import logging, logging.handlers

class ExLogger(object):
    """ Facade class 
    """
    __slots__ = [ '_logger' ]
    _platform_win32 = sys.platform[:3] == 'win' 
    _platform_nix   = sys.platform[:3] != 'win'  #shortcut
    
    def __init__(self):
        """ Initialize a platform dependent logger
        """
        if (self._platform_win32):
            self._logger = _winLogger()
        else:
            self._logger = _nixLogger() 

# ==============================================
# ==============================================
class _winLogger(object):
    """ Win32 logger class
    """
# ==============================================
# ==============================================
class _nixLogger(object):
    """ *nix logger class
    """


# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
