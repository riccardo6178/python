class Rettangolo:
    def __init__(self, base, altezza):
        self.__base=base
        self.__altezza=altezza 

    def altezza(self):
        return self.__altezza
    #permette di rendere l attributo privato nona cessibile dall'esterno ce lo rende stampabile 
    #potrebbe avre senso scrivere il getter come property
    # i setter e i getter esternalizzano gli attributi delle classi 
    #in alternativa si puo scrivere su c++:
    class Rettangolo{
        public: 
            Rettangolo(base, altezza)
            base=base 
            aletzza=altezza 
        private:
            float base;
            float altezza; 
        protected:
    
    class DRettangolo(Rettangolo)


    }
            
    
    @property
    def area(self):
        return self.__altezza * self.__base
    # glia ttributi privatre e protected non sono modificabilida fuori e non possiamo manco farceli ritornare 
    #  i setter e i getter servono a far ritornare i valori di cui necessitiamo 