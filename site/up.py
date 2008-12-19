#!/usr/bin/env python
import os

email = os.environ['GAE_EMAIL']
cmd = "appcfg.py update --email=%s app/" % email
os.system(cmd)
