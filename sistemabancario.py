class Conto:
    def __init__(self, saldo, deposito, prelievo):
        self.__saldo = saldo

    def deposito(self, x):
        self.saldo += x
    
    def prelievo(self, x):
        if self.__saldo -x < 0:
            print("Mbare non hai soldi")
            return False
        self.saldo -=x
        return True 

    def get_saldo(self):
        return self.__saldo

class ContoCorrente(Conto):
    def __init__(self, perc):
        if 0 < perc < 100:
            self.perc=perc
        else:
            print("Percentuale non valida")
            self.perc=0
        
    def paga(self, x):
        commissione=x*self.perc
        a_pagare=commissione+x
        if self.prelievo(x):
            print("pagamento avvenuto con successo")


#class ContoRisparmio(Conto):
