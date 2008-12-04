"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import os
import jld.tools.defaults as Defaults

class MM_Defaults(Defaults.Defaults):
    _path = os.path.dirname(__file__)+os.sep+'mindmeister_defaults.yaml'

    def __init__(self):
        Defaults.Defaults.__init__(self)
        
# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    d = MM_Defaults()
    
    print d.defaults