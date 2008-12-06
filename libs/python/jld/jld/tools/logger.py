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

def logger( name, include_console = True ):
    """ Returns a simple cross-platform logger
        E.g.
        log = logger.logger('my_logger')
        log.info('message')
    """
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s %(name)-12s %(levelname)-8s: %(message)s ",
                        )        
        
    formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s: %(message)s ")
    handler = xcLogger( name )
    handler.setFormatter(formatter)
    _logger = logging.getLogger(name)
    _logger.addHandler(handler)
    if include_console:
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        _logger.addHandler(console)

    return _logger

def xcLogger( appname ):
    """ Cross-platform log handler
        Returns a NTEventLogHandler for win32 platform
        Returns a SysLogHandler for *nix platform
    """
    if (sys.platform[:3] == 'win'):
        return logging.handlers.NTEventLogHandler( appname )
    
    return logging.handlers.SysLogHandler('/dev/log/%s.log' % appname )

    #More difficult to configure as it defaults to localhost:514 
    #return logging.handlers.SysLogHandler()         

# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    log = logger('Test_xcLogger', True)
    
    log.info( 'TestMessage' )
    