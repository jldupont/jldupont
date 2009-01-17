#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

class GChart(object):
    ""
    _api = "http://chart.apis.google.com/chart?"
    
    def __str__(self):
        ""
        

class BarChart(GChart):
    ""
    def __init__(self, **kwargs):
        GChart.__init__(self)
        
        


# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    import doctest
    doctest.testmod()
