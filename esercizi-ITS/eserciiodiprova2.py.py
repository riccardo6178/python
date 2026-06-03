class Persona:
    persone_totali=0
    def __init__(self, nome_completo, eta,):
        self.nome_completo=nome_completo
        self.eta=eta
        Persona.persone_totali+=1

    def __str__(self):
        return f'Ciao sono {self.nome_completo} e ho {self.eta} anni!'

class Studente(Persona):
    def __init__(self, nome_completo, eta, corso):
        super().__init__(nome_completo, eta)
    
persona1=Persona('Riccardo Rizzo', 21)
persona2=Persona('FIlippo Turetta', 32)

print(Persona.persone_totali)

studente1= Studente('Giacomo Vaccaro', 21, 'Fisica')

print(Persona.persone_totali)

del studente1

print(Persona.persone_totali )