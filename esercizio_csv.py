import csv
file_path = "/home/rick/Downloads/Foglio1.csv"
lista_valori=[]
try:
    with open(file_path, "r", encoding="utf-8") as f:
        valori = csv.reader(f)
        for riga in valori:
            lista_valori.append(riga)
        print(lista_valori)
except FileNotFoundError:
    print("Errore: Assicurati che il file esista nel percorso specificato ")
