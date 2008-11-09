"""MindMeister WEB Service API
"""
__author__ = "Jean-Lou Dupont"
__version__= "$Id$"

import md5
import jld.api as api

class MM(object):
    """MindMeister WEB API
    """
    
    _auth = "http://www.mindmeister.com/services/auth"
    _api  = "http://www.mindmeister.com/services/"
    
    
    def __init__(self, secret):
        self.secret = secret
        
    def api_sign(self, params):
        """Generates the api_sig parameter
        """
        sorted_list = api.alphaOrderParams( params )
        liste = api.concatenateParams( sorted_list )
        string = "%s%s" % (self.secret, liste)
        sign = md5.new(string)
        return sign.digest()
    
    
if __name__ == "__main__":
    """Examples as per MindMeister https://www.mindmeister.com/services/api/auth
    """
    import binascii
    
    params = [('yxz','foo'),('feg','bar'),('abc','baz')]
    
    mm = MM('DEADBEEF')
    
    print binascii.hexlify( mm.api_sign(params) )