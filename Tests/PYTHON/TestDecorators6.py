#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

class deco(object):
    
    def __init__(self, *pargs, **kargs):
        print "deco.__init__ pargs[%s] kargs[%s]" % (pargs, kargs)        

    @classmethod
    def __call__(cls, *pargs, **kargs):
        """ Grab the function to decorate here
        """
        func = pargs[0]
        print "deco.__call__ pargs[%s] kargs[%s]" % (pargs, kargs)
        
        def new_func(*pnargs, **knargs):
            ""
            print "new_func:  pnargs[%s] knargs[%s]" % (pnargs, knargs)
            return func(*pnargs, **knargs)
            
        return new_func        


class Test(object):
    
    def __init__(self, param):
        self.param = param
        
    def __call__(self, *pargs, **kargs):
        print "Test.__call__ pargs[%s] kargs[%s]" % (pargs, kargs)
    
    @deco()
    def func1(self, *pargs, **kargs):
        print "Test.func1: pargs[%s] kargs[%s] param[%s]" % (pargs, kargs, self.param)

    @deco()
    def func2(self, *pargs, **kargs):
        print "Test.func2: pargs[%s] kargs[%s] param[%s]" % (pargs, kargs, self.param)

def tests():
    """
    >>> t= Test("param1")
    >>> t.func1("fnc1.param")
    >>> t.func2("fnc2.param")
    """

# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    import doctest
    doctest.testmod()
