from abc import abstractmethod
class Persona():
    def __init__(self, nome, eta):
        self.__nome=nome
        self.__eta=eta
    

    @property 
    def nome(self):
        return self.__nome

    @property
    def eta(self):          
        return self.__eta
    
    @eta.setter             
    def eta(self, value):
        self.__eta = value
    
    @abstractmethod
    def presentati(self):
        pass

    def __str__(self):
        return f'{self.__nome} | {self.__eta}'

class Studente(Persona):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
        self.corsi=[]

    def mostra_corsi(self):
        for c in self.corsi:
            print(c)


     
    def presentati(self):
        return f'{self.nome} | {self.eta} | {self.corsi}'   

    def set_corso(self, corso):
        self.corsi.append(corso)
    
  
class Insegnante(Persona):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
        self.classi=[]
    
    def presentati(self): 
        return f'Nome: {self.nome} | Classi: {",".join(self.classi)}'


p1 = Persona('Riccardo R', 21)
print(p1)
s1 = Studente('Riccardo R', 21)
s1.set_corso('Matematica')
print(s1)
s1.presentati()

i1=Insegnante('Marco Aurelio', 40)
print(i1)