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

if __name__ == "__main__":
    liste = { 'k2':'v2', 'xyz':'v?xyz', 'abc':'vabc', 'k1':'v1' }
    
    print 'alpha order:'
    sorted_list = alphaOrderParams( liste )
    print sorted_list
    
    print 'concatenate params:'
    print concatenateParams( sorted_list )
    
    print "============"
    print formatParams( sorted_list )