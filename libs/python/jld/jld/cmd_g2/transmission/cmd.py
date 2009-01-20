#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

from jld.cmd_g2 import BaseCmd
import jld.tools.printer as printer

# imports are checked & errors raised later
try:
    import transmission
except:
    pass
        

class TransmissionCmd(BaseCmd):

    def __init__(self):
        BaseCmd.__init__(self)
        self.config_server = None
        self.config_port   = None
        self.config_syslog = None
        self.config_quiet  = None
        
        self._checkDependencies()

    def cmd_listconfig(self, *args):
        """Lists the configuration"""       
        msg = BaseCmd.cmd_listconfig( self, *args )
        print msg
    
    @printer.condprinter('config_quiet')
    def cmd_list(self, *args):
        """Lists the current torrents"""
        
        c = self._getClient()
        torrents = c.list()
        liste = ListTorrent( torrents )
        
        p = ListPrinter(self.msgs, list=liste.iterlist())
        return p.run()

    @printer.condprinter('config_quiet')
    def cmd_reportstatus(self, *args):
        """Reports on the current status of the active torrents"""
        
        client  = self._getClient()
        torrents= client.list()
        session = client.get_session()
        dld     = session.fields['download_dir']
        


    # =================================
    # PRIVATE
    # =================================
    def _checkDependencies(self):
        if "transmission" not in globals():
            import jld.tools.exceptions as exceptions
            raise exceptions.ErrorMissingDependency('error_missing_dependency', {'location':'pypi','dep':'transmission'} )                   

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
        self.buffer =  self.buffer + entry + "\n"
