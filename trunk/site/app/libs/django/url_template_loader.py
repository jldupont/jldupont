""" Django url based template loader with memcache
    @author: Jean-Lou Dupont
"""
_DEBUG = False

import os
import logging

from google.appengine.api import memcache
from django.conf import settings
from django.template import TemplateDoesNotExist
from google.appengine.api import urlfetch

__all__ = ['get_template_sources','load_template_source' ]

_CACHE_TEMPLATE_KEY_CONTENT = "/templates/url/content/%s"
_CACHE_TEMPLATE_KEY_ETAG      = "/templates/url/etag/%s"

def get_template_sources(template_name, template_url_bases=None):
    
    if not template_url_bases:
        template_url_bases = settings.TEMPLATE_URL_BASES
        
    for template_url_base in template_url_bases:
        yield template_url_base % template_name

def load_template_source(template_name, template_url_bases=None):
    tried = []
    
    for url in get_template_sources(template_name, template_url_bases):
        try:
            logging.info("trying [%s]" % url)
            cached_template      = memcache.get(_CACHE_TEMPLATE_KEY_CONTENT % template_name)
            cached_template_etag = memcache.get(_CACHE_TEMPLATE_KEY_ETAG % template_name)
            
            if (cached_template is None):
                tpl,etag = cond_fetch(url)
            else:
                tpl,etag = cond_fetch(url, content = cached_template, etag = cached_template_etag)
                
            if tpl:
                memcache.set(_CACHE_TEMPLATE_KEY_ETAG % template_name, etag, 15*60 )
                memcache.set(_CACHE_TEMPLATE_KEY_CONTENT % template_name, tpl, 15*60 )
                #logging.info( 'saved in memcache [%s]' % template_name )
                return (tpl, template_name)
            
        except Exception,e:
            tried.append(url)
    if tried:
        error_msg = "Tried %s" % tried
    else:
        error_msg = "Your TEMPLATE_URL_BASES setting is empty."
    
    logging.info('NOT FOUND [%s]' % template_name)
    raise TemplateDoesNotExist, error_msg

load_template_source.is_usable = True


# ==========================================

def cond_fetch(url, content = None, etag = None):
    
    headers = { 'If-None-Match': etag } if etag else None
    
    try:
        if (headers):
            result = urlfetch.fetch(url=url, headers = headers)
        else:
            result = urlfetch.fetch(url=url)
        
        if (result.status_code == 304):
            logging.info('not changed etag[%s]' % etag)
            return ( content, etag )
        
        if result.status_code != 200:
            return (None,None)
        
        current_etag = result.headers['ETag']
        logging.info('fetched url[%s] etag[%s]' % (url,current_etag))
        return (result.content, current_etag)
    
    except Exception,e:
        logging.info('tried url[%s] msg[%s]' % (url,e))
        
    return (None,None)
    
