studenti = [
    {"nome": "Anna", "età": 33, "corso": "Biologia"},
    {"nome": "Marco", "età": 22, "corso": "Ingegneria"},
    {"nome": "Chiara", "età": 17, "corso": "Scienze Politiche"},
    {"nome": "Luca", "età": 25, "corso": "Economia"},
    {"nome": "Sofia", "età": 30, "corso": "Informatica"},
    {"nome": "Alessio", "età": 21, "corso": "Architettura"},
    {"nome": "Martina", "età": 18, "corso": "Psicologia"},
    {"nome": "Davide", "età": 24, "corso": "Giurisprudenza"},
    {"nome": "Giulia", "età": 16, "corso": "Medicina"},
    {"nome": "Riccardo", "età": 19, "corso": "Design"}
   
]   


def stampa_minorenni():
    minorenni=0
    for student in studenti:
        if student["età"] < 18: 
            minorenni += 1
            print(f"{student["nome"]}")
    print(f"Gli studenti minorenni sono: {minorenni}")

stampa_minorenni()

def set_corsi(studenti):

    lista=[]
    for student in studenti:
        lista.append(student["corso"])
    set_lista=set(lista)
    print(f"{set_lista}")
    
    length_lista=len(lista)
    length_set=len(set(lista))
    duplicati_totali=length_lista - length_set

    if length_lista > length_set:
        print(f"I duplicati sono: {duplicati_totali}")
    else:
        print("Non ci sono duplicati")

set_corsi(studenti)
