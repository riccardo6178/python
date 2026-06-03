import csv 
from pathlib import Path
import os 

path='/home/rick/Documents/dati_random.csv'

with open(path, 'r+') as csvfile:
    lettore=csv.reader(csvfile, delimiter=',')
    for riga in lettore:
        print(riga)
    csv.writer(csvfile, delimiter=",")

voti=[{"nome":'Riccardo', 'cognome':'rizzo'}, {'nome':'Gianluca', "voto":18}]
print(voti[1]['voto'])


