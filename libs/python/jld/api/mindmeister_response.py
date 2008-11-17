"""MindMeister WEB Service API
"""
__author__ = "Jean-Lou Dupont"
__version__= "$Id$"

from xml.dom import minidom

class MM_ResponseBase(object):
    """ Base class response
    """
    def __init__(self):
        self.code = None
        self.error = None
        
class MM_ResponseBasic(MM_ResponseBase):
    """ Basic response
    """
    def __init__(self, raw = None):
        MM_ResponseBase.__init__(self)
        
        #test purpose
        if (raw is not None):
            self._extractErrorCode(raw)
        
    def _extractErrorCode(self, raw):
        try:
            e = minidom.parseString(raw).documentElement
            self.code = e.getElementsByTagName('err')[0].getAttribute('code')
        except:
            pass


class MM_Response_getFrob(MM_ResponseBase):
    """ In response to mm.auth.getFrob
    """
    def __init__(self, raw):
        MM_ResponseBase.__init__(self)
        self.frob = None
        self._extractErrorCode(raw)
        try:
            e = minidom.parseString(raw).documentElement
            self.frob = e.getElementsByTagName('frob')[0].childNodes[0].nodeValue
        except Exception,e:
            self.error = e
        
class MM_Response_getAuthToken(MM_ResponseBase):
    """ In response to mm.auth.getToken
    """
    def __init__(self, raw):
        MM_ResponseBase.__init__(self)
        self.auth_token = None
        self._extractErrorCode(raw)        
        try:
            e = minidom.parseString(raw).documentElement
            self.auth_token = e.getElementsByTagName('token')[0].childNodes[0].nodeValue
        except Exception,e:
            self.error = e
    
class MM_Response_getList(MM_ResponseBase):
    """ In response to mm.maps.getList
    """
    _attribs = ('id', 'title', 'created', 'modified', 'tags')
    
    def __init__(self, raw):
        MM_ResponseBase.__init__(self)
        self.raw = raw
        self.pages = 0
        self.total = None
        self.maps  = []
        self.count = 0
        self.error = False
        self.error_msg = None
        self._extractErrorCode(raw)        
        try:
            self.tree = minidom.parseString(raw).documentElement
            self._extractTotal()   
            self._extractMaps()         
        except:
            pass
        
    def _extractTotal(self):
        try:    
            self.total = self.tree.getElementsByTagName('maps')[0].getAttribute('total')
            self.pages = self.tree.getElementsByTagName('maps')[0].getAttribute('pages') 
        except Exception,e:
            self.error = e

    def _extractMaps(self):
        """ Returns a list of dict
        """
        try:    
            all_maps = self.tree.getElementsByTagName('map')
            for map in all_maps:
                this = {}
                for attr in self._attribs:
                    this[attr] = map.getAttribute(attr)
                
                self.maps.append( this )
            self.count = len( self.maps )
        except Exception,e:
            self.error = e

# ==========================================================

if __name__ == "__main__":
    rGetList = """
<rsp stat="ok">
<maps page="1" pages="1" perpage="100" total="2">
<map id="2490" title="Copy of Freemind map" owner="3" description=""
    created="2007-06-20 06:40:04" modified="2007-06-20 06:40:04" sharedwith=""
    tags="" public="0" viewonly="0" default="0"/>
<map id="2480" title="Freemind map" owner="3" description=""
    created="2007-06-20 06:40:03" modified="2007-06-20 06:40:03" sharedwith=""
    tags="" public="0" viewonly="0" default="0"/>
</maps>
</rsp>
"""

    r = MM_Response_getList(rGetList)
    print r.total
    print r.maps
