# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 02:32:07 2021

@author: Furkan Kaya
@email: furkakay@nmbu.no
"""

from inf120stat import mean
from inf120stat import stddev

import numpy as np

def read_values(liste):
    while True:
        try:
            values = int(input("Ny verdi (Enter = slutt):"))    
            liste.append(values)
        except:
            return liste
            break
        
def print_statistics(values):    
    print(mean((values)))
    print(stddev((values)))                       
            

def choose_action():
    liste = []
    menu = []
    while True:
        inntastinger = input('''
Velg inntastinger:
[1] Les inn verdier
[2] Tøm verdilisten
[3] Vis gjennomsnitt og standardavvik
[4] List ut verdiene
[5] Avslutt

''')

        if inntastinger == '1' :
            liste = read_values(liste)       
            print(f"liste er {liste}")
        elif inntastinger == '2':
            liste.clear()
        elif inntastinger == '3':
            print_statistics(liste)
        elif inntastinger == '4':
            print(*liste)
        elif inntastinger == '5':
            break

 
choose_action()