# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 02:28:26 2021

@author: Furkan Kaya
"""
#A Monte-Carlo simulation of a dice throw

import random

#Generate random numbers

N = 10000
eyes = [random.randint(1,6) for i in range(N)]
six = 0

#Count how often dice showed six

for outcome in eyes:
    if outcome == 6:
        six += 1

#Print result
print('Got six {0} times from rolling the dice {1} times.'.format(six, N))