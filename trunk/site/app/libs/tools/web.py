""" WEB tools
    @author: Jean-Lou Dupont
"""


import os
import logging

from google.appengine.api import memcache
from google.appengine.api import urlfetch

_CACHE_TIMEOUT = 15*60
_CACHE_TEMPLATE_KEY_CONTENT = "/web/url/content/%s"
_CACHE_TEMPLATE_KEY_ETAG    = "/web/url/etag/%s"

def get(url, timeout=_CACHE_TIMEOUT):
    """ Fetches a resource through an HTTP GET.
        Performs memcaching.
        @param url: url
        @param timeout: memcache timeout in seconds
        @return: (content, etag) 
    """
    cached_page      = memcache.get(_CACHE_TEMPLATE_KEY_CONTENT % url)
    cached_page_etag = memcache.get(_CACHE_TEMPLATE_KEY_ETAG % url)
    
    content,etag = cond_fetch(url, content = cached_page, etag = cached_page_etag)
        
    if not content:
        return (None, None)
    
    memcache.set(_CACHE_TEMPLATE_KEY_ETAG % url, etag, timeout )
    memcache.set(_CACHE_TEMPLATE_KEY_CONTENT % url, content, timeout )
    
    return (content,etag)

def cond_fetch(url, content = None, etag = None):
    """ Conditional HTTP GET.
        Uses the HTTP header 'etag'
        @param content: current content
        @param etag: current etag
        @return: (content, etag)  
    """
    headers = { 'If-None-Match': etag } if etag else {}
    
    try:
        result = urlfetch.fetch(url=url, headers = headers)
        
        if (result.status_code == 304):
            #logging.info('not changed etag[%s]' % etag)
            return ( content, etag )
        
        if result.status_code == 200:       
            current_etag = result.headers['ETag']
            #logging.info('fetched url[%s] etag[%s]' % (url,current_etag))
            return (result.content, current_etag)
    
    except Exception,e:
        logging.info('cond_fetch: tried url[%s] msg[%s]' % (url,e))
        
    return (None,None)
    
