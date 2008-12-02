""" API tools
    @author Jean-Lou Dupont
"""

__version__ = "$Id$"
__author__ = "Jean-Lou Dupont"

import urllib
from types import *

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

def makeList(liste):
    """ Makes an url encoded list
        item1+item2+...
    """
    result = ''
    for item in liste:
        result = result + urllib.quote( item ) + '+'
        
    return result.rstrip('+')
 
def formatParams(liste):
    """ Formats the parameters list for usage in an
        HTTP method. Performs URI encoding.
    """     
    return urllib.urlencode( liste, True )

def versaUrlEncode(liste, RemoveNone = False):
    """ Cases:
        a) 'key'
        b) ('key', 'value')
        c) ('key', [ value list ] )
        d) { 'key1': 'value1', 'key2':['v1', 'v2'] }
    """
    result = ''
    if (type(liste) is DictType):
        keys = liste.keys()
        for key in keys:
            
            right_side = liste[key]
            
            #key
            if (type(right_side) is NoneType):              
                if (not RemoveNone):
                    result = result + urllib.quote( key )
                    result = result + '&'
                continue

            result = result + urllib.quote( key )
            
            #key=int value
            if (type(right_side) is IntType):
                result = result + '=' + str( liste[key] ) + '&'
                continue
            
            #key=value
            if (type(right_side) is StringType):
                result = result + '=' + urllib.quote(liste[key]) + '&'
                continue
            
            #key=[]
            if (type(right_side) is ListType):
                result = result + '=' + makeList( liste[key] ) + '&'
                continue
                
        return result.rstrip('&')
    
    for item in liste:
        if (type(item) is StringType):
            result = result + urllib.quote( str(item) )
        
        if (type(item) is TupleType):
            assert( type(item[0]) is StringType )
            result = result + urllib.quote( str( item[0] ) ) + "="
            if (type(item[1]) is ListType):
                result = result + makeList( item[1] )
            else:
                assert( type(item[1]) is StringType )
                result = result + urllib.quote( item[1] )
                       
        result = result + '&'
        
    return result.rstrip('&')
            

# =========================================================================
class ErrorGeneric(Exception):
    """ Exception base class which accept parameters.
    """
    def __init__(self, msg, params = None):
        Exception.__init__(self, msg)
        self.msg = msg
        self.params = params
        
class ErrorFile(ErrorGeneric):
    """ Generic filesystem error e.g. can't write to filepath
    """
        
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
    print "============"
    print formatParams( liste )
    print "============"
    
    liste2 = ['tag1', 'tag2', 'tag3', 'tag4\special']
    print makeList(liste2)
    print "============"
    #liste3 = { 'key1':'value1', 'key2':['value2a', 'value2b'] }
    liste3 = [ 'first', ('key1','value1'), ('key2',["value2a", "value2b\special", "value2c"]), ('key3','value3') ]
    print versaUrlEncode(liste3)
    print "============"
    liste4 = { 'first':None, 'key1':'value1', 'key2':["value2a", "value2b\special", "value2c"], 'key3':'value3' }
    print versaUrlEncode(liste4)
    