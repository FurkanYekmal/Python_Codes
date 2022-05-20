# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 06:45:52 2021

@author: Furkan Kaya
"""
#This is a program developed to solve a cubic equation based on Cardano's method

import numpy as np

def cubic_solver():
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    d = int(input('d: '))
    
    t = ((-b**3)/(27*a**3) + (b*c)/(6*a**2) - (d)/(2*a))
    g = ((c)/(3*a) - ((b**2)/(9*a**2)))
    h = ((b)/(3*a))
    f = ((np.cbrt(t + np.sqrt(t + g))) + (np.cbrt(t - np.sqrt(t + g))) - h)
    
    print(f)
    
cubic_solver()

    
    