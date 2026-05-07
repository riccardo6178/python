class NodoC:
    def __init__(self, valore):
        self.valore = valore
        self.next   = None
class CircularLinkedList:
    def __init__(self):
        self.__testa = None
        self.__coda  = None
        self.__size  = 0
   
    def insertFirst(self, valore):
        nuovo = NodoC(valore)
        if self.isEmpty():
            self.__testa = nuovo
            self.__coda  = nuovo
            nuovo.next   = nuovo
        else:
            nuovo.next       = self.__testa
            self.__coda.next = nuovo
            self.__testa     = nuovo
        self.__size += 1
    def insertLast(self, valore):
        nuovo = NodoC(valore)
        if self.isEmpty():
            self.__testa = nuovo
            self.__coda  = nuovo
            nuovo.next   = nuovo
        else:
            nuovo.next       = self.__testa
            self.__coda.next = nuovo
            self.__coda      = nuovo
        self.__size += 1
    def insertAfter(self, valore_riferimento, nuovo_valore):
        if self.isEmpty():
            raise IndexError("lista vuota")
        corrente = self.__testa
        while True:
            if corrente.valore == valore_riferimento:
                if corrente == self.__coda:
                    self.insertLast(nuovo_valore)
                    return
                nuovo         = NodoC(nuovo_valore)
                nuovo.next    = corrente.next
                corrente.next = nuovo
                self.__size += 1
                return
            corrente = corrente.next
            if corrente == self.__testa:
                break
        raise ValueError(f"{valore_riferimento} non trovato nella lista")
    def insertBefore(self, valore_riferimento, nuovo_valore):
        if self.isEmpty():
            raise IndexError("lista vuota")
        if self.__testa.valore == valore_riferimento:
            self.insertFirst(nuovo_valore)
            return
        corrente = self.__testa
        while corrente.next != self.__testa:
            if corrente.next.valore == valore_riferimento:
                nuovo         = NodoC(nuovo_valore)
                nuovo.next    = corrente.next
                corrente.next = nuovo
                self.__size += 1
                return
            corrente = corrente.next
        raise ValueError(f"{valore_riferimento} non trovato nella lista")
    # -- RIMOZIONE --
    def removeFirst(self):
        if self.isEmpty():
            raise IndexError("removeFirst da una lista vuota")
        valore = self.__testa.valore
        if self.__testa == self.__coda:
            self.__testa = None
            self.__coda  = None
        else:
            self.__testa     = self.__testa.next
            self.__coda.next = self.__testa
        self.__size -= 1
        return valore
    def removeLast(self):
        if self.isEmpty():
            raise IndexError("removeLast da una lista vuota")
        valore = self.__coda.valore
        if self.__testa == self.__coda:
            self.__testa = None
            self.__coda  = None
        else:
            corrente = self.__testa
            while corrente.next != self.__coda:
                corrente = corrente.next
            corrente.next = self.__testa
            self.__coda   = corrente
        self.__size -= 1
        return valore
    def remove(self, valore):
       
        if self.isEmpty():
            raise IndexError("lista vuota")
        if self.__testa.valore == valore:
            self.removeFirst()
            return
        corrente = self.__testa
        while corrente.next != self.__testa:
            if corrente.next.valore == valore:
                if corrente.next == self.__coda:
                    self.__coda = corrente
                corrente.next = corrente.next.next
                self.__size -= 1
                return
            corrente = corrente.next
        raise ValueError(f"{valore} non trovato nella lista")
    
    def peekFirst(self):
        if self.isEmpty():
            raise IndexError("lista vuota")
        return self.__testa.valore
    def peekLast(self):
        if self.isEmpty():
            raise IndexError("lista vuota")
        return self.__coda.valore

    def traverse(self, passi):
        if self.isEmpty():
            raise IndexError("lista vuota")
        corrente = self.__testa
        for i in range(passi):
            print(f"  Passo {i + 1}: {corrente.valore}")
            corrente = corrente.next
    
    def isEmpty(self):
        return self.__testa is None
    def size(self):
        return self.__size
    def __repr__(self):
        if self.isEmpty():
            return "CircularLinkedList([])"
        elementi = []
        corrente = self.__testa
        while True:
            elementi.append(str(corrente.valore))
            corrente = corrente.next
            if corrente == self.__testa:
                break
        return "CircularLinkedList([" + " -> ".join(elementi) + " -> ...])"

turni = CircularLinkedList()
print("Gestione Turni Analisti — Circular Linked List")
print("-" * 50)

turni.insertLast("alice")
turni.insertLast("bob")
turni.insertLast("carlo")
print("\n1. Aggiunti in ordine: alice, bob, carlo")

print(f"2. Lista attuale: {turni}")

print("\n3. Simulazione 6 turni:")
turni.traverse(6)

turni.insertAfter("bob", "diana")
print("\n4. Diana entra nel team dopo bob")

print(f"5. Lista aggiornata: {turni}")

print("\n6. Simulazione 8 turni (con diana):")
turni.traverse(8)

print("\n7. Bob lascia il team")
turni.remove("bob")

print(f"8. Lista aggiornata: {turni}")

print("\n9. Simulazione 6 turni (senza bob):")
turni.traverse(6)

print(f"\n10. Analisti nel team: {turni.size()}")

