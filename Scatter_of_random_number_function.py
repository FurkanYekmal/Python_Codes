# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 04:48:11 2021

@author: Furkan Kaya
"""

import matplotlib.pyplot as plt
import random

#Generate random numbers

N = 500
x = range(N)
y = [random.uniform(-1,1) for number in x]

#Plot random values

plt.plot(x, y, 'bo')
plt.show()