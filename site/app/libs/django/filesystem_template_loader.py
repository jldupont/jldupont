"""
    @author: Jean-Lou Dupont
"""
import os
import logging

from django.template import TemplateDoesNotExist

template_cache = {}

def load_template_source(path, dirs = None):

  abspath = os.path.abspath(path)

  template = template_cache.get(abspath, None)

  if (template is not None):
      #logging.info("libs.wiki.filesystem_template_loader.load_template_source: name[%s] FOUND IN CACHE" % path)      
      return template 
  
  #directory, file_name = os.path.split(abspath)
  try:
      template = (open(abspath).read(), path)
  except:
      #logging.info("libs.wiki.filesystem_template_loader.load_template_source: name[%s] NOT FOUND" % path) 
      raise TemplateDoesNotExist, "Tried [%s]" % path

  template_cache[abspath] = template

  #logging.info("libs.wiki.filesystem_template_loader.load_template_source: name[%s] FOUND" % path)          
  return template
        

load_template_source.is_usable = True