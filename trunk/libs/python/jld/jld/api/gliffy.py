#!/usr/bin/env python
""" Gliffy API
    @author: Jean-Lou Dupont
    
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import re

# Patterns for extracting the diagram ID
# ======================================
_rawpatterns = [
             '/publish/(\d+)/',
             '/pubdoc/(\d+)/',
             '/publish/(\d+)$',
             '/pubdoc/(\d+)$',
             ]
_patterns = []
for p in _rawpatterns:
    _patterns.append( re.compile( p ) )

def extractIdFromURI(uri):
    """ Extracts the diagram ID from a URI
    
        >>> tests = [ \
        'http://www.gliffy.com/publish/1553333/', \
        'http://www.gliffy.com/pubdoc/1554222/L.jpg',]
        >>> for t in tests: \
        print extractIdFromURI( t )
        1553333
        1554222
    """
    for p in _patterns:
        g = p.search( uri )
        try:    id = g.group(1)
        except: id = None
        if (id is not None):
            return id
    return None

# Representations
# ===============
_representations = [
                    'http://www.gliffy.com/pubdoc/%s/L.jpg',
                    'http://www.gliffy.com/pubdoc/%s/M.jpg',
                    'http://www.gliffy.com/pubdoc/%s/S.jpg',
                    'http://www.gliffy.com/pubdoc/%s/T.jpg',
                    ]

def representations(id):
    """ Generator for representations
        @param id: the source diagram id 
        @return: URI to target representation
        
    >>> for r in representations(123): print r
    http://www.gliffy.com/pubdoc/123/L.jpg
    http://www.gliffy.com/pubdoc/123/M.jpg
    http://www.gliffy.com/pubdoc/123/S.jpg
    http://www.gliffy.com/pubdoc/123/T.jpg
    """
    for r in _representations:
        yield r % id


class Client(object):
    """ Client API to Gliffy
    """


# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    import doctest
    doctest.testmod()
