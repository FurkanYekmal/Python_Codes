# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 00:26:39 2021

@author: Furkan Kaya
@email: furkakay@nmbu.no
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('meteodata_aas_2012.csv', skiprows=[1], header=[1], sep=';')

df = pd.DataFrame(data)

#Tavg = 10   "Verdier brukt for deloppgave 3"
#A = 20      "Verdier brukt for deloppgave 3"
#offset = 0  "Verdier brukt for deloppgave 3"
Tavg = 6
A = 10
offset = -100
omega = (2*np.pi)/365
day = np.arange(start=1, stop=366, step=1)

def year_temp(days):

    plt.plot(df['T_avg'].to_numpy())
    plt.plot(Tavg + A*np.sin(omega*(day + offset)))
    plt.show()
    
year_temp(day)

"""
I denne siste delen av oppgaven skal vi forsøke å finne hva Tavg er. Her velger
jeg da å oppgi Tavg = 6 basert på den temperaturen jeg bruker i selve oppgaven 
til å finne en gul plott som gir høyest R verdi for funksjonen (R = statistikken)
Ved å bruke df['T_avg'].mean() får jeg en verdi på 5.911. Jeg føler at verdien
jeg oppgir er ganske god. Når det kommer til amplituden, så har jeg satt en
verdi på 10. Var i grunnen litt usikker om det passet best med 10 eller 9, men
valgte til slutt 10 da jeg følte at den lignet mest med eksempelet fra faglærer.
"""