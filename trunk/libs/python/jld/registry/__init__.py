""" Cross-platform Registry
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import sys
import yaml
import logging
import os.path
from types import *
try:
    import _winreg
except:
    pass

class RegistryError(Exception):
    """ An exception class for Registry
    """
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)
    
"""
class WindowsRegistry(object):
    
    _win = "Software/Python/Registry/%s"

    
    def __init__(self, forceLinux = False):
        self.is_win = (sys.platform[:3] == 'win')
        #for debugging
        if (forceLinux):
            self.is_win = False

        
    def set(self, file, key, value):
        if self.is_win:
            return self._updateWin(file, key, value)
        
        return self._updateLin(file, key, value)
        
    def get(self, file, key):
        if self.is_win:
            return self._getWin(file, key)
        
        return self._getNix(file, key)
            
    def _getWin(self, file, key):
        result = None
        subkey = self._win % file
        try:
            rkey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, subkey, 0, _winreg.KEY_READ)
            (value, valuetype) = _winreg.QueryValueEx(rkey, key)
            result = value
        except:
            #the key does not exist yet, probably
            logging.warn('Python Registry: key [%s] file[%s] does not exist' % (key, file))
            return result
        
        return result

    def _updateWin(self, file, key, value):
        try:
            subkey = self._win % file
            ckey = _winreg.CreateKey( _winreg.HKEY_LOCAL_MACHINE, subkey)
            _winreg.SetValueEx(ckey, key, 0, _winreg.REG_SZ, value)           
        except Exception,e:
            logging.error("Python Registry: write error key[%s] file[%s] exception msg{%s}" %(key, file,e))
""" 


class LinuxRegistry(object):
    
    _lin  = "/etc/python/registry/%s"
    
    _lind = "c:\\etc\\python\\registry\\%s"
        
    def __init__(self, debug = False):
        self._debug = debug
        
    def getKey(self, file, key):
        content = self._load(file)
        if (content is None):
            return None
        try:
            d = yaml.load( content )
        except:
            raise RegistryError('LinuxRegistry: error parsing YAML from file[%s]' % file)
        
        return self._extractKey(d, key)

    def _extractKey(self, obj, key):
        if (type(obj) is ListType ):
            for i in obj:
                if (type(i) == 'dict'):
                    found = False
                    try:
                        value = i[key]
                        found = True
                    except:
                        pass
                    if (found):
                        return value
                    
        if (type(obj) is DictType):
            try:
                return obj[key]
            except:
                return None
            
        return None
            
    
    def setKey(self, file, key, value):
        content = self._load(file)
        if (content is not None):
            d = yaml.load( content )
            d[key] = value
        else:
            d = {key:value}

        self._save(file, yaml.dump(d) )
        
    def _load(self, file):
        result = None
        path = self._getPath(file)
            
        if (not os.path.exists(path) or not os.path.isfile(path)):
            return result
        try:
            infile = open(path,'r')
            result = infile.readlines()
        except:
            logging.warn('LinuxRegistry: error loading file[%s]' % file)
        finally:
            infile.close()
            
        return result
        
    def _save(self, file, content):
        self._prepareDir()
        path = self._getPath(file)
        try:
            outfile = open(path, 'w')
            outfile.write(content)
            outfile.close()            
        except:
            raise RegistryError('LinuxRegistry: error writing file[%s]' % path)
         
    def _getPath(self, file, trim = False):
        if (self._debug):
            path = self._lind % file
        else:
            path = self._lin % file
        #useful during debugging
        if (trim):
            path.rstrip( os.sep )
        return path

    def _prepareDir(self):
        """Creates the registry directory if it does not already exists
        """
        path = self._getPath("", trim=True)
        if (os.path.isdir(path)):
            return
        
        bits = path.split( os.sep )

        spath = bits.pop(0)
        bit = bits.pop(0)
        while bit is not None:
            spath = spath + os.sep + bit
            if ( not os.path.isdir(spath) ):
                os.mkdir( spath )
            try:
                bit = bits.pop(0)
            except:
                bit = None

# ================================================================================

if __name__=="__main__":
    r = LinuxRegistry(True)
    
    print r.getKey('mindmeister', 'secret')
    
    r.setKey('mindmeister', 'secret', 'SECRET')
    
    print r.getKey('mindmeister', 'secret')