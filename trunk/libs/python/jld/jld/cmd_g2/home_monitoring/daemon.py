#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

from Phidgets.PhidgetException import *
from Phidgets.Events.Events import *
from Phidgets.Devices.InterfaceKit import *


import jld.tools.daemon as daemon

# - Receive config
# - Open device
# -- Wait for attach
# - Loop
# - Lookup event
# - Write event to log

class HomeMonDaemon(daemon.BaseDaemon):
    """ Serves one device
    """
    def __init__(self):
        daemon.BaseDaemon.__init__(self)
        self.ikit = None
        
        self.deviceName = None
    
    def run(self):
        ""
        self.init()

    def init(self):
        """ Init 
        """
        try:
            self.ikit = InterfaceKit()
            
            self.ikit .setOnAttachHandler(self.inferfaceKitAttached)
            self.ikit .setOnDetachHandler(self.interfaceKitDetached)
            self.ikit .setOnErrorhandler(self.interfaceKitError)
            self.ikit .setOnInputChangeHandler(self.interfaceKitInputChanged)
            self.ikit .setOnOutputChangeHandler(self.interfaceKitOutputChanged)
            self.ikit .setOnSensorChangeHandler(self.interfaceKitSensorChanged)
        except Exception,e:
            pass
        
    #=========================
    # interface kit callbacks
    #=========================
    def interfaceKitAttached(self):
        """ """
    def interfaceKitDetached(self):
        """ """
    def interfaceKitError(self):
        """ """
    def interfaceKitInputChanged(self):
        """ """
    def interfaceKitOutputChanged(self):
        """ """
    def interfaceKitSensorChanged(self):
        """ """
        

    def loop(self):
        ""