""" Pretty Printer
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

from types import *

class BasePrettyPrinter(object):
    """Generic Pretty Printer"""

    def __init__(self):
        self.tbl_hdr = None #cached table header

    def header(self):
        """Prints a header"""
        
    def table_header(self, tpl_item = None):
        """Prints a table header"""
    
    def footer(self):
        """Prints a footer"""
    
    def line(self, entry):
        """Prints one line"""
    
    def run(self, list, page_len = 20, repeat_table_header = True):
        """Default (basic) printer implementation"""
        list = self._processList(list)
        self.header()
        count = 0
        for item in list:
            if (not count):
                count = page_len
                self.table_header( item )
            self.line(item)
            count = count - 1
        self.footer()

    def _dictToList(self, dic):
        ""
        list = []
        for k,v in dic.items():
            list.append( (k,v) )
        return sorted( list )

    def _processList(self, list):
        """Override this"""
        return list

# ==================================================================

class SimplePrettyPrinter(BasePrettyPrinter):
    """Simple Printer which uses stdout"""

    def table_header(self, item_tpl):
        """Prints a table header"""
        if (self.tbl_hdr):
            print self.tbl_hdr
            return
        
        self.tbl_hdr = ''
        keys = item_tpl.keys()
        for key in keys:
            self.tbl_hdr = self.tbl_hdr + str(key) + ' , '

        self.tbl_hdr = self.tbl_hdr.rstrip(" ,")
        print self.tbl_hdr
        print "--" 
    
    def line(self, entry):
        """Prints one line"""
        result = ''
        for item in entry:
            result = result + entry[item] + ' , '
            
        print result.rstrip(' ,')


class MessagePrinter(BasePrettyPrinter):

    def __init__(self, msgs, msgs_prefix = ''):
        BasePrettyPrinter.__init__(self)
        self.msgs = msgs
        self.msgs_prefix = msgs_prefix

    def _get_msg(self, key):
        if type(self.msgs) is DictType:
            return self.msgs[key]
        
        return self.msgs.render(key)

    def header(self):
        """Prints a header"""
        key = self.msgs_prefix + 'header'
        print self._get_msg(key)
        
    def table_header(self, tpl_item = None):
        """Prints a table header"""
        key = self.msgs_prefix + 'tableheader'
        print self._get_msg(key)
    
    def footer(self):
        """Prints a footer"""
        key = self.msgs_prefix + 'footer'
        print self._get_msg(key)
    

class PrinterConfig(MessagePrinter):

    def __init__(self, msgs, msgs_prefix = "config_" ):
        MessagePrinter.__init__(self, msgs, msgs_prefix)
       
    def line(self, entry):
        """Prints one line"""
        print "%s: %s" % (entry[0], entry[1])

    #def _processList(self, list):
    #    return self._dictToList(list)
    
# ==============================================
# ==============================================

if __name__ == "__main__":
    def tests(self):
        """
>>> msgs = {'config_header':'Header', 'config_footer': 'Footer', 'config_tableheader':'Table Header'}
>>> configs = { 'key1':'value1', 'key2':'value2' }
>>> p = PrinterConfig(msgs)
>>> p.run(configs)
Header
Table Header
key1: value1
key2: value2
Footer"""
    
    import doctest
    doctest.testmod()
