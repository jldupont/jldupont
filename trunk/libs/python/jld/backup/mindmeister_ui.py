""" MindMeister User Interface
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import re
import sys
import jld.api as api
import jld.registry as reg
import jld.tools.cmd_ui as ui

class MM_UI(ui.UIBase):
    """ Handles user interface
    """
    _map = {
        'ErrorNetwork':     { 'msg': 'error_network',   'help':'', },
        'ErrorAccess':      { 'msg': 'error_access',    'help':'', },
        'ErrorObject':      { 'msg': 'error_object',    'help':'', },
        'ErrorMethod':      { 'msg': 'error_method',    'help':'', },
        'ErrorValidation':  { 'msg': 'error_validation','help':'', },
        'ErrorProperty':    { 'msg': 'error_property',  'help':'', },
        'ErrorProtocol':    { 'msg': 'error_protocol',  'help':'', },
        'RegistryException':{ 'msg': 'error_registry',  'help':'', },
    }
    
    def __init__(self):
        UIBase.__init__(self)


# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
