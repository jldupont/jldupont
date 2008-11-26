""" Django Vars
    Adds contextual variables
    @author: Jean-Lou Dupont
"""

import os
import logging
from types import *

import google.appengine.ext.webapp.template as template
from libs.django import verifyQuotes
from django.template import NodeList

register = template.create_template_register()

def do_varset(parser, token):
    """
        var set
        Form #1:
            {% varset "var-name" "var-value" %}
        Form #2:
            {% varset "var-name" %}
                value
            {% endvarset %}
    """
    try:
        liste = token.split_contents()
        assert(len(liste)>=2)
    except Exception,e:
        logging.warn('varset: msg[%s]' % e)
        raise template.django.template.TemplateSyntaxError, "%r tag requires 2 or 3 arguments" % token.contents.split()[0]

    tag_name = liste[0]
    varName  = liste[1]
    verifyQuotes( tag_name, varName )

    if (len(liste) == 2):
        varValue = parser.parse(('endvarset',))
        parser.delete_first_token()
        
    if (len(liste) == 3):
        varValue = liste[2]
        verifyQuotes( tag_name, varValue )
        varValue = liste[2][1:-1]

    logging.info("varValue [%s]" % varValue)

    return VarSetNode( varName[1:-1], varValue )

class VarSetNode(template.django.template.Node):
    
    def __init__(self, key, value):
        self.key  = key
        self.value = value
        
    def render(self, context):
        if (type(self.value) == StringType):
            context[self.key] = self.value
        else:
            nodelist = NodeList()
            for node in self.value:
                nodelist.append(node.render(context))
            context[self.key] = nodelist.render(context)
        return ""
    
# REGISTER WITH DJANGO
register.tag( 'varset', do_varset )

def do_varget(parser, token):
    """
        var get
        {% varset "var-name" %}
    """
    try:
        tag_name, varName = token.split_contents()
    except:
        raise template.django.template.TemplateSyntaxError, "%r tag requires one argument" % token.contents.split()[0]

    verifyQuotes( tag_name, varName )
    
    return VarGetNode( varName[1:-1] )

class VarGetNode(template.django.template.Node):
    
    def __init__(self, key):
        self.key  = key
        
    def render(self, context):
        value = context[self.key] if (self.key in context) else None
        return value
    
# REGISTER WITH DJANGO
register.tag( 'varget', do_varget )
