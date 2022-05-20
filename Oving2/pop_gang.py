# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 21:52:27 2021

@author: Furkan Kaya
@Email: furkakay@nmbu.no
"""

import numpy as np
import matplotlib.pyplot as plt 


#Koden som ble brukt for Deloppgave 1
t = -1
N = 0

for i in range (1,62,1):
         t = t + 1
         N = ((50000)/(1+ 4165*np.exp(-0.2*t))) 
         tlis = [t]
         Nlis = [N]
         for j in range (1):  
                        tlis = int(t)
                        Nlis = round(N)
                        print(tlis, Nlis)
      
"""
Her har jeg da først funnet C ved å ha at t = 0 gir N = 12. C er da 4165 for 
ordens skyld. Videre lager jeg for-loop for header som inneholder variablene, 
og så lager jeg en forloop for vari-ablene t og N. Så printer jeg disse i en 
tabell med header. Vi dobbeltsjekker med verdiene oppnådd i de tre første kol-
onner i oppgaveteksten og ser at vi har fått det korrekt så langt. 
Her har jeg også fjernet alle desimaler etter komma for å gjøre det oversiktlig
og for å tilpasse det oppgaven spurte om.
"""

#Koden som ble brukt for Deloppgave 2 (gangetabell)

#for i in range (10):
    #a = (i+1)
    #b =((i+1)*2)
    #c = ((i+1)*3)
    #d = ((i+1)*4)
    #e = ((i+1)*5)
    #f = ((i+1)*6)
    #g = ((i+1)*7)
    #h = ((i+1)*8)
    #j = ((i+1)*9)
    #k = ((i+1)*10)
    #print(a, b, c, d, e, f, g, h, j, k, sep = '   \t  ')
    

"""
På denne valgte jeg å sette alle variabler inn i datasett, og så foreta en 
print av dem. For å få til korrekt tabell, benyttet jeg meg av \t funksjonen 
inne i en sep. Etter det prøvde jeg meg litt frem helt til jeg fikk fin tabell.
"""