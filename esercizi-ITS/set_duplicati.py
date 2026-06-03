def main()
    lista = input("Seleziona una lista di numeri e verranno contati i duplicati")

def duplicati(lista):

length_lista=len(lista)
length_set=len(set(lista)
duplicati_totali=length_lista - length_set

    if length_lista > length_set:
        print(f"I duplicati sono: {duplicati_totali}")
    else:
        print("Non ci sono duplicati")
