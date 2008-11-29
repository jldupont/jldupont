""" Defaults
    Provides default configuration interface
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import yaml
import os.path
import sys
from string import Template

class Defaults(object):
    """
    """
    def __init__(self, filepath):
        self.filepath = filepath
        self.defaults = None
        
    def _load(self):
        try:
            file = open(self.filepath,'r')
            self.defaults = yaml.load(file)
            file.close()
        except Exception,e:
            pass
        