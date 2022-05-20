# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 18:12:53 2021

@author: Furkan Kaya
"""
import numpy as np
import matplotlib.pyplot as plt

"""
Bergmann's rule says that animals living in colder climates tend to be larger
in size. Swedish scientists measured the body mass of different moose 
populations in Sweden and found that the further north you go, 
the bigger the moose get! Taking their data we can fit a line through it to
predict the body mass of a moose at some latitude using the equation 
"""

mass = 0
a = 2.757
b = 16.793

#print('Input the desired Latitude:')

#latitude = float(input())


#mass = (a*latitude) + b

#print('Output the mass', mass)

latitude1 = np.linspace(58,66)
mass1 = (a*latitude1) + b

plt.plot(latitude1, mass1, '')
plt.xlabel('Latitude (degrees North)')
plt.ylabel('average body mass of female moose')
plt.show()