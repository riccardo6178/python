
import csv
path_file = '/home/rick/Documents/python/esame/file.csv'
prodotti = []
class Prodotto:
    valore_totale = 0
    def __init__(self, nome, categoria, prezzo, quantità, codice='PR-00001'):
        self.__codice = codice
        self.__nome = nome
        self.__categoria = categoria
        self.__prezzo = prezzo
        self.__quantità = quantità
        Prodotto.valore_totale += self._prezzo * self._quantità
        prodotti.append(self)
    def __str__(self):
        return (f"[{self._codice}] {self._nome} - {self._categoria}\n"
                f"Prezzo: {self._prezzo:.2f} EUR | Quantità: {self._quantità}")
    def carica_scorte(self, aumento):
        if aumento < 0:
            print('Quantità non valida')
        else:
            self._quantità += aumento
            Prodotto.valore_totale += aumento * self._prezzo
    def get_nome(self):
        return self._nome
    def get_codice(self):
        return self._codice
    def vendi_prodotto(self, da_vendere):
        if self._quantità < da_vendere:
            print('Quantità insufficiente')
        else:
            self._quantità -= da_vendere
            print(f'Hai venduto {da_vendere} prodotti')
    @classmethod
    def get_valore_totale(cls):
        return cls.valore_totale
def carica_scorte_da_csv():
    print('Di che prodotto vuoi aumentare il numero?')
    codice = input()
    print('Di quanto vuoi aumentare il prodotto?')
    aumento = int(input())
    with open(path_file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for riga in reader:
            if riga['codice'] == codice:
                for p in prodotti:
                    if p.get_codice() == codice:
                        p.carica_scorte(aumento)
                        return
    print('Prodotto non trovato')
def carica_prodotti_da_csv():
    with open(path_file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for riga in reader:
            prodotto = Prodotto(
                nome=riga['nome'],
                categoria=riga['categoria'],
                prezzo=float(riga['prezzo']),
                quantità=int(riga['quantità']),
                codice=riga.get('codice', 'PR-00001')
            )
            prodotti.append(prodotto)