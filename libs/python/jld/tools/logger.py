#! /usr/bin/env python
""" Cross-platform logger
    @author: Jean-Lou Dupont
    
    XXX not tested thoroughly... do not use!
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import sys
import logging
import logging.handlers

def logger( name ):
    """ Returns a simple cross-platform logger
        E.g.
        log = logger.logger('my_logger')
        log.info('message')
    """
    handler = xcLogger( name )
    _logger = logging.Logger( name )
    _logger.addHandler( handler )
    return _logger

def xcLogger( appname ):
    """ Cross-platform log handler
        Returns a NTEventLogHandler for win32 platform
        Returns a SysLogHandler for *nix platform
    """
    if (sys.platform[:3] == 'win'):
        return logging.handlers.NTEventLogHandler( appname )
    
    return logging.handlers.SysLogHandler('/dev/log')

    #More difficult to configure as it defaults to localhost:514 
    #return logging.handlers.SysLogHandler()         

# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    import logging
    
    handler = xcLogger('Test_xcLogger')
    logger = logging.Logger('Test_xcLogger')
    logger.addHandler( handler )
    
    logger.info( 'xcLogger -- TestMessage' )
    