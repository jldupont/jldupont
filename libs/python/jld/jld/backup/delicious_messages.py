""" Messages interface for Delicious Backup
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import os
from jld.tools.messages import Messages

class Delicious_Messages(Messages):
    
    filepath = os.path.dirname( os.path.abspath( __file__ )) + os.sep + "delicious_messages.yaml"
    
    def __init__(self):
        Messages.__init__(self, self.filepath)
