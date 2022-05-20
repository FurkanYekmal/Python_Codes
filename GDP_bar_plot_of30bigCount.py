# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 19:00:51 2021

@author: Furkan Kaya
"""

#The ranking of GDP (US $ million) by country according to the IMF 2021

import matplotlib.pyplot as plt

countries1 = ('USA', 'China', 'Japan', 'Germany', 'UK', 'India', 
             'France', 'Italy') 
countries2 = ('Canada', 'South Korea', 'Russia', 'Australia', 'Brazil', 'Spain',
              'Mexico')
countries3 = ('Indonesia', 'Netherlands', 'Switzerland','Saudi-Arabia', 'Turkey',
              'Taiwan', 'Iran', 'Poland')
countried4 =  ('Sweden', 'Belgium','Thailand', 'Nigeria', 'Austria', 
               'Rep. of Ireland', 'Israel')
GDP1 = [22675271, 16642318, 5378136, 4319286, 3124650, 3094704, 2938271, 2106287]     
GDP2 = [1883487, 1806707, 1710739, 1617543, 1491772, 1461552,1192480]
GDP3 = [1158783, 1012598, 824734, 804921, 794530, 759104, 682589, 642121]
GDP4 = [625948, 578996, 538775, 514049, 481796, 476663, 446708]


#plt.bar(countries1, GDP1)
#plt.bar(countries2, GDP2)
#plt.bar(countries3, GDP3)
#plt.bar(countries4, GDP4)
plt.show()

