import sys
import os

import page

file = open('wk.xml', 'r')

try:
    index = 0
    while(True):
        line = file.readline()
        print line
        index += 1
        if ( index == 70 ):
            break
        
except Exception, e:
    print "Exception, msg=%s" % e
    
finally:
    file.close()
    