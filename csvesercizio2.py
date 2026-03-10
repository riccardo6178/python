import csv
file_path='/home/rick/Documents/csv/voti.csv'
righe = []

try:
    with open(file_path, "r+") as f:
        valori=csv.reader(f)
        lista=list(valori)
        for riga in lista:
            riga.append(int(riga[2])>18)
            
        print(lista)
        writer=csv.writer(f)
        writer.writerows(lista)
except FileNotFoundError:
    print("Errore: Assicurati che il file esista nel percorso specificato ")

