#! /usr/bin/env python
""" Cross-platform
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import sys
import logging.handlers

def xcLogger( appname ):
    """ Cross-platform log handler
        Returns a NTEventLogHandler for win32 platform
        Returns a SysLogHandler for *nix platform
    """
    if (sys.platform[:3] == 'win'):
        return logging.handlers.NTEventLogHandler( appname )
    
    return logging.handlers.SysLogHandler() 
        

# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    import logging
    
    handler = xcLogger('Test_xcLogger')
    logger = logging.Logger('Test_xcLogger')
    logger.addHandler( handler )
    
    logger.info( 'TestMessage' )
    