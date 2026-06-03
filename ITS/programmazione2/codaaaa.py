#nizializziamo la coda 
queue = ["Rick", "Giulia", "Marco"]

#enqueue -- aggiungiamo in fondo
queue.append("Anna")
print(queue) #['Rick', 'Giulia', 'Marco', 'Anna']

#dequeue -- rimuoviamo dalla testa
primo= queue.pop(0)
print(primo) #'Rick' -- il primo entrato è il primo ad uscire 
print(queue) #['Giulia', 'Marco', 'Anna']