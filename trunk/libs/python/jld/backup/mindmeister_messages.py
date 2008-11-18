""" Messages interface for MindMeister
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import os.path
from jld.tools.messages import Messages

class MM_Messages(Messages):
    
    filepath = os.path.dirname( os.path.abspath( __file__ )) + os.sep + "mindmeister_messages.yaml"
    
    def __init__(self):
        Messages.__init__(self, self.filepath)
