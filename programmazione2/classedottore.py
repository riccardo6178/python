

class Persona:
    def __init__(self, nome, cognome, età):
        self.nome = nome
        self.cognome = cognome
        self.età = età

    def __str__(self):
        return f'{self.nome} {self.cognome} | Età: {self.età}'

class Dottore(Persona):
    def __init__(self, nome, cognome, età, specializzazione, stipendio):
        super().__init__(nome, cognome, età)
        self.specializzazione = specializzazione
        self.stipendio = stipendio
        self.pazienti = []
    
    def __str__(self):
        return f'DOTTORE: {self.nome} {self.cognome} | PROFESSIONE: {self.specializzazione}'
    
    def get_stipendio(self):
        return f'{self.cognome}, {self.nome} {self.stipendio}'
    
    def set_stipendio(self, value: int):
        self.stipendio = value
    
    def aggiungi_paziente(self, paziente):
        self.pazienti.append(paziente)
    
    def mostra_pazienti(self):
        for paziente in self.pazienti:
            print(paziente)


class Paziente(Persona):
    def __init__(self, nome, cognome, età, gruppo_sanguigno):
        super().__init__(nome, cognome, età)
        self.gruppo_sanguigno = gruppo_sanguigno
        self.patologie = []
    
    def stampaPatologie(self):
        for p in self.patologie:
            print(p)

    def aggiungi_patologia(self, patologia: str):
        self.patologie.append(patologia)

    def rimuovi_patologia(self, patologia):
        self.patologie.remove(patologia)

    def __str__(self):
        return f'{self.nome} {self.cognome} | Età: {self.età} | {self.patologie}'



paziente1=Paziente('Mario', 'Mudò', 20, 'A')
paziente2=Paziente('Prova', 'Prova', 13, 'A')

dottore1=Dottore('Riccardo', 'Rizzo', 30, 'Neurologo', 10000)
dottore2=Dottore('Marco', 'Saccone', 28, 'Ginecologo', 10000)


dottore1.aggiungi_paziente(paziente1)

dottore2.aggiungi_paziente(paziente2)

paziente1.aggiungi_patologia('Coviddi')
paziente1.aggiungi_patologia('Coviddi')

print('Paziente dottore 1:')
dottore1.mostra_pazienti()

paziente1.rimuovi_patologia('Coviddi')
print(str(paziente1))