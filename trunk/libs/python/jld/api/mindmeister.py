"""MindMeister WEB Service API
"""
__author__ = "Jean-Lou Dupont"
__version__= "$Id$"

import binascii
import md5
import urllib2
import jld.api as api

class MM(object):
    """MindMeister WEB API
    """
    
    _auth = "http://www.mindmeister.com/services/auth?api_key=%s&perms=%s&frob=%s&api_sign=%s"
    _api  = "http://www.mindmeister.com/services/rest?%s"
    
    _perms = ['read', 'write', 'delete']
    
    def __init__(self, secret, api_key, auth_token = None):
        self.secret = secret
        self.api_key = api_key
        self.auth_token = auth_token
        
    def api_sig(self, params):
        """Generates the api_sig parameter
        """
        sorted_list = api.alphaOrderParams( params )
        liste = api.concatenateParams( sorted_list )
        string = "%s%s" % (self.secret, liste)
        sign = md5.new(string)
        return binascii.hexlify( sign.digest() )
       
    def gen_auth_url(self, perm, frob):
        """ Generates the authentication URL used to point
            the user to.
            Client must call the mm.auth.getFrob before
            trying to generate an authentication URL.
        """
        if perm not in self._perms:
            raise RuntimeException("invalid permission")
        
        params = {  'api_key':  self.api_key,
                    'frob':     frob,
                    'perms':    perm
                  }
        sign = self.api_sign(params)
        
        return self._auth % (self.api_key, perm, frob, sign) 

    def do(self, **args):
        """ Executes an arbitrary method
        """
        if (self.auth_token is not None):
            args['auth_token'] = self.auth_token
        
        args['api_key'] = self.api_key    
        sig = self.api_sig( args )
        args['api_sig'] = sig
        
        params = api.formatParams( args )
        url = self._api % params
        
        return url
        
    
# ===================================================================================
    
if __name__ == "__main__":
    """Examples as per MindMeister https://www.mindmeister.com/services/api
    """
   
    params = { 'yxz':'foo' ,'feg':'bar', 'abc':'baz' }
    
    mm = MM('DEADBEEF','c4f64204ca7ee60dd11da6d568b2b199')
    
    print mm.api_sig(params)  # should be 75178b3c27252027ae97b9a5eb36ce41
    print "##############"
    #https://www.mindmeister.com/services/rest?
    # api_key=c4f64204ca7ee60dd11da6d568b2b199
    # &method=mm.test.echo
    # &api_sig=b46d4eabe4e18cd7fcab2de42d743f2d
    #mm2 = MM('','')
    #print mm2.do(method='mm.test.echo')
    
    #print mm2.do(method='mm.maps.getPublicList')
    
    