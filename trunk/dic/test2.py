import xml.sax

import PageParser

parser = xml.sax.make_parser(  )
handler = PageParser.PageHandler(  )

parser.setContentHandler(handler)
parser.parse("wk.xml")

print "Count: %i" % handler.count