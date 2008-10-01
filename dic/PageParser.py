"""
    Wiktionary
    
    ==lang==
    ===type===
    
    {{en-noun}}
        
"""
import xml.sax.handler
import re

 
class PageHandler(xml.sax.handler.ContentHandler):
    """
        Assumes no child elements to the supported elements
    """
    _elements = ("title", "text")
    
    def __init__(self):
        self.mapping = {}
        self.count = 0
        self.doBuffering = False
        self.title = None
 
    def startElement(self, name, attributes):
        self.buffer = ""
        if (name in PageHandler._elements):
            self.doBuffering = True
 
    def characters(self, data):
        if self.doBuffering:
          self.buffer += data
 
    def endElement(self, name):
        self.doBuffering = False
        
        if (name=="title"):
            if (self.buffer.find(':')==-1):
                self.title = self.buffer
            else:
                self.title = None
            return
        
        if name=="text":
            if (self.title is not None):                
                self.count += 1
                self.mapping[ name ] = self.buffer
                
                o = TextHandler.extract( self.buffer )
                if (len(o)):
                    print "<%s> %s" % (self.title, str(o) )
                
                try:
                    pass
                    #print "(%i) <%s> %s" % (self.count, name, self.buffer)
                except Exception ,e:
                    pass
                    #print "! exception, <%s> " % name

class TextHandler(object):
    
    _lang = re.compile( "==(\w+)=="   )
    _type = re.compile( "===(\w+)===" )
    
    @staticmethod
    def extract(input):
        #split by newline
        t = input.split("\n")

        output = []
        for line in t:
            l = TextHandler._lang.search( line )
            t = TextHandler._type.search( line )
            if (l is not None):
                output.append( l.group(1) )
            if (t is not None):
                output.append( t.group(1) )
                
        return output
            
            
            