#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"


def formatSqliteURI( path ):
    """ Formats a filesystem path
        to a valid Sqlite URI.
        Under Windows, the backward slash \
        must be replaced with forward slash /
        as well as replacing the semicolon :
        to a pipe character |.
        For a complete URI, just prepend sqlite:///
    """
    return  path.replace('\\','/').replace(':','|')

