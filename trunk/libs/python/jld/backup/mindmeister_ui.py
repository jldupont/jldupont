""" MindMeister User Interface
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

class MM_UI(object):
    """ Handles user interface
    """
    def __init__(self):
        pass
    
    def setParams(self, params):
        """ Generic parameter setting interface
        """

    def handleError( self, code, msg ):
        """ Displays, if required, an appropriate user message
            corresponding to an error condition.
            Also generates logging and/or email messages as appropriate.
        """

# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
