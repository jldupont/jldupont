#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"


class deco(object):
    
    def __init__(self, *params):
        """ Grab the parameters to the decorator here
        """
        #print "__init__ params[%s]" % params
        self.params = params

    def __call__(self, func):
        """ Grab the function to decorate here
        """
        self.original_func = func
        #print "in-call func[%s]" % func
        return self.new_func
    
    def new_func(self, *args):
        from_orig = self.original_func( *args )
        return "from new_func params[%s] args[%s]" % (self.params, args) 
    

@deco('param1')
def test(*args):
    return "in-test %s" % args


class Tests():
    """
    >>> result = test("p2")
    >>> print result
    in-test
    """

# ==============================================
# ==============================================

if __name__ == "__main__":
    import doctest
    doctest.testmod()#verbose=True, report=True)
