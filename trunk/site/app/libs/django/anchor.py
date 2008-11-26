# @author: Jean-Lou Dupont

import os
import google.appengine.ext.webapp.template as template
from libs.django import verifyQuotes

register = template.create_template_register()

def do_anchor(parser, token):
    """
        Anchor
        {% a "url" "text" %}
    """
    try:
        tag_name, url, text = token.split_contents()
    except:
        raise template.django.template.TemplateSyntaxError, "%r tag requires two arguments" % token.contents.split()[0]

    verifyQuotes( tag_name, url )
    verifyQuotes( tag_name, text )
    
    return AnchorNode( url[1:-1], text[1:-1] )

class AnchorNode(template.django.template.Node):
    def __init__(self, url, text):
        self.url  = url
        self.text = text
        
    def render(self, context):
        return "<a href='%s'>%s</a>" % (self.url, self.text)
    
# REGISTER WITH DJANGO
register.tag( 'a', do_anchor )

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
    
# REGISTER WITH DJANGO
register.tag( 'ai', do_anchor_image )
