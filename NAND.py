# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 19:00:09 2021

@author: Furkan Kaya
"""

#Our aim with this script is to create a function that returns the output of a 
#NAND gate

nand = 0
A = int(input('Nand A:'))
B = int(input('Nand B:'))

def nand(A,B):
    if A == B == 1:
        nand = 1
        print('1')
    elif A== B ==0:
        nand = 0
        print('0')
    elif A == 1 and B == 0:
        nand = 0
        print('0')
    elif A == 0 and B == 1:
        nand = 0
        print('0')
    else:
        print('You need the values 0 or 1 for this function to work')

nand(A,B)


