# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 05:15:52 2021

@author: Furkan Kaya
@email: furkakay@nmbu.no
"""

import random as rd

def scrabble_words():
    
    with open('sowpods.txt', 'r') as f:
        lines = f.readlines()
        for i in range(10):
            random_choice = rd.choice(lines)
            print(random_choice)
    
scrabble_words()
