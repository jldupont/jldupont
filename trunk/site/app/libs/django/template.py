"""
    Custom Django Template loader
    * registers the filesystem/memcache based page template loader
    * registers the custom tags defined in libs.wiki
    
    @author: Jean-Lou Dupont
    
    @example:
    
        from libs.wiki import template
        rendered_template = template.render( page_name, template_values )
    
"""

__version__ = "$Id: template.py 583 2008-10-09 14:33:43Z jldupont $"
__author__  = "Jean-Lou Dupont"

import os
import logging

import django
import django.conf

#import django.template.loader as django_loader  
#django_loader.template_source_loaders = None

_loaders = (    'libs.django.filesystem_template_loader.load_template_source',
                'libs.django.db_template_loader.load_template_source',
                )

try:
    setattr(django.conf.settings, 'TEMPLATE_LOADERS', _loaders )
    logging.info('libs.django.template: already loaded init')
except AttributeError:
    django.conf.settings.configure( TEMPLATE_LOADERS = _loaders )
    logging.info('libs.django.template: first time init')        
except (EnvironmentError, RuntimeError):
    logging.error('libs.django.template: error init Django')

import django.template
import django.template.loader

django.template.add_to_builtins( "libs.django.anchor" )
django.template.add_to_builtins( "libs.django.include" )

#======================================================

def render(template_name, template_dict, debug=False):
    tpl = django.template.loader.get_template(template_name)
    return tpl.render( django.template.Context(template_dict) )

#======================================================
