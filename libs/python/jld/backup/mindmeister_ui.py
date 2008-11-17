""" MindMeister User Interface
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

class MM_UI(object):
    """ Handles user interface
    """
    def __init__(self):
        self.msgs = None
        self.params = {}
    
    def setParams(self, msgs, params):
        """ Generic parameter setting interface
        """
        self.msgs = msgs
        self.params = params

    def handleError( self, exc ):
        """ Displays, if required, an appropriate user message
            corresponding to an error condition.
            Also generates logging and/or email messages as appropriate.
        """

# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
