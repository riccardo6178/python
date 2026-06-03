import json
import os

# Variabile path richiesta
path = "/home/rick/Documents/studenti.json"

def aggiungi_studente():
    studenti = []
    
    # 1. Verifica se il file esiste
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Prova a caricare il JSON
                studenti = json.loads(content)
        except json.JSONDecodeError as e:
            print(f"⚠️  Attenzione: Il file JSON è corrotto ({e})")
            print("ℹ️  Verrà creata una nuova lista vuota.")
            studenti = []
        except Exception as e:
            print(f"⚠️  Errore di lettura: {e}")
            studenti = []
    else:
        print("ℹ️  File non trovato. Verrà creato un nuovo file.")
        studenti = []

    # 2. Assicurati che i dati siano una lista
    if not isinstance(studenti, list):
        print("⚠️  I dati non sono una lista. Verrà creata una nuova lista.")
        studenti = []

    # 3. Chiedi i dati allo studente
    print("\n--- Aggiungi Nuovo Studente ---")
    nome = input("Inserisci il Nome: ").strip()
    cognome = input("Inserisci il Cognome: ").strip()
    classe = input("Inserisci la Classe (es. 1A): ").strip()

    if not nome or not cognome:
        print("❌ Errore: Nome e Cognome sono obbligatori.")
        return

    # 4. Crea il dizionario dello studente
    nuovo_studente = {
        "nome": nome,
        "cognome": cognome,
        "classe": classe
    }

    # 5. Aggiungi alla lista
    studenti.append(nuovo_studente)
    print(f"\n✅ Studente '{nome} {cognome}' aggiunto con successo!")

    # 6. Salva nel file JSON
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(studenti, f, indent=4, ensure_ascii=False)
        print(f"💾 Dati salvati in: {path}")
    except PermissionError:
        print(f"❌ Errore: Non hai i permessi di scrittura in {path}")
    except Exception as e:
        print(f"❌ Errore durante il salvataggio: {e}")

if __name__ == "__main__":
    aggiungi_studente()
