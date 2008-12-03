""" Cross-platform Registry
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import sys

class Registry(object):
    """Facade for the cross-platform Registry
        Can be accessed like a dictionary: for this
        functionality, an instance must be constructed
        with the 'file' parameter specified.
    """
    reg = None
    
    def __init__(self, file = None):
        self.file = file
        
        if (Registry.reg is not None):
            return
        if sys.platform[:3] == 'win':
            from jld.registry.windows import WindowsRegistry 
            Registry.reg = WindowsRegistry(file)
        else:
            from jld.registry.linux import LinuxRegistry
            Registry.reg = LinuxRegistry(file)
    
    def getKey(self, file, key):
        """GETS the specified key
            @throws RegistryException
        """
        return Registry.reg.getKey(file, key)
    
    def setKey(self, file, key, value, cond = False):
        """SETS the specified key
            @throws RegistryException
        """
        if (cond):
            if (value is None):
                #print "skipping key[%s]" % key
                return
        return Registry.reg.setKey(file, key, value)
    
    # DICTIONARY INTERFACE
    # ====================
    
    def __getitem__(self, key):
        return Registry.reg[key]
    
    def __setitem__(self, key, value):
        Registry.reg[key] = value
    
    def __contains__(self, key):
        return (key in Registry.reg)
        
# ================================================================================

if __name__=="__main__":
    r = Registry()
    
    print 'GET>>>' + r.getKey('mindmeister', 'secret')
    print 'GET>>>' + r.getKey('mindmeister', 'api_key')
    
    r.setKey('mindmeister', 'test', 'TESTING!')
    
    print 'GET>>>' + r.getKey('mindmeister', 'test')
    
    r.setKey('mindmeister', 'secret', 'SECRET!')

    
