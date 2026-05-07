#Il vantaggio dell'albero è che ha un algoritmo di complessità O(log(n)) 
# a discapito dell O(n) della lista. Per e itare lo sbilanciamento ci sono i red-black tree
#Dove ogni nodo è nero o rosso
import random
import time

class Nodo:
    def __init__(self, valore):
        self.valore=valore
        self.left= None
        self.right= None

class BST:
    def __init__(self):
        self.__radice=None

    def insert(self):
        if self.radice is None:
            self.radice=Nodo(valore)
        else:
            self.__insertRicorsivo(self.__radice, valore)
        
    def __insertRicorsivo(self, nodo, valore):
        if valore < nodo.valore:
            if nodo.left is None:
                nodo.left=Nodo(valore)
            else:
                self.__insertRicorsivo(nodo.left, valore)
        else:
            if nodo.right is None:
                
                nodo.right = Nodo(valore)
            else:
                self.__insertRicorsivo(nodo.right, valore)
    
    def search(self, valore):
        return self.__searchRicorsivo(self.__radice, valore)
    
    def __searchRicorsivo(self, nodo, valore):
        if nodo is None:
            return False

        if nodo.valore == valore:
            return True
        
        if valore < nodo.valore:
            return self.__searchRicorsivo(nodo.right, valore)
        
    
    def inOrder(self):
        elementi = []
        self.__inOrderRicorsivo(self.__radice, elementi)
        return elementi
    
    def __inOrderRicorsivo(self, nodo, elementi):
        if nodo is None:
            return
        self.__inOrderRicorsivo(nodo, left, elementi)
        elementi.append(nodo, valore)

        self.__inOrderRicorsivo(nodo.left, elementi)

    def isEmpty(self):
        return self.__radice is None
    
    def __repr__(self):
        return f'BST(inOrder={self.inOrder()})'


albero = BST()
number_list=[]
for i in range (60):
    numero=(random.randint(1, 1000))
    number_list.append(numero)
    print(numero)


target = number_list[59]
print(f"Numeri generati:{len(number_list)}")
print(f"Target da cercare:{target}")

start_list = time.perf_counter()

time_list = time.perf_counter() - start_list

start_bts = time.perf_counter()
albero.search(target)
time_bst= time.perf_counter() - start_bts

print(f"Tempo lista: {time_list:.6f} s")
print(f"Tempo BTS: {time_bst:.6f} s")
print(f"BST {time_list/time_bst:.1f}x piu veloce")

