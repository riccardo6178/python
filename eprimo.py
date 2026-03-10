def eprimo():
    n=int(input("inserisci un numero e verrà decretato se è primo: "))
          
    for i in range(2, n):
        if x % i == 0:
         return False
    return True

    if eprimo(n):
          print("Il numero è primo!")
    else:      
        print("Il numero non è primo")

eprimo()
