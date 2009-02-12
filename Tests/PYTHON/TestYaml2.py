#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import yaml

# ==============================================
# ==============================================

tests = [
"""
american:
  - Boston Red Sox
  - Detroit Tigers
  - New York Yankees
national:
  - New York Mets
  - Chicago Cubs
  - Atlanta Braves
"""
,
"""
- [name        , hr, avg  ]
- [Mark McGwire, 65, 0.278]
- [Sammy Sosa  , 63, 0.288]
"""
,
"""
null: ~
true: boolean
false: boolean
string: '12345'
"""
,
"""
-
 device: default
 name: homemon
""",
"""
-
  name: Mark McGwire
  hr:   65
  avg:  0.278
-
  name: Sammy Sosa
  hr:   63
  avg:  0.288
"""
,
"""
Mark McGwire: {hr: 65, avg: 0.278}
Sammy Sosa: {
    hr: 63,
    avg: 0.288
  }
"""
,
#{'hr': ['Mark McGwire', 'Sammy Sosa'], 'rbi': ['Sammy Sosa', 'Ken Griffey']}
"""
hr:
  - Mark McGwire
  # Following node labeled SS
  - &SS Sammy Sosa
rbi:
  - *SS # Subsequent occurrence
  - Ken Griffey
"""
,
#[{'item': 'Super Hoop', 'quantity': 1}, {'item': 'Basketball', 'quantity': 4}, {'item': 'Big Shoes', 'quantity': 1}]
"""
- item    : Super Hoop
  quantity: 1
- item    : Basketball
  quantity: 4
- item    : Big Shoes
  quantity: 1
"""
,
"""
- [&D homemon, I0, input0]
- [*D, I1, input1]
"""
]
for test in tests:
    r = yaml.load(test)
    print r
