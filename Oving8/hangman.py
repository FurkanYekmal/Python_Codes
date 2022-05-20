# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 21:29:48 2021

@author: Furkan Kaya
@email: furkakay@nmbu.no
"""

import random as rd

def find_words():
    f = open('sowpods.txt', 'r')
    lines = f.readlines()
    random_choice = rd.choice(lines)
    return random_choice.upper()

def hangman(random_choice):
    



