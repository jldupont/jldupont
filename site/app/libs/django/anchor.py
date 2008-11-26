# @author: Jean-Lou Dupont

import os
import logging

import google.appengine.ext.webapp.template as template
from libs.django import verifyQuotes, unquote

register = template.create_template_register()

@register.tag('a')
def do_anchor(parser, token):
    """
        Anchor
        {% a "url" "text" ["target"] %}
    """
    try:
        liste = token.split_contents()
        tag_name = liste[0]
        url  = liste[1]
        text = liste[2]
    except:
        raise template.django.template.TemplateSyntaxError, "%r tag requires two or three arguments" % token.contents.split()[0]

    target = liste[3] if (len(liste)==4) else None
    if (target):
        verifyQuotes( tag_name, target )
       
    verifyQuotes( tag_name, (url,text) )
    url, text, target = unquote( [url, text, target] )   
    return AnchorNode( url, text, target )

class AnchorNode(template.django.template.Node):
    def __init__(self, url, text, target = None):
        self.url  = url
        self.text = text
        self.target = target
        
    def render(self, context):
        if (self.target):
            return "<a href='%s' target='%s'>%s</a>" % (self.url, self.target, self.text)
        
        return "<a href='%s'>%s</a>" % (self.url, self.text)

# ============================================================
    
@register.tag('ai')
def do_anchor_image(parser, token):
    """
        Anchor with Image
        {% ai "url" "title" "src" %}
    """
    try:
        tag_name, url, title, src = token.split_contents()
    except:
        raise template.django.template.TemplateSyntaxError, "%r tag requires three arguments" % token.contents.split()[0]

    verifyQuotes(tag_name, url)
    verifyQuotes(tag_name, title)
    verifyQuotes(tag_name, src)

    return AnchorImageNode( url[1:-1], title[1:-1], src[1:-1] )
    
class AnchorImageNode(template.django.template.Node):
    def __init__(self, url, title, src):
        self.url  = url
        self.title = title
        self.src   = src
        
    def render(self, context):
        return "<a href='%s' title='%s'><img src='%s'></a>" % (self.url, self.title, self.src)
