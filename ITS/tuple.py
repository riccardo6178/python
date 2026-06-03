tupla = (10, 19, 7, 14, 3)

def taglia_tupla():
    print(f"tupla tagliata dentro al funzione:{tupla[2:]}")

def concatena_tupla():
   
    print("Crea una nuova tupla (inserisci due valori tra parentesi separati da virgola): ")
    global tupla 
    nuova_tupla= (209, 217)
    tupla = tupla + nuova_tupla
    print(f"Tupla concatenata: {tupla}")

def stampa_tupla():
        print(f"Tupla stampata: {tupla}")

def menu():
   scelta=1
   while scelta != 0:
     print('''
     Scegli cosa fare sulla tupla:
     1) Taglia tupla
     2) Concatena tupla
     3) Stampa tupla
     0) Esci 
     ''')
     scelta=int(input())
     if scelta == 1:
          taglia_tupla()
     if scelta == 2:
          concatena_tupla()
     if scelta == 3:
          stampa_tupla()
     if scelta == 0:
         break

menu()

