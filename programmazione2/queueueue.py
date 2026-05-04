from collections import deque

class Coda:
    def __init__(self):
        self.__queue=deque()
    

    def enqueue(self, utente):
        self.__queue.append(utente)
    

    def dequeue(self):
        self.__queue.popleft()
    

    def mostra_coda(self):
        if not self.__queue:
            print('Coda vuota!')
        else:
            for i in self.__queue:
                print(i)


    def lunghezza(self):
        return len(self.__queue) 


    def peek(self):
        return self.__queue[-1]    
    

    def primo(self):
        return self.__queue[0]
    

            
    

coda=Coda()
coda.enqueue('ciao')
print(coda.primo())
print(coda.lunghezza())
print(coda.peek())
