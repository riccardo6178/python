class Rettangolo:
    def __init__(self, larghezza, altezza):
        self._larghezza=larghezza
        self._altezza=altezza
    @property
    def area(self):
        return self._larghezza * self._altezza

r=rettangolo(5, 3)
print(f"Area: {r.area}")
      
