def esegui():
    l=[]
    l_reverse=[]
    somma_positivi=0
    conteggio_pari=0
    conteggio_dispari=0
    print('Scegli un numero')
    n=int(input())
    if n>0:
        for i in range(n):
            print('scegli un numero')
            num=int(input())
            if num % 2 == 0:
                conteggio_pari+=1
            if num % 2 == 1:
                conteggio_dispari+=1
            if num > 0:
                somma_positivi+=num
            l.append(num)
    print(f'Conteggio pari: {conteggio_pari}\nConteggio dispari:{conteggio_dispari}\nSomma positivi: {somma_positivi}')
    lista=sorted(l)
    leng=len(lista)
    for i in lista:
        l_reverse.append(lista[leng-1])
        leng=leng-1
    print(f'Lista organizzata e al contrario:{l_reverse} ')
esegui()