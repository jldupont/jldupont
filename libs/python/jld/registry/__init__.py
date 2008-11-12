""" Cross-platform Registry
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import sys

class Registry(object):
    """Facade for the cross-platform Registry
    """
    reg = None
    
    def __init__(self):
        if (Registry.reg is not None):
            return
        if sys.platform[:3] == 'win':
            from jld.registry.windows import WindowsRegistry 
            Registry.reg = WindowsRegistry()
        else:
            from jld.registry.linux import LinuxRegistry
            Registry.reg = LinuxRegistry()
    
    def getKey(self, file, key):
        """GETS the specified key
            @throws RegistryException
        """
        return Registry.reg.getKey(file, key)
    
    def setKey(self, file, key, value, cond = False):
        """SETS the specified key
            @throws RegistryException
        """      
        return Registry.reg.setKey(file, key, value, cond)
    
# ================================================================================

if __name__=="__main__":
    r = Registry()
    
    print 'GET>>>' + r.getKey('mindmeister', 'secret')
    print 'GET>>>' + r.getKey('mindmeister', 'api_key')
    
    r.setKey('mindmeister', 'test', 'TESTING!')
    
    print 'GET>>>' + r.getKey('mindmeister', 'test')
    
    r.setKey('mindmeister', 'secret', 'SECRET!')

    
