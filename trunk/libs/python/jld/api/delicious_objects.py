#!/usr/bin/env python
""" Delicious objects
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

from xml.dom import minidom

import jld.api as api


__sample_bundles = """
<?xml version="1.0" encoding="UTF-8"?>
<bundles>
  <bundle name="my-stuff" tags="my-diagrams my-mindmaps"/>
  <bundle name="php" tags="php pear PHING phpdoc PHPUnit PEAR-CHANNEL"/>
  <bundle name="programming" tags="gae GWT python programming"/>
  <bundle name="software" tags="ajax jquery eclipse subversion programming"/>
  <bundle name="telecomm" tags="IP ITU atca fcoe utca ITU-T ethernet companies semiconductor"/>
</bundles>
"""

__sample__tags = """
<?xml version="1.0" encoding="UTF-8"?>
<tags>
  <tag count="1" tag=".net"/>
  <tag count="19" tag="AI"/>
  <tag count="2" tag="AOP"/>
  <tag count="1" tag="AmazonWebServices"/>
  <tag count="1" tag="BT"/>
  <tag count="1" tag="Brain"/>
<tags>
"""

__sample_recent = """
<?xml version="1.0" encoding="UTF-8"?>
<posts user="jldupont" tag="">
  <post href="http://www.gliffy.com/publish/1553434/" hash="94bd15480886834d104b24178dcc3e48" description="BasicInterfaces" tag="my-diagrams" time="2008-12-01T20:36:01Z" extended=""/>
  <post href="http://dev.chromium.org/developers/design-documents/extensions" hash="b02e129cdaa64cbbb54252cfbfebeeee" description="Extensions " tag="chromium, google" time="2008-12-01T19:31:46Z" extended=""/>
</posts>
"""

#no matching posts
__sample_recent2 = """
https://api.del.icio.us/v1/posts/recent?count=100&tag=business333
<?xml version="1.0" encoding="UTF-8"?>
<posts user="jldupont" tag="business333"/>
"""

__sample_update = """
<?xml version="1.0" encoding="UTF-8"?>
<update time="2008-12-01T20:36:01Z" inboxnew="0"/>
"""

class Update(object):   
    def __init__(self, raw):
        try:
            e = minidom.parseString(raw).documentElement
            self.time = e.getAttribute('time')
            self.inbox = e.getAttribute('inboxnew')
        except Exception,e:
            raise api.ErrorProtocol( 'msg:expecting', {'param':'update'} )
    

__sample_bundle = """
<?xml version="1.0" encoding="UTF-8"?>
<bundles>
  <bundle name="my-stuff" tags="my-diagrams my-mindmaps"/>
</bundles>
"""
class Bundle(object):
    def __init__(self, raw):
        try:
            e = minidom.parseString(raw).documentElement
            b = e.getElementByTagName('bundle')[0]
            self.time = b.getAttribute('time')
            self.inbox = e.getAttribute('inboxnew')
        except Exception,e:
            raise api.ErrorProtocol( 'msg:expecting', {'param':'update'} )
    
