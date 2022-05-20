# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 05:39:28 2021

@author: Furkan Kaya
"""

a = int(input('Price: '))
b = int(input('Percentage discount: '))

c = a - (a*(b/100))

print('Final price after discount is: ', c)