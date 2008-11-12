""" Messages interface for MindMeister
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import yaml
import os.path
import sys

class MM_Messages(object):
    
    filepath = "mindmeister_messages.yaml"
    
    def __init__(self):
        self.msgs = None
    
    def _load(self):
        """ Loads the messages from the filesystem
        """
        path = os.dirname( os.abspath(__file__) ).join(os.sep).self.filepath
        file = open(path,'r')
        self.msgs  = yaml.load(file)
        file.close()
        
    def __getitem(self, key):
        if (self.msgs is None):
            self._load()
        return self.msgs[key] 