with open("studenti.csv", 'r+', newline='') as csvfile:
    media_maggiore=0
    righe=csvfile.readlines()
    for riga in righe:
        tot=0
        valori=riga.split(',')
        print(valori)
        for valori in 