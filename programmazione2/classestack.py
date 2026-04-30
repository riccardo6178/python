class Stack:
    def __init__(self):
        self.__history = []

    def pop_stack(self):
        if self.__history.is_empty:
            print(f'La lista è vuota')
        else:
            return self.__history.pop()

    def append_stack(self, elemento):
        self.__history.append(elemento)       
     
    def peek_stack(self):
        return self.__history[-1]

    def insert_stack(self, indice, elemento):
        self.__history.insert(indice, elemento)
    
    def remove_stack(self, elemento):
        self.__history.remove(elemento)

lista=Stack()

lista.append_stack('google')

print(lista.peek_stack())


print(lista.peek_stack())