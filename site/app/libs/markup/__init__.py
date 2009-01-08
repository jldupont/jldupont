"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import logging

from docutils.core import publish_parts
import libs.cache as cache

def getReSText(dirs, fragment_path):
    """ Returns a ReStructuredText rendered file
    
        @raise Warning: if the file isn't found in the dirs 
    """
    content = cache.fetchpage( dirs, fragment_path )
    if content:
        return content
    
    content, abs_path, from_cache_flag = cache.fetchfile( dirs, fragment_path )
    
    parts = publish_parts(source=content, writer_name="html4css1")
    
    rendered_page = parts["html_title"] + parts["html_subtitle"] + parts["fragment"]
    
    cache.storepage( abs_path, rendered_page )
    
    return rendered_page
    