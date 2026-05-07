from math import sqrt
def distanza(A, B):
    distanza=float(sqrt(((B[0]**2)-(A[0]**2))+((B[1]**2)-(A[1]**2))))
    print(f'distanza originale:{distanza}')
    return distanza

def quadrato(distanza_tra_punti):
        print(distanza_tra_punti**2)

def menu():
    while True:
        A=(0, 1)
        B=(1, 3)
        print('MENU')
        print('''
            1)Distanza tra due punti
            2) Quadrato della distanza tra due punti
            0)esci
            ''')
        scelta=int(input('Cosa vuoi fare?: '))
        if scelta==1:
            distanza(A, B)
        if scelta==2:
            quadrato(distanza(A, B))
        else:
            break
      
menu()