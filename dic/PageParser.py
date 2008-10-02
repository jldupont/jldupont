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
                try:
                    self.title = self.buffer.encode( 'latin-1' )
                except:
                    self.title = None
            else:
                self.title = None
            return
        
        if name=="text":
            if (self.title is not None):                
                self.count += 1
                self.mapping[ name ] = self.buffer
                
                o = TextHandler.extract( self.buffer )
                if (len(o)):
                    try:
                        print "<%s> %s" % (self.title, str(o) )
                    except:
                        print "<%s>" % self.title

class TextHandler(object):
    
    _blacklist= {u'Etymology':True, u'Pronunciation':True, 
                u'Translations':True, u'Abbreviation':True, 
                u'Symbol':True, u'Translingual': True,
                u'Synonyms': True, u'Antonyms': True,
                u'Quotations': True, u'Hyphenation': True,
                u'Conjugation': True, u'References': True,
                u'Particle': True, u'Anagrams': True,
                u'Declension': True, u'Interlingua': True,
                u'Homophones': True, u'Compounds': True,
                u'Etymology1': True, u'Etymology2': True,
                
                
                }
    
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
                e = TextHandler.filter( l.group(1) )
                if (e is not None):
                    output.append( e )
            if (t is not None):
                e = TextHandler.filter( t.group(1) )
                if (e is not None):
                    output.append( e )                
        return output
            
    @staticmethod
    def filter(input):
        try:
            TextHandler._blacklist[input]
            return
        except:
            return input
        
            