"""
    @author: Jean-Lou Dupont
"""
import logging
from types import *

import django
import django.conf

try:
  django.conf.settings.configure(
    DEBUG=False,
    TEMPLATE_DEBUG=False,
  )
except (EnvironmentError, RuntimeError):
  pass

import django.template
import django.template.loader

def render(template_name, template_dict, debug=False):
    tpl = django.template.loader.get_template(template_name)
    try:
        rendered = tpl.render( django.template.Context(template_dict) )
    except Exception,e:
        logging.warn('Rendering error template[%s] msg[%s]' % (template_name, e) )
    return rendered

def unquote(obj):
    """ Remove single/double quotes
    """
    if (type(obj) is NoneType):
        return []
    
    if (type(obj) is not ListType):
        obj = [obj,]
    
    liste = []
    for o in obj:
        item = o
        if (o is not None):
            item = item.lstrip("'\"")
            item = item.rstrip("'\"")
        liste.append(item)

    return liste

def verifyQuotes(tag_name, obj):
    if (obj is None):
        return
    
    if (type(obj) == 'list'):
        for o in obj:
            if not (o[0] == o[-1] and o[0] in ('"', "'")):
                logging.warn('verifyQuotes: error')
                raise django.template.TemplateSyntaxError, "%r tag's parameter[%s] be in quotes" % (tag_name, o)
            
    if (type(obj) == 'str'):
        if not (obj[0] == obj[-1] and obj[0] in ('"', "'")):
            logging.warn('verifyQuotes: error')            
            raise django.template.TemplateSyntaxError, "%r tag's parameter[%s] be in quotes" % (tag_name, obj)
    
def setConfig( name, value ):
    try:
        setattr(django.conf.settings, name, value )
    except (EnvironmentError, RuntimeError):
        logging.error('libs.django: error setConfig[%s, %s]' % (name, value))   

# =====================================================

# === TAGS ===
django.template.add_to_builtins( "libs.django.anchor" )
django.template.add_to_builtins( "libs.django.include" )
django.template.add_to_builtins( "libs.django.vars" )

# === FILTERS ===
django.template.add_to_builtins( "libs.django.filters" )

