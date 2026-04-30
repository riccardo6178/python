class Notifica:
    def __init__(self):
        self.__notifiche=[]

    #Aggiunge una notifica in cima
    def arriva(self, messaggio):
        self.__notifiche.append(messaggio)

    #Leggi ultima notifica e rimuovi
    def segna_come_letto(self):
        if self.__notifiche==[]:
            print(f'Non ci sono notifiche')
        else:
            print(f'{self.__notifiche[-1]}')
            self.__notifiche.pop()
            print(f'Notifica rimossa!')

    def prossima(self):
        return f'{self.__notifiche[-1]}'
    
    def mostra_notifiche(self):
        return f'{"\n".join(self.__notifiche)}'
    


centro_notifiche=Notifica()

centro_notifiche.arriva(f'Whatsapp: Ciao!')

centro_notifiche.arriva(f'Telegram: Prova la nuova MiniApp')
print(centro_notifiche.mostra_notifiche())

centro_notifiche.segna_come_letto()
print(centro_notifiche.mostra_notifiche())

