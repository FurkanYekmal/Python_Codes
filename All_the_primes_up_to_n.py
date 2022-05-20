3# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 21:45:24 2021

@author: Furkan Kaya
"""
#This function will find all the prime numbers up to an input value

import numpy as np
import math

prime = int(input('Enter your desired number:'))

for i in range(1,prime):
    for j in range(2,i):
        if(i%j == 0):
            break
    else:
        print(i)