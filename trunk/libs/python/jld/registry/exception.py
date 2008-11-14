""" Registry Exception class
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

class RegistryException(Exception):
    """ An exception class for Registry
    """
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)
