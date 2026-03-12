class Persona:
    def __init__(self, nome, birthdate):
        self.nome = nome
        self.età = età
        self.birthdate =  birthdate

class Studente(Persona):
    def __init__(self, nome, birthdate, matricola, corso, voti):
        self.matricola=matricola
        self.corso=corso
        self.voti=dict()
    

    def descrizione(self):
        return f"Matricola: {self.matricola} | Corso: {self.corso} | Voti: {self.voti}" 


