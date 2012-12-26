#coding=utf-8
# Filename: __init__.py
# import sys
# sys.path.append("..")
# sys.path.append("../base")

solversList = ['sNakeSingle',
    'sHideSingle',
    'sNakePair'
    ]

classes = []
for s in solversList:
    exec ('from ' + s + ' import ' + s)
    exec ('classes.append(' + s + '())')

import sLink

# from sNakeSingle import sNakeSingle
# from sHideSingle import sHideSingle
# from sNakePair import sNakePair

# __all__ = ['solver', 'sNakeSingle', 'sHideSingle', 'sNakePair']


# SOLVERS_LIST =     [    sNakeSingle(), 
#                     sHideSingle(),
#                     sNakePair()
#                 ]