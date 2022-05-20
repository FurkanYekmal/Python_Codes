# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 20:41:27 2021

@author: Furkan Kaya
"""
c = 299792458  # Speed of light [m/s]

print("Please insert the distance you want to measure how long it takes to travel at the speed of light:")

t = 0

# Calculate the time taken using t = d/c and return it.
distance = int(input())
t = distance/c
    

print('The time it takes is (in seconds):', t)
