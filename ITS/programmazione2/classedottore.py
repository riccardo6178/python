

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

class GestioneStudio:
    def __init__(self):
        self.dottori: list[Dottore] = []
        self.pazienti: list[Paziente] = []
    
    def crea_dottore(self, nome, cognome, età, specializzazione, stipendio):
        dottore=Dottore(nome, cognome,età, specializzazione, stipendio)
        self.dottori.append(dottore)
        return dottore

    def aggiungi_dottore(self, dottore):
        self.dottori.append(dottore)
        
    def mostra_dottori(self):
        for d in self.dottori:
            print(f'Dottore: {d}')
    
    def crea_paziente(self, nome, cognome, età, gruppo_sanguigno):
        paziente=Paziente(nome, cognome, età, gruppo_sanguigno)
        self.pazienti.append(paziente)
        return paziente
        
    def aggiungi_paziente(self, paziente):
        self.pazienti.append(paziente)
    
    def msotra_pazienti(self):
        for i, p in enummerate(self.pazienti):
            print(f'{i}){p}')


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


def menu():
    while True:
        print(('-'*10) + 'MENU' + ('-'*10))
        print('1) Visualizza pazienti')
        print('2)Visualizzza dottori')
        print('3) Aggiungi dottore')
        print('4) Aggiungi paziente ')
        print('5) Menu patologie')
        print('0)Esci')
        scelta=int(input('Scegli cosa fare: '))
        if scelta==1:
            GestioneStudio.msotra_pazienti()
        if scelta==2:
            gestione=GestioneStudio()
            gestione.mostra_dottori()
        if scelta==3:
            gestione=GestioneStudio()
            print('Insreisci il nome del dottore: ')
            nome=input()
            print("Insreisci il cognome del dottore: ")
            cognome=input()
            print("Inserisci l'età del dottore: ")
            età=int(input())
            print('Inserisci la specializzazione del dottore: ')
            specializzazione=input()
            print('Insreisci lo stipendio del dottore: ')
            stipendio=int(input())
            gestione.crea_dottore(nome, cognome, età, specializzazione, stipendio)

        


menu()
