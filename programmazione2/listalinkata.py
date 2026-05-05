class Nodo:
    def __init__(self, valore):
        self.valore=valore
        self.next=None

class LinkedList:
    def __init__(self):
        self.__testa=None
        self.__size=0

    def InsertFirst(self, valore):
        nuovo=Nodo(valore)
        nuovo.next = self.__testa
        self.__testa=nuovo
        self.__size+=1

    def InsertLast(self, valore):
        nuovo=Nodo(valore)
        if self.__testa is None:
            self.__testa=nuovo
        else:
            corrente = self.__testa
            while corrente.next is not None:
                corrente = corrente.next
            corrente.next = nuovo
        self.__size += 1


    def insertAfter(self, valore_riferimento, nuovo_valore):
        corrente = self.__testa
        while corrente is not None:
            if corrente.valore == valore_riferimento:
                nuovo         = Nodo(nuovo_valore)
                nuovo.next    = corrente.next
                corrente.next = nuovo
                self.__size += 1
                return
            corrente = corrente.next
        raise ValueError(f"{valore_riferimento} non trovato nella lista")

    def insertBefore(self, valore_riferimento, nuovo_valore):
        if self.isEmpty():
            raise IndexError("lista vuota")
        if self.__testa.valore == valore_riferimento:
            self.InsertFirst(nuovo_valore)
            return
        corrente = self.__testa
        while corrente.next is not None:
            if corrente.next.valore == valore_riferimento:
                nuovo         = Nodo(nuovo_valore)
                nuovo.next    = corrente.next
                corrente.next = nuovo
                self.__size += 1
                return
            corrente = corrente.next
        raise ValueError(f"{valore_riferimento} non trovato nella lista")

    def removeFirst(self):
        if self.isEmpty():
            raise IndexError("removeFirst da una lista vuota")
        valore       = self.__testa.valore
        self.__testa = self.__testa.next
        self.__size -= 1
        return valore

    def removeLast(self):
        if self.isEmpty():
            raise IndexError("removeLast da una lista vuota")
        if self.__testa.next is None:
            valore       = self.__testa.valore
            self.__testa = None
            self.__size -= 1
            return valore
        corrente = self.__testa
        while corrente.next.next is not None:
            corrente = corrente.next
        valore        = corrente.next.valore
        corrente.next = None
        self.__size -= 1
        return valore

    def peekFirst(self):
        if self.isEmpty():
            raise IndexError("lista vuota")
        return self.__testa.valore

    def isEmpty(self):
        return self.__testa is None

    def size(self):
        return self.__size

    def __repr__(self):
        elementi = []
        corrente = self.__testa
        while corrente is not None:
            elementi.append(str(corrente.valore))
            corrente = corrente.next
        return "LinkedList([" + " → ".join(elementi) + "])"

cronologia = LinkedList()
print("=" * 60)
print("GESTIONE CRONOLOGIA MODIFICHE — config.txt")
print("=" * 60)

cronologia.InsertLast("admin")
cronologia.InsertLast("mario")
cronologia.InsertLast("sara")
print("Prime modifiche registrate: admin, mario, sara")

print(f"{cronologia}")

cronologia.insertAfter("mario", "guest")
print("\nInserito 'guest' dopo 'mario'")

print(f"{cronologia}")

cronologia.insertBefore("admin", "root")
print("\nInserito 'root' prima di 'admin'")

print(f"{cronologia}")

cronologia.insertBefore("sara", "luca")
print("\nInserito 'luca' prima di 'sara'")

print(f"{cronologia}")

rimosso = cronologia.removeFirst()
print(f"\n Archiviata modifica più vecchia: '{rimosso}'")

print(f"{cronologia}")

rimosso = cronologia.removeLast()
print(f"\nAnnullata ultima modifica: '{rimosso}'")

print(f"{cronologia}")

print(f"\nModifiche registrate: {cronologia.size()}")

piu_recente = cronologia.peekFirst()
print(f"Modifica più recente: '{piu_recente}'")


