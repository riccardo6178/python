
class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
        
    def descrizione(self):
        return f"Nome: {self.nome} | Eta': {self.eta}" 

    def __str__(self):
        return self.descrizione
    


class Studente(Persona):
    def __init__(self, nome, eta, voti):
        super().__init__(nome, eta)
        self.voti = voti 
    

    def descrizione(self):
        return f"Nome: {self.nome} | Eta': {self.eta} | Voti: {self.voti}" 

    def __str__(self):
        return self.descrizione()

    def mostra_voti(self):
        print(f"Voti di {self.nome}:")
        for voto in self.voti:
            for materia, punteggio in voto.items():
                print(f"  {materia}: {punteggio}")


lista_studenti=[
    Studente("Alice Bianchi", 20, [{"Matematica": 8}, {"Fisica": 7}, {"Informatica": 9}]),
    Studente("Luca Verdi", 22, [{"Matematica": 6}, {"Fisica": 8}, {"Sicurezza": 7}]),
    Studente("Sofia Romano", 21, [{"Reti": 9}, {"Sistemi": 8}, {"Crittografia": 10}]),
    Studente("Marco Gialli", 23, [{"Programmazione": 7}, {"Basi di dati": 6}, {"Web": 8}]),
    Studente("Giulia Neri", 19, [{"Inglese": 9}, {"Matematica": 8}, {"Laboratorio": 9}])
]

def visualizza_tutti(lista):
    """Visualizza tutti gli studenti con i relativi voti."""
    if not lista:
        print("Nessuno studente presente.")
        return
    for studente in lista:
        print(studente) 

def aggiunti_voti(lista):
    print("Scegli lo studente")
    for i, studente in enumerate(lista, start = 1):
        print(f"{i} {studente.nome}")
    try:
        scelta = int(input("Inserisci il numero: ")) - 1
        if scelta < 0 or scelta >= len(lista):
            print("Numero non valido.")
            return
        studente = lista[scelta]
        materia = input("Inserisci la materia: ")
        punteggio = int(input(f"Inserisci il voto in {materia}: "))
        studente.voti.append({materia: punteggio})
        print(f"Voto aggiunto a {studente.nome}.")
    except ValueError:
        print("Input non valido.") 