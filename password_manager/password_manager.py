import hashlib
from account import *
root_user="user criptato"
master_password="password criptata"
def menu():
    scelta=1
    while scelta != 0:
        print('''
    ---- YOUR-PASSWORD-MANAGER ----
        1) Vedi gli account
        2) Aggiungi un account
        0) Esci
          ''')
        scelta=int(input())
        if scelta==1:
            see_accounts()
        if scelta==2:
            add_account()
        if scelta==0:
            break

def get_password():
    tentativi=3
    while tentativi<=3:
          print("Inserisci la master password")
          password_corrente=input()
          if password_corrente != master_password:
             print("Password errata. Hai massimo 3 tentativi\n")
             tentativi -= 1
             print(f"Tentativi disponibili: {tentativi}")
          if password_corrente == master_password:
              menu()
        

def get_user():
    tentativi = 3
    print("=== AUTENTICAZIONE UTENTE ===")
    
    while tentativi > 0:
        print(f"\nTentativi rimasti: {tentativi}")
        user_corrente = input("Inserisci il nome utente: ")
        
        if user_corrente == root_user:
            print("Utente riconosciuto!")
            get_password()
        else:
            tentativi -= 1
            if tentativi > 0:
                print(f" Utente errato.")
            else:
                print("Numero massimo di tentativi esaurito.")
                return False


def main():
        
         print("Benvenuto nel tuo password manager!")
         get_user()
            
main()        

