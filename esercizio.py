file = open('/home/rick/Documents/Programming/python-projects/Programmazione-ITS/esercizio.txt', 'w+')

def main():
    try:
        file.write("Ciao!")
        print("Ho scritto nel file!")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Errore: {e}")
        

main()
