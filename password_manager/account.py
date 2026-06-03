database={}
def add_account():
    """Aggiunge un nuovo account alla lista."""
    print("Inserisci la mail dell'account che si desidera salvare: ")
    new_account = input()

    if new_account in database:
        print(f"L'account {new_account} esiste già!")
        return 

    database[new_account] = None

    print(f"Account {new_account} aggiunto con successo!")
    add_password(new_account)

def add_password(account):
    """Aggiunge una password per l'account specificato, ma solo se l'account esiste."""
    if account not in database:
        print(f"Errore: l'account {account} non esiste!")
        return
    
    print(f"Inserisci la password per l'account {account}: ")
    new_password = input()
    database[account]=new_password
    print("Password salvata con successo!")


def see_accounts():
    """Stampa tutti gli account con le relative password."""
    print("\n" + "="*40)
    print("ELENCO ACCOUNT E PASSWORD")
    print("="*40)

    if not database:  # Se il dizionario è vuoto
        print("Nessun account salvato.")
        return

    # Scorriamo il dizionario con .items() che restituisce (chiave, valore)
    for account, password in database.items():
        if password:  # Se la password non è None o stringa vuota
            print(f"📧 Account: {account}  |  🔑 Password: {password}")
        else:
            print(f"📧 Account: {account}  |  ⚠️ Password: NON IMPOSTATA")

    print("="*40)
    print(f"Totale account: {len(database)}")
