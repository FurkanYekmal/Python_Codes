# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 05:55:51 2021

@author: Furkan Kaya
"""

a = int(input('Your number: '))

b = 2**a + 1 
c = 2*a + 1

d = b/c

if d == 1:
    print('Your number is a Curzon number')

elif d!=1:
    print('Your number is not a Curzon number')