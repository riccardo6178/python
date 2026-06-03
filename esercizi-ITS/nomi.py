lista = [ "Luca", "Marco", "Giovanni", "Matteo", "Francesco",
    "Alessandro", "Davide", "Andrea", "Roberto", "Simone",
    "Giulia", "Sofia", "Aurora", "Ginevra", "Alice",
    "Emma", "Chiara", "Martina", "Giorgia", "Francesca"]

def aggiungi_nome():
    nome=(input("Scegli un nome da aggiungere: "))
    lista.append(nome)

def rimuovi_nome():
    nome=input("Scegli il nome da rimuovere: ")
    lista.remove(nome)   

def stampa_lista():
          lista.sort()
          print(lista)

def menu():
   scelta=1
   while scelta != 0:
     print('''
     Scegli cosa fare sulla lista:
     1) Aggiungi un elemento 
     2) Rimuovi un elemento
     3) Stampa lista ordinata
     0) Esci 
     ''')
     scelta=int(input())
     if scelta == 1:
          aggiungi_nome()
     if scelta == 2:
          rimuovi_nome()
     if scelta == 3:
          stampa_lista()
     if scelta == 0:
         break

menu()
