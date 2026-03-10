def fattoriale(n):
    if n==1   #clausola di uscita, da un termine alla operazione
        return 1
    return n * fattoriale(n - 1)

print(fattoriale(5))


