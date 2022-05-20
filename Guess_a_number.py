# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 05:20:12 2021

@author: Furkan Kaya
"""

import random

#Generate a random number
number = random.randint(1,100)
attempts = 0
guess = 0

while guess != number :
    guess = int(input('Guess a number: '))
    attempts += 1
    
    if guess == number:
        print('Correct! You used', attempts, 'attempts!')
        break
    elif guess < number:
        print('Go higher!')
    else:
        print('Go lower!')
