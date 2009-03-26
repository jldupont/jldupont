#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

__all__ = ['isGAEDev','isGAEHosted','isGAE']


import os

_sw  = getattr(os.environ, 'SERVER_SOFTWARE', '')
_dev = _sw.startswith('Dev')
_gae = _sw.startswith('Google')

def isGAEDev():
    return _dev

def isGAEHosted():
    return _gae

def isGAE():
    return _dev or _gae

# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    print "isGAE: [%s]" % isGAE()