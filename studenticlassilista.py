class Libro:
    def __init__(self, titolo, autore):
        self.titolo=titolo
        self.autore=autore

    def info_libro(self):
        print(f"{self.titolo} | {self.autore}")

    def __str__(self):
        return f"{self.autore} | {self.titolo}"
    
class Utente:
    def __init__(self, nome, cognome):
        self.nome=nome
        self.cognome=cognome

    def mostra_utente(self):
        print(f"{self.nome}, {self.cognome}")
    
    def __str__(self):
        return self.mostra_utenti

libri=[]

def aggiungi_libro():
    print('Inserisci il titolo del libro:')
    titolo_libro=input()
    print("Ora inserisci l'autore:")
    autore_libro=input()
    libro=Libro(autore_libro, titolo_libro)
    libri.append(str(libro))
    print(libri)

aggiungi_libro()