lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def epari(n):
    return n % 2 == 0

lista_pari=list(filter(epari, lista))
print(lista_pari)
