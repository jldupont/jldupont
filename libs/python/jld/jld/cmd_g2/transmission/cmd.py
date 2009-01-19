#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

from jld.cmd_g2 import BaseCmd
import jld.tools.printer as printer

try:
    import transmission
except:
    import jld.tools.exceptions as exceptions
    raise exceptions.ErrorMissingDependency('error_missing_dependency', {'location':'pypi','dep':'transmission'} )


class TransmissionCmd(BaseCmd):

    def __init__(self):
        BaseCmd.__init__(self)
        self.config_server = None
        self.config_port   = None
        self.config_syslog = None
        self.config_quiet  = None
        
    def cmd_listconfig(self, *args):
        """Lists the configuration"""       
        return BaseCmd.cmd_listconfig( self, *args )
    
    def cmd_list(self, *args):
        """Lists the current torrents"""
        if self.config_quiet:
            return
        
        c = self._getClient()
        torrents = c.list()
        liste = ListTorrent( torrents )
        
        p = ListPrinter(self.msgs, list=liste.iterlist())
        p.run()


    # =================================
    # PRIVATE
    # =================================

    def _getClient(self):
        return transmission.transmission.Client(address=self.config_server, port=self.config_port)



##################################################################################
##################################################################################



class ListTorrent(object):
    def __init__(self, list):
        self.list = list
        
    def iterlist(self):
        for id, torrent in self.list.iteritems():
            yield str(torrent)
            
    
class ListPrinter(printer.MessagePrinter):
    def __init__(self, msgs, list):
        printer.MessagePrinter.__init__(self, msgs, 'list_', list=list)
        
    def line(self, entry):
        print entry
