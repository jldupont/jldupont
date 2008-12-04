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

this_file_path = os.path.abspath( __file__ )
this_path = os.path.dirname( this_file_path  )
sys.path.append( this_path )

import jld as jld

version = jld.__version__
egg_name = 'jld-%s-py2.5.egg' % version
URL = 'http://jldupont.googlecode.com/svn/tags/eggs/%s' % egg_name

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


import shutil

#Find /tags by recursing downwards
path = os.path.abspath( __file__ )
while True:
    path = os.path.dirname( path )
    tags_path = path + os.sep + 'tags'
    if (os.path.exists(tags_path)):
        break

#Compute source path of egg
source_egg_path = this_path + os.sep + 'dist' + os.sep + egg_name 
dest_egg_path = tags_path + os.sep + 'eggs' 

# Copy to tags directory
print 'copying to tags directory'
shutil.copy(source_egg_path, dest_egg_path)