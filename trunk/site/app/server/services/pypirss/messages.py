#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""
from string import Template

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

__all__ = ['prepareMessage',]

_messages = {
'error_package_not_found':'',
'error_package_releases':'',
'error_package_release_data_datastore_access':'',
'error_package_release_data':'',
'error_package_release_data_downloads':'',             
}


_message_template = """

"""

_template = Template( _message_template )

def prepareMessage(msg_id, params):
    """ Prepares a message.
    """
    params['msg'] = _messages[msg_id]
    return _template.substitute(params)