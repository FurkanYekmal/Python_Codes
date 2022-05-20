# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 21:52:27 2021

@author: Furkan Kaya
@Email: furkakay@nmbu.no
"""

import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd



#Koden som ble brukt for Deloppgave 1
t = []
N = []

for i in range (61):
         t.append(i)
         N.append(round((50000)/(1+ 4165*np.exp(-0.2*i))))
         

for row in zip(*(t,N)):
    print(row)
    
        #df = pd.DataFrame(t, N)
        #print(df)     
                     
      
"""
Her har jeg da først funnet C ved å ha at t = 0 gir N = 12. C er da 4165 for 
ordens skyld. Videre har jeg foretatt en løkke som går gjennom 61 iterasjoner,
altså fra 0 til 60. Jeg brukte append funksjonen til å legge til verdier, og 
jeg brukte row til å lage den andre forløkken. Som vedlegg har jeg lagt ved en
Dataframe fra pandas som gir bedre tabeller og høyere funksjonalitet, men i den
er den andre forløkken mindre viktig. Så jeg tok med begge metoder.  
"""

#Koden som ble brukt for Deloppgave 2 (gangetabell)

for i in range (10):
    a = (i+1)
    b =((i+1)*2)
    c = ((i+1)*3)
    d = ((i+1)*4)
    e = ((i+1)*5)
    f = ((i+1)*6)
    g = ((i+1)*7)
    h = ((i+1)*8)
    j = ((i+1)*9)
    k = ((i+1)*10)
    print(a, b, c, d, e, f, g, h, j, k, sep = '   \t  ')
    

"""
På denne valgte jeg å sette alle variabler inn i datasett, og så foreta en 
print av dem. For å få til korrekt tabell, benyttet jeg meg av \t funksjonen 
inne i en sep. Etter det prøvde jeg meg litt frem helt til jeg fikk fin tabell.
"""