import csv
import json

file_path='/home/rick/Documents/utenti.csv'
jsonfile_path='/home/rick/Documents/conversione.json'

def leggi_lista():
    dati=[]

    with open(file_path, "r+", encoding='utf-8') as csvfile:
        utenti=csv.DictReader(csvfile)
        for riga in utenti:
            dati.append(riga)
        print(dati)
    return dati

def converti_json():
    file_path='/home/rick/Documents/conversione.json'
    try:
        with open(file_path, 'r+') as jsonfile:
            json.dump(leggi_lista(), jsonfile, indent=4)
    except FileNotFoundError as error:
        with open(file_path, 'w+') as jsonfile:
            print(f'ERRORE:{error}\njsonfile non esiste...')
            print('jsonfile creato')

def aggiungi_utente():
    try:
        with open(jsonfile_path, "r+", indent=4) as jsonfile:
            jsonfile_opened=json.load(jsonfile)
        print(jsonfile_opened)
    except FileNotFoundError as e:
        print("ERRORE\n")
        print(f'{e}\n')
        print('ritornando al menu...')
        menu()

def stampa_json():
    with open(file_path, "r+") as jsonfile:
        for row in jsonfile:
            print(row)


def main():
    scelta=1
    while scelta!=0:    
        try:    
            print('-'*20)
            print(" "*8 + "MENU" + " "*8)
            print('1) Visualizza il file json')
            print('2) Agiungi un utente al file')
            print('3)Rimuovi utente dal file')
            print('4)Converti da csv a json')
            print('0)Esci')
            print("\n\n")
            scelta=int(input("\n\nScegli cosa fare: "))
            if scelta==1:
                leggi_lista()
        except scelta>4:
            print("inserisci un valore tra 0 e 4")
        except TypeError:
            print("Quitting...")
            scelta=0
main()
 



