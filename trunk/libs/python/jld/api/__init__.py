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
class ErrorGeneric(Exception):
    """ Exception base class which accept parameters.
    """
    def __init__(self, msg, params = None):
        Exception.__init__(self, msg)
        self.msg = msg
        self.params = params
        
class ErrorDb(ErrorGeneric):
    """ Generic Db error e.g. can't open database file
    """

class ErrorNetwork(ErrorGeneric):
    """ Error at the network layer e.g. DNS error, no connection etc. 
    """

class ErrorAuth(ErrorGeneric):
    """ Generic Authentication error
    """

class ErrorAccess(ErrorGeneric):
    """ Generic Access error e.g. restricted access
    """

class ErrorObject(ErrorGeneric):
    """ Generic object error e.g. object not found
    """

class ErrorMethod(ErrorGeneric):
    """ Generic method error e.g. unavailable method for API end-point etc.
    """

class ErrorValidation(ErrorGeneric):
    """ Generic validation error e.g. invalid parameter
    """

class ErrorProperty(ErrorGeneric):
    """ Generic property error e.g. feature X not available
    """

class ErrorProtocol(ErrorGeneric):
    """ Generic protocol error e.g. expecting parameter X but not found
    """

class ErrorInvalidCommand(ErrorGeneric):
    """ Generic command error e.g. invalid command from cmd-line utility 
    """

class ErrorDaemon(ErrorGeneric):
    """ Generic daemon error e.g. can't os.fork
    """

class ErrorConfig(ErrorGeneric):
    """ Generic configuration error e.g. can't load configuration from filesystem
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