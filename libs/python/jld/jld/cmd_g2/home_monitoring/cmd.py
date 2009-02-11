#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import os

from   jld.cmd_g2 import BaseCmd

# imports are checked & errors raised later
try:
    import Phidgets
except:
    pass
        

class HomeMonCmd(BaseCmd):

    def __init__(self):
        BaseCmd.__init__(self)
        self.config_syslog = None
        
        self._checkDependencies()


    # =================================
    # PRIVATE
    # =================================
    
    def _checkDependencies(self):
        if "Phidgets" not in globals():
            import jld.tools.exceptions as exceptions
            raise exceptions.ErrorMissingDependency('error_missing_dependency', {'location':'http://www.phidgets.com/','dep':'Phidgets'} )                   



##################################################################################
##################################################################################



