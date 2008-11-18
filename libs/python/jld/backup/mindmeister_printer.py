""" MindMeister Maps list pretty printer
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import jld.tools.printer as printer

class MM_Printer(printer.BasePrettyPrinter):

    _fields = [ 'mapid', 'title' ]

    def __init__(self, msgs):
        printer.BasePrettyPrinter.__init__(self)
        self.msgs = msgs

    def header(self):
        """Prints a header"""
        print self.msgs.render( 'tbl_header' )
        
    def table_header(self, tpl_item = None):
        """Prints a table header"""
        result = ''
        for field in self._fields:
            result = result + field + ' , '
        
        print '==='    
        print result.rstrip(' ,')
        print '==='
    
    def footer(self):
        """Prints a footer"""
        print self.msgs.render( 'tbl_footer' )
    
    def line(self, entry):
        """Prints one line"""
        result = ''
        for field in self._fields:
            result = result + entry[field] + ' , '
            
        print result.rstrip(' ,') 
            


# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
