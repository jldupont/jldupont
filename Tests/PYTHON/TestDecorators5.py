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
        print "__init__ pargs[%s] kargs[%s]" % (pargs, kargs)
        self.pargs = pargs
        self.kargs = kargs

    def __call__(self, *pargs, **kargs):
        """ Grab the function to decorate here
        """
        print "__call__ pargs[%s] kargs[%s]" % (pargs, kargs)
        self.original_func = pargs[0]
        return self.new_func
    
    def new_func(self, *pargs, **kargs):
        """ Acts pretty much as a function replacement
        """
        print "new_func: pargs[%s] kargs[%s]" % (pargs, kargs)
        from_orig = self.original_func( self, *pargs, **kargs )
        return "from new_func self.pargs[%s] self.kargs[%s] pargs[%s] kargs[%s]" % (self.pargs, self.kargs, pargs, kargs) 
    
class Foo(object):
    
    @deco('deco-param1')
    def fnc1(self):
        print "in: Foo:fnc1"


class Tests():
    """
    >>> f = Foo()
    >>> f.fnc1()
    """

# ==============================================
# ==============================================

if __name__ == "__main__":
    import doctest
    doctest.testmod()#verbose=True, report=True)
