#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

__all__ = ['messages','message_template']

from string import Template

# MESSAGES
# ========
messages = {
'error_package_not_found':'Package [$name] was not found',
'error_package_releases':'No release for package [$name]',
'error_package_release_data_datastore_access':'Error accessing the datastore',
'error_package_release_data':'Error accessing package release data',
'error_package_release_data_downloads':'Error accessing "downloads" attribute from package[$name]',
}


# BASE PAGE TEMPLATE
# ==================
message_template = """
<html>
 <body>
  <b>ERROR:</b> $msg
 </body>
</html> 
"""