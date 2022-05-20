# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 18:18:01 2021

@author: Furkan Kaya
"""
#The program tries to address the Farm problem

#number of legs

def number_of_legs(chicken, cow, pig):
    ch_legs = chicken * 2
    cow_legs = cow *4 
    pig_legs = pig * 4
    
    total_legs = ch_legs + cow_legs + pig_legs
    return total_legs

number_of_legs()
    
