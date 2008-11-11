"""
    @author: Jean-Lou Dupont
"""
__author__   = "Jean-Lou Dupont"
__version__  = "$Id$"

import inspect

def searchForMethods(obj, prefix):
    """Search for all methods with starting prefix
    """
    methods = inspect.getmembers(obj)
    
    liste = []
    for method in methods:
        name = str( method[0] )
        type = str( method[1] )
        if (type.find('bound method') or type.find('unbound method')):
            if (name.startswith(prefix)):
                liste.append( name )
            
    return liste


if __name__ == "__main__":
    
    class X(object):
        def cmd_C1(self):
            pass
        def cmd_C2(self):
            pass
        def other(self):
            pass
        
    print searchForMethods(X, 'cmd_')
    x = X()
    print searchForMethods(x, 'cmd_')