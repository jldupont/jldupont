#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

from jld.cmd_g2 import BaseCmd

try:
    import transmission
except:
    import jld.tools.exceptions as exceptions
    raise exceptions.ErrorMissingDependency('error_missing_dependency', {'location':'pypi','dep':'transmission'} )


class TransmissionCmd(BaseCmd):
    """
    """
    def __init__(self):
        BaseCmd.__init__(self)
        self.config_server = None
        self.config_port   = None
        
    def cmd_listconfig(self, *args):
        """Lists the configuration"""
        return BaseCmd.cmd_listconfig( self, *args )
    
    def cmd_list(self, *args):
        """Lists the current torrents"""
        c = self._getClient()
        print c.list()


    def _getClient(self):
        return transmission.transmission.Client(address=self.config_server, port=self.config_port)
    