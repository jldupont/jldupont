#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

class deco(object):
    
    def __init__(self, *pargs, **kargs):
        """ Grab the parameters to the decorator here
        """
        print "deco.__init__ pargs[%s] kargs[%s]" % (pargs, kargs)        

    def __call__(self, *pargs, **kargs):
        """ Grab the function to decorate here
        """
        func = pargs[0]
        print "deco.__call__ pargs[%s] kargs[%s]" % (pargs, kargs)
        
        def new_func( *pnargs, **knargs):
            """ Grab the the target's "self" parameter as pnargs[0]
            """
            this = pnargs[0]
            #print "new_func:  this.param[%s] pnargs[%s] knargs[%s]" % (this.param, pnargs, knargs)
            print "new_func: this.param[%s]" % this.param
            return func(*pnargs, **knargs)
            
        return new_func        


class Test(object):
    
    def __init__(self, param):
        self.param = param
        
    def __call__(self, *pargs, **kargs):
        print "Test.__call__ pargs[%s] kargs[%s]" % (pargs, kargs)
    
    @deco('deco-to-func1')
    def func1(self, *pargs, **kargs):
        print "Test.func1: pargs[%s] kargs[%s] param[%s]" % (pargs, kargs, self.param)

    @deco('deco-to-func2')
    def func2(self, *pargs, **kargs):
        print "Test.func2: pargs[%s] kargs[%s] param[%s]" % (pargs, kargs, self.param)

def tests():
    """

>>> t= Test("param1")
>>> t.func1("fnc1.param")
new_func: this.param[param1]
Test.func1: pargs[('fnc1.param',)] kargs[{}] param[param1]
>>> t.func2("fnc2.param")
new_func: this.param[param1]
Test.func2: pargs[('fnc2.param',)] kargs[{}] param[param1]
"""

# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    import doctest
    doctest.testmod()
