import csv
path_file = '/home/rick/Documents/python/esame/file.csv'
prodotti = []
class Prodotto:
    valore_totale = 0
    def __init__(self, nome, categoria, prezzo, quantita, codice=None):
        self.__codice = codice if codice else f"PR-{len(Prodotto.valore_totale):05d}"
        self.__nome = nome
        self.__categoria = categoria
        self.__prezzo = float(prezzo)
        self.__quantita = int(quantita)
        Prodotto.valore_totale += self.__prezzo * self.__quantita
    def __str__(self):
        return f"[{self.__codice}] {self.__nome} - {self.__categoria}\n Prezzo: {self.__prezzo:.2f} EUR | Quantita: {self.__quantita}"
    def __repr__(self):
        return self.__str__()
    def aumenta_scorte(self, aumento):
        self.__quantita += aumento
    def vendi(self, quantita):
        if quantita > self.__quantita:
            print("Quantita insufficiente!")
            return False
        self.__quantita -= quantita
        Prodotto.valore_totale -= self.__prezzo * quantita
        return True
    def get_codice(self):
        return self.__codice
    def get_nome(self):
        return self.__nome
def carica_scorte():
    prodotti.clear()
    with open(path_file, "r", newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for riga in reader:
            prodotto = Prodotto(riga[1], riga[2], riga[3], riga[4], riga[0])
            prodotti.append(prodotto)
def aggiungi_prodotto():
    print("Inserisci il nome del prodotto: ")
    nome = input()
    print("Inserisci il codice: ")
    codice = input()
    print("Inserisci la categoria: ")
    categoria = input()
    print("Inserisci il prezzo: ")
    prezzo = input()
    print("Inserisci la quantita: ")
    quantita = input()
    prodotto = Prodotto(nome, categoria, prezzo, quantita, codice)
    prodotti.append(prodotto)
def vendi_prodotto():
    print("Inserisci il codice del prodotto: ")
    codice = input()
    for p in prodotti:
        if p.get_codice() == codice:
            print(p)
            print("Quanta quantita vuoi vendere? ")
            qta = int(input())
            if p.vendi(qta):
                print("Vendita effettuata!")
            return
    print("Prodotto non trovato!")
def stampa_singolo_prodotto():
    print("Inserisci il codice del prodotto: ")
    codice = input()
    for p in prodotti:
        if p.get_codice() == codice:
            print(p)
            return
    print("Prodotto non trovato!")
def stampa_tutti_i_prodotti():
    for p in prodotti:
        print(p)
        print("-" * 30)
def stampa_valore_totale():
    print(f"Valore totale magazzino: {Prodotto.valore_totale:.2f} EUR")
def rimuovi_prodotto():
    print("Inserisci il codice del prodotto da rimuovere: ")
    codice = input()
    for p in prodotti:
        if p.get_codice() == codice:
            prodotti.remove(p)
            print("Prodotto rimosso!")
            return
    print("Prodotto non trovato!")
def salva_inventario():
    with open(path_file, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Codice", "Nome", "Categoria", "Prezzo", "Quantita"])
        for p in prodotti:
            writer.writerow([p.get_codice(), p.get_nome(), "", 0, 0])
    print("Inventario salvato!")
def menu():
    while True:
        print("-" * 10 + "MENU" + "-" * 20)
        print("""
        1) Carica scorte
        2) Vendi prodotto
        3) Stampa singolo prodotto
        4) Stampa tutti i prodotti
        5) Stampa valore totale magazzino
        6) Rimuovi prodotto
        7) Salva inventario su file
        0) Esci
        """)
        scelta = input("Scegli cosa fare: ")
        if scelta == "0":
            break
        elif scelta == "1":
            carica_scorte()
        elif scelta == "2":
            vendi_prodotto()
        elif scelta == "3":
            stampa_singolo_prodotto()
        elif scelta == "4":
            stampa_tutti_i_prodotti()
        elif scelta == "5":
            stampa_valore_totale()
        elif scelta == "6":
            rimuovi_prodotto()
        elif scelta == "7":
            salva_inventario()
        else:
            print("Scelta non valida!")


menu()