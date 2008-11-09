"""
    @author Jean-Lou Dupont
"""

__version__ = "$Id$"
__author__ = "Jean-Lou Dupont"


def tupleCompare( tuple1, tuple2 ):
    """Compares two tuples together
    """
    return cmp( tuple1[0], tuple2[0] )
    

def alphaOrderParams(liste):
    """Orders a parameters list (e.g. (key,value) ) by alphabetical key 
    """
    return sorted(liste, tupleCompare)


def concatenateParams(liste):
    """Concatenates (key,value) list
        e.g. liste = [(k1,v1), (k2,v2)]
             result = k1v1k2v2
    """
    result = ''
    for param in liste:
        result = result + str(param[0]) + str(param[1])
    
    return result

# =========================================================================

if __name__ == "__main__":
    liste = [ ('k2', 'v2'), ('xyz','vxyz'), ('abc','vabc'), ('k1','v1') ]
    
    print 'alpha order:'
    print alphaOrderParams( liste )
    
    print 'concatenate params:'
    print concatenateParams( liste )