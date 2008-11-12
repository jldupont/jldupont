""" Messages interface for MindMeister
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import yaml
import os.path
import sys
from jld.tools.messages import Messages

class MM_Messages(Messages):
    
    filepath = "mindmeister_messages.yaml"
    
    def __init__(self):
        Messages.__init__(self, self.filepath)
