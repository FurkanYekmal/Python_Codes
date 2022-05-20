# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 22:32:04 2021

@author: Furkan Kaya
"""

def getindices(s):
    return [i for i, c in enumerate(s) if c.isupper()]

