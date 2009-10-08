"""
    import_wrapper
    @author: Jean-Lou Dupont
"""
import os
import glob
import sys
import logging

root = os.path.split(__file__)[0]
sys.path.insert(0, os.path.join(root, 'subdomains'))
sys.path.insert(0, os.path.join(root, 'libs'))
sys.path.insert(0, os.path.join(root, 'server'))
for ziplib_fn in glob.glob(os.path.join(root, 'libs', '*.zip')):
    sys.path.insert(0, ziplib_fn)