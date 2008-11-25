""" Django Vars
    Adds contextual variables
    @author: Jean-Lou Dupont
"""

import os
import google.appengine.ext.webapp.template as template
from libs.django import verifyQuotes

register = template.create_template_register()

def do_varset(parser, token):
    """
        var set
        {% varset "var-name" "var-value" %}
    """
    try:
        tag_name, varName, varValue = token.split_contents()
    except:
        raise template.django.template.TemplateSyntaxError, "%r tag requires two arguments" % token.contents.split()[0]

    verifyQuotes( tag_name, varName )
    verifyQuotes( tag_name, varValue )
    
    return VarSetNode( varName[1:-1], varValue[1:-1] )

class VarSetNode(template.django.template.Node):
    
    def __init__(self, key, value):
        self.key  = key
        self.value = value
        
    def render(self, context):
        context[key] = value
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
        value = context[key] if (key in context) else None
        return value
    
# REGISTER WITH DJANGO
register.tag( 'varget', do_varget )
