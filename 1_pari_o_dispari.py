while True: 
    print("Inserisci un numero: ")
    numero=int(input())

    if (numero == 0):
        print("Numero non valido")
        break

    elif ((numero % 2) == 0):
        print("Il numero è pari")
    elif ((numero % 2) == 1):
        print("Il numero è dispari")
