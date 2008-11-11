""" Specialized String Template
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

from string import Template

class ExTemplate(Template):
    """String Template to ease integration with other string processing modules e.g. OptionParser
    """
    
    # must appear here to shadow the base class
    delimiter = '^^'
    
    def __init__(self, init):
        Template.__init__(self, init)
