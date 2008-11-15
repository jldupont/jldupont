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
    
    def __init__(self, level):
        """ Initialize a platform dependent logger
        """
        if (self._platform_win32):
            self._logger = _winLogger(level)
        else:
            self._logger = _nixLogger(level) 

# ==============================================
# ==============================================
class _baseLogger(object):
    """
    """

# ==============================================
# ==============================================
class _winLogger(_baseLogger):
    """ Win32 logger class
    """
    def __init__(self,level):
        """
        """
# ==============================================
# ==============================================
class _nixLogger(_baseLogger):
    """ *nix logger class
    """
    def __init__(self,level):
        """
        """

# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
