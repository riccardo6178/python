# Relazione sulle Strutture Dati: Pila, Lista Collegata e Albero BST

## 1. Pila (Stack)

### Cosa è
La pila è una struttura dati lineare che segue il principio **LIFO** (*Last In, First Out*): l'ultimo elemento inserito è il primo ad essere rimosso. Analogia: una pila di piatti — metti un piatto sopra e prendi sempre quello in cima.

### A che serve
- Cronologia del browser (pulsante "Indietro")
- Undo/Redo negli editor di testo
- Valutazione di espressioni matematiche
- Gestione delle chiamate di funzione (call stack)
- DFS (*Depth First Search*) nei grafi

### Implementazione in Python
```python
class Stack:
    def __init__(self):
        self.__data = []

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        return self.__data.pop()

    def peek(self):
        if self.isEmpty():
            raise IndexError("empty stack")
        return self.__data[-1]

    def isEmpty(self):
        return len(self.__data) == 0

    def size(self):
        return len(self.__data)
```
Si usa una lista Python come contenitore privato (`__data`). Il metodo `append()` fa da push (aggiunge in coda), `pop()` rimuove l'ultimo elemento. Entrambi operano in fondo alla lista, quindi non richiedono spostamenti in memoria.

### Complessità computazionale
| Operazione | Costo |
|------------|-------|
| `push`     | O(1)  |
| `pop`      | O(1)  |
| `peek`     | O(1)  |
| `isEmpty`  | O(1)  |
| `size`     | O(1)  |

### Pro
- Operazioni push/pop in tempo costante O(1)
- Implementazione semplice ed intuitiva
- Incapsulamento: la classe Stack espone solo metodi leciti, impedendo accessi arbitrari

### Contro
- Accesso consentito solo all'elemento in cima — non c'è accesso diretto agli elementi interni
- Se si usa una lista diretta invece della classe, il programmatore può violare la disciplina LIFO (es: `insert()`, `sort()`, accesso per indice)

---

## 2. Lista Collegata Singolarmente (LinkedList)

### Cosa è
La lista collegata è una struttura dati lineare in cui gli elementi (nodi) non sono memorizzati in celle contigue di memoria. Ogni nodo contiene un **valore** e un **puntatore** al nodo successivo. L'ultimo nodo punta a `None`. Non esistono indici — per arrivare all'n-esimo elemento bisogna scorrere dal primo.

### A che serve
- Inserimenti e rimozioni frequenti in testa
- Code (deque) — la doppiamente linkata è la base di `collections.deque`
- Gestione di memoria nei sistemi operativi
- Implementazione di pile e code dinamiche

### Implementazione in Python
```python
class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.next = None

class LinkedList:
    def __init__(self):
        self.__testa = None
        self.__size = 0

    def insertFirst(self, valore):
        nuovo = Nodo(valore)
        nuovo.next = self.__testa
        self.__testa = nuovo
        self.__size += 1

    def insertLast(self, valore):
        nuovo = Nodo(valore)
        if self.__testa is None:
            self.__testa = nuovo
        else:
            corrente = self.__testa
            while corrente.next is not None:
                corrente = corrente.next
            corrente.next = nuovo
        self.__size += 1

    def removeFirst(self):
        if self.isEmpty():
            raise IndexError("removeFirst da una lista vuota")
        valore = self.__testa.valore
        self.__testa = self.__testa.next
        self.__size -= 1
        return valore

    def removeLast(self):
        if self.isEmpty():
            raise IndexError("removeLast da una lista vuota")
        if self.__testa.next is None:
            valore = self.__testa.valore
            self.__testa = None
        else:
            corrente = self.__testa
            while corrente.next.next is not None:
                corrente = corrente.next
            valore = corrente.next.valore
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
```

### Complessità computazionale
| Operazione         | Costo  |
|--------------------|--------|
| `insertFirst`      | O(1)   |
| `insertLast`       | O(n)   |
| `removeFirst`      | O(1)   |
| `removeLast`       | O(n)   |
| `peekFirst`        | O(1)   |
| Ricerca per valore | O(n)   |
| Accesso per indice | O(n)   |

### Pro
- Inserimento e rimozione in testa in O(1) — nessuno spostamento di massa
- Memoria non contigua: non serve un blocco unico di grandi dimensioni
- Crescita dinamica senza riallocazioni

### Contro
- Accesso sequenziale O(n): non esiste accesso diretto per indice
- `insertLast()` e `removeLast()` costano O(n) perché bisogna scorrere fino alla fine
- Ogni nodo occupa memoria extra per il puntatore `next`
- Maggiore complessità di implementazione rispetto a una lista Python

---

## 3. Albero Binario di Ricerca (BST — Binary Search Tree)

### Cosa è
Un albero binario è una struttura dati gerarchica in cui ogni nodo può avere al massimo **due figli**: sinistro e destro. Il **BST** aggiunge una regola di ordinamento: per ogni nodo, tutti i valori nel sottoalbero sinistro sono **minori**, tutti quelli nel sottoalbero destro sono **maggiori**. Questa regola rende la ricerca molto efficiente.

### A che serve
- Ricerca veloce su dati dinamici (dizionari, indici di database)
- Insiemi ordinati (sorted set)
- Implementazione di mappe (TreeMap)
- Scheduling e code prioritarie
- System calls e gestione della memoria nei sistemi operativi

### Implementazione in Python
```python
class NodoBST:
    def __init__(self, valore):
        self.valore = valore
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.__radice = None

    def insert(self, valore):
        if self.__radice is None:
            self.__radice = NodoBST(valore)
        else:
            self.__insertRicorsivo(self.__radice, valore)

    def __insertRicorsivo(self, nodo, valore):
        if valore < nodo.valore:
            if nodo.left is None:
                nodo.left = NodoBST(valore)
            else:
                self.__insertRicorsivo(nodo.left, valore)
        else:
            if nodo.right is None:
                nodo.right = NodoBST(valore)
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
        else:
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
```

### Complessità computazionale (caso medio — albero bilanciato)
| Operazione | Costo medio | Costo peggiore* |
|------------|-------------|-----------------|
| `insert`   | O(log n)    | O(n)            |
| `search`   | O(log n)    | O(n)            |
| `inOrder`  | O(n)        | O(n)            |

\* Il caso peggiore si verifica quando i valori vengono inseriti in ordine crescente o decrescente: l'albero **degenera in una lista** (ogni nuovo nodo va sempre a destra o sempre a sinistra).

### Pro
- Ricerca molto veloce O(log n) su dati dinamici — molto più efficiente di una lista O(n)
- Mantiene i dati ordinati automaticamente — la visita inOrder restituisce i valori in ordine crescente
- Inserimenti e ricerche si riducono a metà dell'albero ad ogni passo (se bilanciato)

### Contro
- **Sbilanciamento**: se i dati sono già ordinati, l'albero degenera in una lista e la ricerca torna O(n)
- **Memoria**: ogni nodo porta due puntatori (left e right) anche se vuoti — overhead rispetto a una lista
- Implementazione più complessa (ricorsione, gestione dei casi base)
- Non esiste una struttura nativa in Python — va implementata manualmente
- Per evitare lo sbilanciamento servono varianti auto-bilancianti come **Red-Black Tree** o **AVL Tree**

---

## Tabella riassuntiva comparativa

| Caratteristica          | Pila (Stack)         | Lista Collegata       | Albero BST           |
|-------------------------|----------------------|-----------------------|----------------------|
| **Principio**           | LIFO                 | Lineare sequenziale   | Gerarchico ordinato  |
| **Accesso**             | Solo in cima         | Sequenziale O(n)      | Logaritmico O(log n) |
| **Inserimento testa**   | N/A (push O(1))      | O(1)                  | O(log n)             |
| **Inserimento coda**    | N/A (push O(1))      | O(n)                  | O(log n)             |
| **Ricerca per valore**  | N/A                  | O(n)                  | O(log n) / O(n)*     |
| **Memoria per nodo**    | Solo il valore       | Valore + 1 puntatore  | Valore + 2 puntatori |
| **Complessità codice**  | Bassa                | Media                 | Alta                 |
| **Rischio principale**  | Violare LIFO         | Scorrimento lungo     | Sbilanciamento       |

\* O(n) nel caso peggiore (albero degenerato a lista).

---

*Relazione basata sugli appunti del corso "Python - CYB".*
