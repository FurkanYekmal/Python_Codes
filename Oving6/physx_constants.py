# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 18:29:58 2021

@author: Furkan Kaya
@email: furkakay@nmbu.no
"""
import csv

d = {}

def const_reader():
    with open('constants.txt', 'r') as f:
        next(f)
        next(f)
        for line in f:
            data = line.split()
            name = " ".join(data[:-2])
            value = float(data[-2])
            d[name] = value
        print('Fundamental constants')
        for name, value in sorted(d.items()):
            print('{:30s} {:25}'.format(name, value))
                
const_reader()
        
    
    
