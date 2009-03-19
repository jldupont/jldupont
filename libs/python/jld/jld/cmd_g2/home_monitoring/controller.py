#!/usr/bin/env python
""" Controller class for home_monitoring

    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import sys

try:
    import pyfse
except:
    raise RuntimeError( "homemon: requires package 'pyfse'. This package can be obtained @ Pypi (easy_install pyfse)" )
    

__all__ = ['HomeMonController',]


class HomeMonController(Controller):
    def __init__(self, table):
        Controller.__init__(self, table)


_transistion_table = {
    ():'',
    ():'',
}

