"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

__all__ = [ 'RawDoc' ]

from xml.dom import minidom

from BeautifulSoup import BeautifulSoup

# Google AppEngine
try:
    from google.appengine.api import urlfetch
    def fetcher(self, url):
        return urlfetch.fetch(url)
    
# Normal
except:
    import urllib2
    def fetcher(url):
        socket = urllib2.urlopen(url)
        return socket.read()

# Exception classes
import jld.api as api

class RawDoc(object):
    """  Retrieves a Google Documents 'doc' in raw format 
    """
    
    _api = "http://docs.google.com/RawDocContents?action=fetch&justBody=false&revision=_latest&editMode=false&docID=%s"
    
    def __init__(self, docid = None):
        """
        """
        self.docid = docid

    def fetch(self, docid = None):
        """ Retrieves and processes
        """
        did = docid if docid else self.docid
        url = self._api % did
        
        try:
            raw = fetcher( url )
        except Exception,e:
            raise api.ErrorNetwork('network error')
        
        return self._process(raw)
        
    def _process(self, content):
        
        raw = BeautifulSoup(content).prettify()
        
        try:
            e = minidom.parseString(raw).documentElement
            bodyE = e.getElementsByTagName('body')[0]  #only one body element of course
            body  = bodyE.childNodes[0].nodeValue
        except Exception,e:
            raise api.ErrorProtocol('missing_element', {'element':'body'})

        print body

        try:
            revision = bodyE.getAttribute('revision')
        except Exception,e:
            raise api.ErrorProtocol('missing_attribute', {'attribute':'revision'} )
        
        try:
            styleE = e.getElementsByTagName('style')[0]
            style   = styleE.childNodes[0].nodeValue            
        except Exception,e:
            raise api.ErrorProtocol('missing_element', {'element':'style'})
        
        return ResultDoc( style, body, revision )

class ResultDoc(object):
    """ Result doc
    """
    def __init__(self, style, body, revision):
        self.style = style
        self.body  = body
        self.revision = revision
        

"""
    WRONG DOCUMENT ID, RESULT:
    <body class=app id="DocAction"  onload="DoPageLoad();" topmargin=0> ...
    
    GOOD DOCUMENT ID, RESULT:
    <body onload="DoPageLoad();" revision="dgstxrxv_138fh5wphfc:24"> ...
     
"""

# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """

    h = RawDoc('dgstxrxv_138fh5wphfc')
    result = h.fetch()
    
    print result.revision
    #print result.style
    