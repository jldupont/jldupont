"""
    @author: Jean-Lou Dupont
"""
import os
import logging

from google.appengine.api import memcache

_CACHE_TIMEOUT      = 0
_CACHE_KEY_TS       = "/cachefile/ts/%s"
_CACHE_KEY_CONTENT  = "/cachefile/content/%s"
_CACHE_KEY_PAGE     = "/cachefile/page/%s"


def fetchpage(dirs, fragment_path):
    """ Retrieves a *page* from the cache.
        A *page* corresponds to a processed file,
        in other words, a file that has been *massaged*
        and cached. The source file is checked for freshness.
        
        @return: content or None
    """
    content, abs_path, cache_flag = fetchfile(dirs, fragment_path)
    cached_page = memcache.get(_CACHE_KEY_PAGE % abs_path)
    
    #if the file and the page are in sync
    if cache_flag and cached_page:
        return cached_page
    
    #If the file does not even exist,
    #an exception Warning is raised
    
    #If the page is stale
    return None
        
    
def storepage(abs_path, content):
    """
    """    
    memcache.set(_CACHE_KEY_PAGE % abs_path, content, _CACHE_TIMEOUT)
    

def fetchfile(dirs, fragment_path):
    """ Retrieves a file from the cache.
    
        @param dirs: a list of directories to search into
        @param fragment_path: the filepath fragment
        @return: (content, abs_path, from_cache_flag)  
    """
    result = (None, None, None)
    for dir in dirs:
        path   = os.path.join( dir, fragment_path )
        try:    current_ts = os.path.getmtime(path)
        except: continue
        content, cache_flag = getfile(path, current_ts)
        if content:
            result = (content, path, cache_flag) 
            return result

    raise Warning('msg:file-not-found')
        

def getfile(path, current_ts):
    """ Retrieves the content of file.
        Verifies if the cache is up-to-date or else
        fetches a fresh copy.  Updates the cache if necessary.
        
        @param path: absolute filesystem path 
        @return: (content, from_cache_flag)
    """
    try:
        cached_ts       = memcache.get(_CACHE_KEY_TS      % path)    
        cached_content  = memcache.get(_CACHE_KEY_CONTENT % path)        
        if (cached_ts and cached_content):
            if (cached_ts == current_ts):
                return (cached_content, True)
    
        fh = open(path,'r')
        content = fh.read()
        fh.close()
        
        memcache.set(_CACHE_KEY_TS      % path, current_ts, _CACHE_TIMEOUT)
        memcache.set(_CACHE_KEY_CONTENT % path, content,    _CACHE_TIMEOUT)
    
        return (content, False)
    
    except Exception,e:
        logging.warn("libs.cache.getfile: exception [%s]" % e)
        return (None,None)
