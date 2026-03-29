import json
import csv 
import os
from pathlib import Path 
convertiti=0

def crea_csv(path):
    print('File non trovato... ')
    print("Si desidera creare il csvfile?(Verra' creato nella cartella daocumenti)")
    try:        
        scelta=input("[Y/n]")
    except:
        scelta!='Y', 'n'
    if scelta=='Y':
        with open(path, 'w+') as csvfile:
            if os.path.exists(path):
                    print('File creato!')
    elif scelta=='n':
            print('Uscendo.....')
    else:
            print('Inserisci Y o n')


def leggi_csv(path):
    if os.path.exists(path):
        try:
            with open(path, 'r+') as csvfile:
                for riga in csvfile:
                    print(riga)
        except FileNotFoundError:
            print('FIle non trovato...')
    else:
        crea_csv(path)


def leggi_file(path):
    with open(path, 'r+', newline='') as csvfile:
        contenuto=csv.reader(csvfile, delimiter=" ")
        for row in contenuto:
            print(row)

def converti_dizionario(path):
    with open(path, 'r') as csvfile:
        lettore=csv.reader(csvfile)
        dizionario=dict(lettore)
        print(dizionario)

def salva_json(path):
    with open(path, 'r') as csvfile:
        try:
            path_json=input('Scrivi il path completo dove vuoi salvare il file: ')
            with open(path_json, 'w+') as jsonfile:
                reader=csv.reader(csvfile)
                for row in reader:
                    json.dump(row, jsonfile)
        except IsADirectoryError:
            print("Devi specificare amche il nome del file!")
        

def menu():
    while True:
        print(('-'*10)+('MENU')+('-'*10))
        print('1) Leggi il file csv')
        print('2) Converti i dati in un dizionario')
        print('3) Salva in un file JSON')
        print('0) Esci')
        scelta=int(input('Scegli cosa fare: '))
        try:
            if scelta == 1:
                nomefile=input('scrivi il nome del file csv da leggere: ')
                path_completo='/home/rick/Documents/'+nomefile 
                leggi_csv(path_completo)
            elif scelta == 2:
                nomefile=input('scrivi il nome del file csv da cvonvertire: ')
                path_completo='/home/rick/Documents/'+nomefile 
                converti_dizionario(path_completo)

            elif scelta==3:
                nomefile=input('Scrivi il nome del file da convertire: ')
                path_cmpleto='/home/rick/Documents/'+ nomefile
                salva_json(path_cmpleto)
            else:
                break
        except FileNotFoundError as e:
            print(e)
        except ValueError:
            print("devi inserire un numero!")


if __name__=="__main__":
    menu()
