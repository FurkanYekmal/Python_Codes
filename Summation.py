# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 06:02:48 2021

@author: Furkan Kaya
"""

n = int(input('Enter number: '))

v = []

for i in range(n):
    v.append(i+1)
    d = sum(v)
    print(d)
    