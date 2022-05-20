# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 16:56:22 2021

@author: Furkan Kaya
"""

#Can a newborn baby be expected to live to a billion (10e9) seconds?

#An average person is expected to live to 80 years

seconds = 60     #Seconds in a minute
minutes = 60     #Minutes in an hour
hours = 24       #Hours in a day
days = 365       #Days in a year
years = 80       #Life-expectancy for the baby

life_exp = seconds*minutes*hours*days*years

if life_exp >= 10e9:
    print('The baby is expected to live to a billion seconds')
elif life_exp < 10e9:
    print('The baby is not expected to live to a billion seconds')


