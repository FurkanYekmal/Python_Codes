# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 04:52:43 2021

@author: Furkan Kaya
"""

import random

def make_deck():
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['C', 'D', 'H', 'S']
    
    deck = []
    for s in suits:
        for r in ranks:
            deck.append(r+s)
            
    random.shuffle(deck)
    return deck

deck = make_deck()
    