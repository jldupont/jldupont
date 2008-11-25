""" Django filesystem based template loader with memcache
    @author: Jean-Lou Dupont
"""
_DEBUG = True

import os
import logging

from google.appengine.api import memcache
from django.conf import settings
from django.template import TemplateDoesNotExist

__all__ = ['get_template_sources','load_template_source' ]

_CACHE_TEMPLATE_KEY_CONTENT = "/templates/file/content/%s"
_CACHE_TEMPLATE_KEY_TS      = "/templates/file/ts/%s"

# OPTIONAL CONFIGURATION
# ======================
_LISTE = settings.TEMPLATE_ALLOWED_EXTENSIONS
_EXTENSIONS = _LISTE if _LISTE else []

def get_template_sources(template_name, template_dirs=None):
    
    if not template_dirs:
        template_dirs = settings.TEMPLATE_DIRS
        
    for template_dir in template_dirs:
        for extension in _EXTENSIONS:
            if (template_name.endswith(extension)):
                yield os.path.join(template_dir, template_name)
            else:
                yield os.path.join(template_dir, template_name + extension)

def load_template_source(template_name, template_dirs=None):
    tried = []
    
    for filepath in get_template_sources(template_name, template_dirs):
        #logging.info('processing template_name[%s]' % template_name)
        logging.info('processing template_name[%s] filepath[%s]' % (template_name, filepath))
        try:
            ts = os.path.getmtime(filepath)
            cached_template    = memcache.get(_CACHE_TEMPLATE_KEY_CONTENT % template_name)
            cached_template_ts = memcache.get(_CACHE_TEMPLATE_KEY_TS % template_name)
            if (not _DEBUG):
                if (cached_template is not None):
                    if (ts == cached_template_ts):
                        logging.info( 'got from memcache [%s]' % template_name )
                        return (cached_template, template_name)   
            
            logging.info('>1')
            tpl = (open(filepath,'r').read(), filepath)
            logging.info('>2')
            ts  = os.path.getmtime(filepath)
            logging.info('>3')
            memcache.set(_CACHE_TEMPLATE_KEY_TS % template_name, ts, 5*60 )
            memcache.set(_CACHE_TEMPLATE_KEY_CONTENT % template_name, tpl[0], 5*60 )
            #logging.info( 'saved in memcache [%s]' % template_name )
            return tpl
        except Exception,e:
            tried.append(filepath)
            logging.debug('Exception [%s] type[%s]' % (e,type(e)))
    if tried:
        error_msg = "Tried %s" % tried
    else:
        error_msg = "Your TEMPLATE_DIRS setting is empty. Change it to point to at least one template directory."
        
    logging.info('NOT FOUND [%s]' % template_name)
    raise TemplateDoesNotExist, error_msg

load_template_source.is_usable = True

