"""
    @author: Jean-Lou Dupont
"""
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
    return tpl.render( django.template.Context(template_dict) )

def verifyQuotes(tag_name, obj):
    if (obj is None):
        return
    
    if (type(obj) == 'list'):
        for o in obj:
            if not (o[0] == o[-1] and o[0] in ('"', "'")):
                raise template.django.template.TemplateSyntaxError, "%r tag's parameter[%s] be in quotes" % (tag_name, o)
            
    if (type(obj) == 'str'):
        if not (obj[0] == obj[-1] and obj[0] in ('"', "'")):
            raise template.django.template.TemplateSyntaxError, "%r tag's parameter[%s] be in quotes" % (tag_name, obj)
    
def setLoaders( _loaders ):
    try:
        setattr(django.conf.settings, 'TEMPLATE_LOADERS', _loaders )
    except AttributeError:
        django.conf.settings.configure( TEMPLATE_LOADERS = _loaders )       
    except (EnvironmentError, RuntimeError):
        logging.error('libs.django: error init Django')


def setDirs( _dirs ):
    try:
        setattr(django.conf.settings, 'TEMPLATE_DIRS', _dirs )
    except AttributeError:
        django.conf.settings.configure( TEMPLATE_DIRS = _dirs )       
    except (EnvironmentError, RuntimeError):
        logging.error('libs.django: error init Django')


# =====================================================

django.template.add_to_builtins( "libs.django.anchor" )
django.template.add_to_builtins( "libs.django.include" )

