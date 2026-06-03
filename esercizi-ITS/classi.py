file_path='/home/rick/Documents/Libreria'
libri=[]


class Libro:
    def __init__(self, autore, titolo, genere):
        self.autore=autore 
        self.genere=genere 
        self.titolo=titolo     

    def descrizione(self):
        return f"autore: {self.autore} | titolo: {self.titolo} | genere: {self.genere}"

    def __str__(self):
        return self.descrizione()

    def __repr__(self):
        return self.descrizione()


def mostra_libri():
    with open(file_path, "r", encoding='UTF-8') as file_libreria:
        righe = file_libreria.readlines()
        if not righe:
            print("Il file e' vuoto, aggiungere un nuovo libro")
            menu()
        for riga in enumerate(righe, start=1):
            print(f"{riga}", end='\n')
            
            
            

def aggiungi_libro():
    try:
        with open(file_path, "a+") as libreria:
            print("INSERIRE UN NUOVO LIBRO")
            print("Inserisci l'autore: ")
            autore = input()
            print("Inserisci il titolo: ")
            titolo = input()
            print("Inserisci il genere del libro: ")
            genere = input()
            nuovo_libro = Libro(autore, titolo, genere)
            print(f"NUOVO LIBRO")
            print(f"{nuovo_libro}")
            libreria.write(str(f"{nuovo_libro}"))
         
    except FileNotFoundError as err:
        print(f"ERRORE: {err}")
        with open(file_path, "w") as libreria:
            print("File libreria creato")

def rimuovi_libro():
    with open(file_path, "r+") as file_libreria:
        print("Quale libro vuoi rimuovere?")
        righe = file_libreria.readlines()
        for riga in enumerate(righe, start=1):
            print(f"{riga}", end='\n')
        try:
            scelta=int(input("Inserisci il numero del libro da rimuovere(0 PER USCIRE): "))
            if 1 <= scelta <= len(righe):
                rimosso=righe.pop(scelta-1)
            if scelta==0:
                print("Uscendo...")
                menu()
        except ValueError:
            print("inserisci un numero valido")
        except IndexError:
            print("inserisci un numero valido")
        finally:
             with open(file_path, "w", encoding='UTF-8') as f:
                f.writelines(righe)    

def menu():
    while True:
        print("=== MENU GESTIONE LIBRERIA ===")
        print("1. Aggiungi un libro")
        print("2. Visualizza tutti i libri")
        print("3. Rimuovi un libro")
        print("0. Esci")
        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            aggiungi_libro()
        elif scelta == "2":
            mostra_libri()
        elif scelta=="3":
            rimuovi_libro()
        elif scelta == "0":
            print("Uscita dal programma")
            exit()
        else:
            print("Opzione non valida\n")


menu()
