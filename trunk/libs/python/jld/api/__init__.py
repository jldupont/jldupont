""" API tools
    @author Jean-Lou Dupont
"""

__version__ = "$Id$"
__author__ = "Jean-Lou Dupont"

import urllib

def alphaOrderParams(liste):
    """ Orders a dictionary based parameters list 
        (e.g. {key:value} ) by alphabetical key order.
        Returns the resulting list
    """
    keys = liste.keys()
    keys.sort()
    result = []
    for key in keys:
        result.append( (key, liste.get(key)) )
    return result


def concatenateParams(liste):
    """Concatenates [ (key,value) ] list
    """
    result = ''
    for key,value in liste:
        result = result + str(key) + str(value)
    
    return result


def formatParams(liste):
    """ Formats the parameters list for usage in an
        HTTP method. Performs URI encoding.
    """     
    return urllib.urlencode( liste, True )


# =========================================================================

class ErrorNetwork(Exception):
    """ Error at the network layer e.g. DNS error, no connection etc. 
    """

class ErrorAuth(Exception):
    """ Generic Authentication error
    """

class ErrorAccess(Exception):
    """ Generic Access error e.g. restricted access
    """

class ErrorObject(Exception):
    """ Generic object error e.g. object not found
    """

class ErrorMethod(Exception):
    """ Generic method error e.g. unavailable method for API end-point etc.
    """

class ErrorValidation(Exception):
    """ Generic validation error e.g. invalid parameter
    """

class ErrorProperty(Exception):
    """ Generic property error e.g. feature X not available
    """

class ErrorProtocol(Exception):
    """ Generic protocol error e.g. expecting parameter X but not found
    """

# =========================================================================

if __name__ == "__main__":
    liste = { 'k2':'v2', 'xyz':'v?xyz', 'abc':'vabc', 'k1':'v1' }
    
    print 'alpha order:'
    sorted_list = alphaOrderParams( liste )
    print sorted_list
    
    print 'concatenate params:'
    print concatenateParams( sorted_list )
    
    print "============"
    print formatParams( sorted_list )