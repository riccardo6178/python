tentativi=0
max_tentativi=0

def menu():
    global tentativi
    global max_tentativi
        print("""
    1) Segui la lezione
    2) Quitta la lezione
    3) Pausa
            """)
    try:
        if tentativi > max_tentativi
            print("Troppi tentativi")
            return None
        scelta=int(input("Cosa vuoi fare?"))
        if scelta <= 0 or scelta > 3
            raise ValueError #PER GENERARE UN VALUE ERROR A PIACIMENTO 
        return scelta
    exept ValueError
        print("Scelta non valida")
        menu()

    scelta = menu()
    print("Hai scelto", scelta)
    match scelta:
        case 1
            print("Bravo segui")
        case 2
            exit()
        case 3
            print("prendi il caffe")

#LA FUNZIONE SE SI METTE UN VALORE TROPPO ALTO RITORNA NONE PERCHE IL VALORE DI RITORNO DI TRY EXCEPT E NONE 
