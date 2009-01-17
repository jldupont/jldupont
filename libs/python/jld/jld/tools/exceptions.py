#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

class ErrorMissingDependency(Exception):
    def __init__(self, msg, params = None):
        Exception.__init__(self, msg)
        self.msg = msg
        self.params = params
