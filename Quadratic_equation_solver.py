# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 06:15:36 2021

@author: Furkan Kaya
"""

import numpy as np

def quadratic_function():
    
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))

    f1 = ((-b + (np.sqrt(b**2 - 4*a*c)))/(2*a))
    f2 = ((-b - (np.sqrt(b**2 - 4*a*c)))/(2*a))
    
    if f1 == f2:
        print('Root is:', f1)
    else:
        print('First root is: ', f1)
        print('Second root is: ', f2)

quadratic_function()