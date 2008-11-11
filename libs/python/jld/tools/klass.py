"""
    @author: Jean-Lou Dupont
"""
__author__   = "Jean-Lou Dupont"
__version__  = "$Id$"

import inspect
from types import *

def searchForMethods(obj, prefix, stripPrefix = True):
    """Search for all methods with starting prefix. Returns a list of tuples (method_name, doc_string)
    """
    methods = inspect.getmembers(obj, lambda X:type(X) is MethodType)
    
    _liste = []  ;  _matches = []
    
    for method in methods:
        _name = str( method[0] )
        _type = method[1]
        
        if (_name.startswith(prefix)):
            if (stripPrefix):
                _name = _name[len(prefix):]
            _liste.append( (_name, inspect.getdoc(method[1]) ) )
            _matches.append( _name )
            
    return (_matches, _liste)

# =========================================================


if __name__ == "__main__":
    
    class X(object):
        def cmd_C1(self):
            """Command C1"""
            pass
        def cmd_C2(self):
            """Command C2"""
            pass
        def other(self):
            pass
        
    print searchForMethods(X, 'cmd_')
    x = X()
    print searchForMethods(x, 'cmd_')