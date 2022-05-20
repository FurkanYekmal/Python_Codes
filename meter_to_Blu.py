# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 19:31:07 2021

@author: Furkan Kaya
"""
#This program will transform input meter values to British length units

cm = float(input('Input your meter to British length unit in cm:'))

inch = cm * 0.394
foot = inch/12
yard = foot/3
mile = yard/1760

if cm > 0:
    print('This is in inches:', inch)
    print('This is in feet:', foot)
    print('This is in yard:', yard)
    print('This is in mile:', mile)

else:
    print('Please insert a value higher than 0')

