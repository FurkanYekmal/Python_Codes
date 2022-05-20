# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 13:41:47 2021

@author: Furkan Kaya
@email: furkakay@nmbu.no
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Lesing av filen som inneholder meteorologisk data

data = pd.read_csv('meteodata_aas_2012.csv', skiprows=[1], header=[1], sep=';')

df = pd.DataFrame(data)

print(df)

#Plottet som skal komme i del 2 av oppgaven

plt.plot(df['T_avg'].to_numpy())
plt.xlabel('day of year')
plt.ylabel('Temp [deg C]')
plt.title('Temperature readings for 2012')
plt.show()

