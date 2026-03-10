import random
numero = random.randint(1, 100)
print("Indovina il numero!: ")
risposta = 0
counter = 0

while risposta != numero:
    risposta = int(input())
    counter += 1
    
    if risposta < numero:
        print("Il numero è troppo basso")
    elif risposta > numero:
        print("Il numero è troppo alto")

print("Bravo! Hai indovinato!")
print(f"Hai impiegato {counter} tentativi")
