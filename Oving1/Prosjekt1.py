# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 01:24:39 2021

@author: Furkan Kaya
email: Furkakay@nmbu.no
"""
import numpy as np
import matplotlib.pyplot as plt

# Funksjonen

t = np.arange(start=0, stop=25, step=1)
N = ((50000)/(1+ 9*np.exp(-0.2*t)))

print(t,N)

#Plott for å finne når 90 prosent av bæreevnen er
#plt.figure(1)

plt.plot(t, N,'-')
plt.axhline(y=45000, color='r', linestyle='-')
plt.xlabel('tid (t)')
plt.ylabel('Populasjonsbestand (stykk)')

plt.show()


"""
a) Her har jeg brukt funksjonen np.arange som gitt ovenfor. Det gir meg at jeg
får en tabell hvor alle verdier fra 1 time til 50 timer er oppgitt. Jeg fant
hva C er ved å sette populasjon ved t = 0 lik 5000. Dette gjorde det mulig for 
meg å finne at C = 9 ved tradisjonell utregning matematisk. Jeg gjettet meg ikk
e fram altså, men heller regnet på det. Håper det er i orden. 

b) Svaret etter 24 timer er: 46552 (rundet av oppover til hele tall). Her sette
r jeg da på funksjonen np.arange at tiden blir 25, noe som gjør det lettere å 
finne ut hva populasjonsbestanden blir på det tidspunktet. 

c) Plotten viser at bestanden når 45000 (90 prosent) etter 22 timer omtrent. Her
kan vi se på samme funksjon ved å se at etter 22 timer så er bestanden på 45025.
En plot har blitt lagt ved for å vise dette. Her kan man omtrentlig se at svaret
er omtrent 45000 ved 22 timer. Tallet 45000 kom jeg fram til ved å finne 90 pr-
osent av 50000. 
"""