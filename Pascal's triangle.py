# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 22:51:05 2021

@author: Furkan Kaya 
"""
# Print Pascal's Triangle in Python
 
# input n
n = 4
 
for i in range(1, n+1):
    for j in range(0, n-i+1):
        print(' ', end='')
 
    # first element is always 1
    C = 1
    for j in range(1, i+1):
 
        # first value in a line is always 1
        print(' ', C, sep='', end='')
 
        # using Binomial Coefficient
        C = C * (i - j) // j
    print()