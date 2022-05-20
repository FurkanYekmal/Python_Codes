# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 01:23:13 2021

@author: Furkan Kaya
@email: furkakay@nmbu.no
"""

import numpy as np
import math


def mean(values):
    gjennom = sum(values)/ len(values)
    return gjennom

def variance(values):
    mu = mean(values)
    return mean([(x - mu) ** 2 for x in values])

def stddev(values):
    return np.sqrt(variance(values))