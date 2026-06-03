

def main():
    lista=[]

    print('Inserisci la lunghezza della lista:')
    lunghezza_lista=int(input())
    for i in range(lunghezza_lista):
        valore=int(input('Inserisci un valore: '))
        lista.append(valore)
    somma_numeri(lista)
    potenza(lista)

    
def somma_numeri(lista):
    somma_totale=0
    i=0
    while i < len(lista):
        for elemento in lista:
              somma_totale=lista[elemento]+somma_totale
              i+=1
    
    print(somma_totale)

def potenza(lista):
    lunghezza_lista=len(lista)
    risultato=0
    for elemento in lista:
        risultato=elemento**2
        print(risultato)

if __name__=='__main__':
    main()