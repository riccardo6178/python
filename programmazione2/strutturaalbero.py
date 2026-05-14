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

    def insert(self, valore):
        if self.__radice is None:
            self.__radice=Nodo(valore)
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
            return self.__searchRicorsivo(nodo.left, valore)
        
        if valore > nodo.valore:
            return self.__searchRicorsivo(nodo.right, valore)
        
    
    def inOrder(self):
        elementi = []
        self.__inOrderRicorsivo(self.__radice, elementi)
        return elementi
    
    def __inOrderRicorsivo(self, nodo, elementi):
        if nodo is None:
            return
        self.__inOrderRicorsivo(nodo.left, elementi)
        elementi.append(nodo.valore)

        self.__inOrderRicorsivo(nodo.right, elementi)

    def isEmpty(self):
        return self.__radice is None
    
    def __repr__(self):
        return f'BST(inOrder={self.inOrder()})'


