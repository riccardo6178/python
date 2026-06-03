import csv
path_file='/home/rick/Documents/python/esame/file.csv'
prodotti=[]


class Prodotto: 
    valore_totale=0
    def __init__(self, __codice,__nome, __categoria, __prezzo, __quantità):
        self.__codice=__codice
        self.__nome=__nome
        self.__categoria=__categoria
        self.__prezzo=__prezzo
        self.__quantità=__quantità
        valore_totale=(self.__prezzo * self.__quantità)+Prodotto.valore_totale

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

def stampa_prodotti():
    with open(path_file, 'r+', newline='' ) as csvfile:
        righecsv=csvfile.readlines()
        for riga in righecsv:
            print(riga)


def carica_scorte():
    print('Di quanto vuoi aumentare il prodotto?')
    aumento=int(input())
