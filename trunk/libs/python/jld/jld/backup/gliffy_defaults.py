""" Gliffy Backup utility
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import os
import jld.tools.defaults as Defaults

class Gliffy_Defaults(Defaults.Defaults):
    _path = os.path.dirname(__file__)+os.sep+'gliffy_defaults.yaml'

    def __init__(self):
        Defaults.Defaults.__init__(self)
