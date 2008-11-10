"""MindMeister WEB Service API
"""
__author__ = "Jean-Lou Dupont"
__version__= "$Id$"

import md5
import jld.api as api

class MM(object):
    """MindMeister WEB API
        http://www.mindmeister.com/services/rest?api_key=KEY&auth_token=TOKEN&method=METHOD&api_sig=SIGNATURE
        
        e.g.
        https://www.mindmeister.com/services/rest?api_key=c4f64204ca7ee60dd11da6d568b2b199&auth_token=d73f84e0e724cbd12daf503a63736387&map_id=6805299&method=mm.maps.export&api_sig=907c8967e86e3197722fc541829d98f0
    """
    
    _auth = "http://www.mindmeister.com/services/auth?api_key=%s&perms=%s&frob=%s&api_sign=%s"
    _api  = "http://www.mindmeister.com/services/rest?api_key=%s&method=%s&api_sign=%s%s"
    
    _perms = ['read', 'write', 'delete']
    
    def __init__(self, secret, api_key):
        self.secret = secret
        self.api_key = api_key
        
    def api_sign(self, params):
        """Generates the api_sig parameter
        """
        sorted_list = api.alphaOrderParams( params )
        liste = api.concatenateParams( sorted_list )
        string = "%s%s" % (self.secret, liste)
        sign = md5.new(string)
        return sign.digest()
       
    def gen_auth_url(self, perm, frob):
        """ Generates the authentication URL used to point
            the user to.
        """
        if perm not in self._perms:
            raise RuntimeException("invalid permission")
        
        params = [  ('api_key', self.api_key),
                    ('frob', frob),
                    ('perms', perm)
                  ]
        sign = self.api_sign(params)
        
        return self._auth % (self.api_key, perm, frob, sign) 
    
    def __getattribute__(self, attr, *args):
        """ Generic Method call
        """
        if (not attr.startswith('method_')):
            raise RuntimeException("invalid method name")
        
        method = attr.partition('method_')[2]
        args['method'] = method
        
        def generic(*args):
            sign = self.api_sign( args )
            
        return generic
    
# ===================================================================================
    
if __name__ == "__main__":
    """Examples as per MindMeister https://www.mindmeister.com/services/api/auth
    """
    import binascii
    
    params = [('yxz','foo'),('feg','bar'),('abc','baz')]
    
    mm = MM('DEADBEEF')
    
    print binascii.hexlify( mm.api_sign(params) )