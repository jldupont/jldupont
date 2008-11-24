"""
    @author: Jean-Lou Dupont
"""
import os
import logging

from google.appengine.api import memcache
from django.conf import settings
from django.template import TemplateDoesNotExist

def get_template_sources(template_name, template_dirs=None):
    
    if not template_dirs:
        template_dirs = settings.TEMPLATE_DIRS
        
    for template_dir in template_dirs:
        yield os.path.join(template_dir, template_name)

def load_template_source(template_name, template_dirs=None):
    tried = []
    
    #cached_template = memcache.get('/templates/'+template_name)
    cached_template = None
    if (cached_template is not None):
        #logging.info( 'got from memcache' )
        return (cached_template, template_name)
    
    for filepath in get_template_sources(template_name, template_dirs):
        try:
            tpl = (open(filepath).read(), filepath)
            memcache.set('/templates/'+template_name, tpl[0], 5*60 )
            return tpl
        except IOError:
            tried.append(filepath)
    if tried:
        error_msg = "Tried %s" % tried
    else:
        error_msg = "Your TEMPLATE_DIRS setting is empty. Change it to point to at least one template directory."
    raise TemplateDoesNotExist, error_msg
load_template_source.is_usable = True
