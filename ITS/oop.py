class Cerchio:
        def __init__(self, raggio):
            self.raggio=raggio

        def area(self):
            return self.raggio*self.raggio*3.14

        def perimetro(self):
            return 2*3.14*self.raggio
c=Cerchio(12)
print(c.area())
print(f"Raggio: {c.raggio}")
print(f"perimetro: {c.perimetro()}")
print(c)
