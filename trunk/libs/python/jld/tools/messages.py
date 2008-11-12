""" Messages interface
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import yaml
import os.path
import sys
from string import Template

class Messages(object):
    
    def __init__(self, path):
        """path: filesystem path to YAML messages
        """
        self.filepath = path
        self.msgs = None
    
    def _load(self):
        """ Loads the messages from the filesystem
        """
        file = open(self.filepath,'r')
        self.msgs  = yaml.load(file)
        file.close()
        
    def __getitem__(self, key):
        if (self.msgs is None):
            self._load()
        return self.msgs[key]
    
    def render(self, key, params):
        msg = self[key]
        tpl = Template(msg)
        return tpl.substitute( params )
    
if __name__ == "__main__":

    path = os.path.dirname(__file__) + os.sep + 'messages.yaml'
    msg = Messages(path)
    
    params = {'msg':'message'}
    print msg.render( 'msg1', params )
     