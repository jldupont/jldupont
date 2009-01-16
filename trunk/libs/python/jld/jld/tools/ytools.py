#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import os
import yaml
from string import Template

class YattrException(Exception):
    ""
    def __init__(self, msg, params = None):
        Exception.__init__(self, msg)
        self.msg = msg
        self.params = params

class Yfile(object):

    def __init__(self, src_file, name):
        attrs = self._load(src_file, name)
        self._process(attrs)
        
    def _load(self, src_file, name):
        _base = os.path.dirname(src_file)
        _path = os.path.join(_base, name)

        try:
            file = open(_path,'r')
            defaults = yaml.load(file)
            file.close()
            
        except Exception,e:
            raise YattrException('error_load_file', {'path':_path})
        
        return defaults

    def _process(self, attrs):
        ""
        self.__dict__.update( attrs )
    

class Yattr(Yfile):
    """
    >>> y= Yattr(__file__, 'tests/tests.yaml')
    >>> y.var0
    666
    >>> print y.var1
    value1
    """


class Ymsg(Yfile):
    """
    >>> m = Ymsg(__file__, 'tests/tests.yaml')
    >>> print m.render('msg0')
    message0
    >>> print m.render('msg1', {'msg':'test'} )
    message1 test
    >>> print m.render2('msg2', ('test',) )
    message2 test
    """
    def __init__(self, src_file, name):
        Yfile.__init__(self, src_file, name)
        
    def render(self, key, params = None):
        """ Renders a message template with optional parameters
        
            @param key: the message key
            @param params: the optional parameters
            @return: the rendered message (string)
        """
        tpl = Template( self.__dict__[key] )
        return tpl.substitute( params ).lstrip()
    
    def render2(self, key, params = None):
        """ Renders a template through the 'old' python string templating engine
        
            @param key: the message key
            @param params: the parameters
            @return: rendered string
        """
        tpl = self.__dict__[key]
        if (params):
            return tpl % params
        
        return tpl
        
    
# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    import doctest
    doctest.testmod()

    