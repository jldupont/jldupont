#!/usr/bin/env python
import os

email = os.environ['GAE_EMAIL']
cmd = "/opt/google/appengine/appcfg.py update --email=%s app/" % email
os.system(cmd)
