#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import yaml

# ==============================================
# ==============================================

y1 = """
american:
  - Boston Red Sox
  - Detroit Tigers
  - New York Yankees
national:
  - New York Mets
  - Chicago Cubs
  - Atlanta Braves
"""

y1s = yaml.load(y1)
print y1s

y2 = """
- [name        , hr, avg  ]
- [Mark McGwire, 65, 0.278]
- [Sammy Sosa  , 63, 0.288]
"""
y2s = yaml.load(y2)
print y2s

y3 = """
null: ~
true: boolean
false: boolean
string: '12345'
"""
y3s = yaml.load(y3)
print y3s

y4 = """
-
 device: default
 name: homemon
"""
y4s = yaml.load(y4)
print y4s

