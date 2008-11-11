""" Windows Registry
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import sys
import yaml
import os.path
#import logging
from types import *
import _winreg

from jld.registry.exception import RegistryException

class WindowsRegistry(object):
    
    _win = "Software\\Python\\Registry\\%s"

    def getKey(self, file, key):

        result = None
        subkey = self._win % file
        try:
            rkey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, subkey, 0, _winreg.KEY_READ)
            (value, valuetype) = _winreg.QueryValueEx(rkey, key)
            result = value
        except:
            #the key does not exist yet, probably
            #logging.warn('Python Registry: key [%s] file[%s] does not exist' % (key, file))
            return result
        
        return result

    def setKey(self, file, key, value, cond=False):
        #print "WindowsRegistry.setKey file[%s] key[%s] value[%s]" % (file, key, value)
        if (cond):
            if (value is None):
                return
     
        try:
            subkey = self._win % file
            ckey = _winreg.CreateKey( _winreg.HKEY_LOCAL_MACHINE, subkey)
            _winreg.SetValueEx(ckey, key, 0, _winreg.REG_SZ, value)           
        except Exception,e:
            raise RegistryException("Python Registry: write error key[%s] file[%s] exception msg{%s}" %(key, file,e))
        
        
if __name__ == "__main__":
    r2 = WindowsRegistry()
    print r2.getKey('mindmeister', 'secret')
    
    r2.setKey('mindmeister', 'secret', 'SECRET!')
    print r2.getKey('mindmeister', 'secret')
