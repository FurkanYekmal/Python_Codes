# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 20:11:36 2021

@author: Furkan Kaya
"""
C = 0
print('Insert the Fahrenheit temperature:')

F = int((input()))
C = (5/9)*(F-32)

if F > -460:
    print('The temperature in Celsius is:,', C)
else: 
    print('This value is under the absolute zero')
    

    