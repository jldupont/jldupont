#!/usr/bin/env python
""" NukeSVN - deletes all SVN related directories from a path hierarchy

    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import glob
import os
from optparse import OptionParser

_options =[ 
  {'o1':'-F', 'var':'force', 'action':'store_true', 'default': False, 'help': "Forces the delete action" },
  {'o1':'-q', 'var':'quiet', 'action':'store_true', 'default': False, 'help': "Quiet mode" },
           ]

_usage = """%prog [options] [input_directory]

NukeSVN - deletes all SVN related directories from a directory hierarchy
version $LastChangeRevision$ by Jean-Lou Dupont

The -F option must be used in order to actually perform the delete action or else only a list of the found targets is produced.
"""

def nukedir(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    os.rmdir(directory)
    

def main():
    parser = OptionParser( usage=_usage )
    for o in _options:
        parser.add_option( o['o1'], 
                           dest=o['var'], 
                           action=o['action'], 
                           help=o['help'],
                           default=o['default'] )
    
    (options,args) = parser.parse_args()

    try:
        input  = args[0]
    except:
        input  = os.getcwd()
    
    if (not os.path.isdir(input)):
        print "Error: invalid input_directory parameter"
        exit(0)
    
    if options.force:
        prepend = "deleting: [%s]"
    else:
        prepend = "target: [%s]"
    
    targets = []
    for root, dirs, files in os.walk(input, topdown=False):
        if (os.path.basename(root) == ".svn"):
            targets.append( root )

    for directory in targets:
        if (not options.quiet):
            print prepend % directory
        if (options.force):
            nukedir( directory )
    
    exit(1)

    
# ==============================================
# ==============================================

if __name__ == "__main__":
    main()