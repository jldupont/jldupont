""" Jean-Lou Dupont's Python Library
    EGG setup
    
    Dependencies:
    =============
    Registry package:
        Yaml
    Backup.mindmeister_db:
        Sqlobject
    Tools.messages package:
        Yaml
    
    
"""
import sys
import os.path
from setuptools import setup, find_packages

path = os.path.dirname( os.path.abspath( __file__ ) )
sys.path.append( path )

import jld as jld

URL = 'http://jldupont.googlecode.com/svn/trunk/libs/python/dist/jld-%s-py2.5.egg' % jld.__version__

print "URL: %s" % URL

setup(
    name = "jld",
    description = jld.__desc__,
    author_email = jld.__email__,
    author = jld.__author__,
    url    = URL,
    long_description = jld.__desc__,
    version = jld.__version__,
    package_data = {'':['*.*']},
    packages = ['jld', 'jld.api', 'jld.backup', 'jld.cmd', 'jld.registry', 'jld.tools' ],
    scripts=[ 'jld/backup/scripts/mm.py','jld/backup/scripts/mm.bat' ],
    zip_safe = False,
)