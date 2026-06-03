import moduloprova

def main():
    
    a = int(input("Scegli il primo valore del prodotto: "))
    b = int(input("Inserisci il secondo valore del prodotto: "))
    print(moduloprova.moltiplicazione(a, b)) 

    nome=(input("Chi devo salutare?: "))
    print(moduloprova.saluta(nome))
    
main()
