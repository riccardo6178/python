import csv
path_file='/home/rick/Documents/python/esame/file.csv'
prodotti=[]


class Prodotto: 
    valore_totale=0
    def __init__(self,__nome, __categoria, __prezzo, __quantità, __codice='PR-00001'):
        self.__codice=__codice
        self.__nome=__nome
        self.__categoria=__categoria
        self.__prezzo=__prezzo
        self.__quantità=__quantità
        valore_totale=(self.__prezzo * self.__quantità)+Prodotto.valore_totale
        prodotti.append(self)

    def __str__(self):
        return (f"[{self.__codice}] {self.__nome} - {self.__categoria}\n Prezzo:{self.__prezzo:.2f}EUR | QUantità: {self.__quantità}")

    def carica_scorte(self, aumento):
        if quantità < 0:
            print('Quantità non valida')
        else:
            self.__quantità+=aumento

    def get_nome(self):
        return self.__nome
    
    def get_codice(self):
        return self.__codice

    def vendi_prodotto(self, davendere):
        if self.__quantità<0:
            print('Quantità insufficiente')
        else:
            self.quantità-=davendere
            print(f'Hai venduto {davendere} prodotti')
    
    @classmethod
    def get_valore_totale(cls):
        return cls.valore_totale



def carica_scorte():

    print('Di che prodotto vuoi aumentare il numero?: ')
    codice=input()
    with open(path_file, 'r+', newline='') as csvfile
    for riga in csvfile
        if riga.get_codice()==codice:
            print('Di quanto vuoi aumentare il prodotto?')
            aumento=int(input())
            p.carica_scorte(aumento)
## HO RISCRITTO IL CODICE DA CAPO
## DA QUA IN POI IL CODICE TORNA COME QUELLO VECCHIO CAUSA MANCANZA DI TEMPO

def stampa_prodotti():
    with open(path_file, 'r+', newline='' ) as csvfile:
        righecsv=csvfile.readlines()
        for riga in righecsv:
            print(riga)

def visualizza_prodotto():
    with open(path_file, 'r+', newline='') as csvfile:
        print("Inserisci il codice del prodotto: ")
        codice = input()
        for p in csvfile:
            if p.get_codice() == codice:
                print(p)
                return 


        
def visualizza_prodotti():
    with open(path_file, "r+", newline='') as csvfile:
        reader=csv.reader(csvfile)
        for riga in reader:
            print(riga)
