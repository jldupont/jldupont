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

"""
wiring = [('setOnAttachHandler',        'ikit_attach'),
              ('setOnDetachHandler',        'ikit_detach'),
              ('setOnErrorhandler',         'ikit_error'),
              ('setOnInputChangeHandler',   'ikit_input'),
              ('setOnOutputChangeHandler',  'ikit_output'),
              ('setOnSensorChangeHandler',  'ikit_sensor')]
"""

_transition_table = {
    ():'',
    ():'',
}

