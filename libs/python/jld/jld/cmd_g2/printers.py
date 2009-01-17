#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"


import jld.tools.printer as printer

class MessagePrinter(BasePrettyPrinter):

    def __init__(self, msgs, msgs_prefix = ''):
        BasePrettyPrinter.__init__(self)
        self.msgs = msgs
        self.msgs_prefix = msgs_prefix

    def header(self):
        """Prints a header"""
        key = self.msgs_prefix + 'header'
        print self.msgs.render(key)
        
    def table_header(self, tpl_item = None):
        """Prints a table header"""
        key = self.msgs_prefix + 'tableheader'
        print self.msgs.render(key)
    
    def footer(self):
        """Prints a footer"""
        key = self.msgs_prefix + 'footer'
        print self.msgs.render(key)
    

class PrinterConfig(MessagePrinter):

    def __init__(self, msgs):
        MessagePrinter.__init__(self, msgs)
       
    def line(self, entry):
        """Prints one line"""
        print "%s: %s" % (entry[0], entry[1])

    def _processList(self, list):
        return self._dictToList( list )
