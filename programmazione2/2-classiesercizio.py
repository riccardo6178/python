from abc import ABC, abstractmethod
class Persona(ABC):
    def __init__(self, nome, eta):
        self.nome=nome
        self._eta=eta
    

    @property
    def eta(self):          
        return self._eta
    @eta.setter             
    def eta(self, value):
        self._eta = value

    def __str__(self):
        return f'{self.nome} | {self._eta}'
    
    @abstractmethod
    def presentati(self):
        pass

  



class Studente(Persona):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
        self.corsi=[]

    def mostra_corsi(self):
        for c in self.corsi:
            print(c)


     
    def __str__(self):
        return f'{self.nome} | {self.eta} | {self.corsi}'   

    def set_corso(self, corso):
        self.corsi.append(corso)
    
  
class Insegnante(Persona):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
        self.classi=[]


p1 = Persona('Riccardo R', 21)
print(p1)
s1 = Studente('Riccardo R', 21)
s1.set_corso('Matematica')
print(s1)
s1.mostra_corsi()

i1=Insegnante('Marco Aurelio', 40)
print(i1)