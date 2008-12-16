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
                    ]

def representations(id):
    """ Generator for representations
        @param id: the source diagram id 
    """
    for r in _representations:
        yield r % id

# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    tests = [
             'http://www.gliffy.com/publish/1553333/',
             'http://www.gliffy.com/pubdoc/1554222/L.jpg',
             ]

    print "EXTRACTION tests"
    for t in tests:
        print extractIdFromURI( t )

    print "REPRESENTATIONS tests"
    for r in representations(123):
        print r
        
