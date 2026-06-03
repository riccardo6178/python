import string
import secrets

lunghezza_massima = 24 
lunghezza_desiderata = 8
lunghezza_minima = 8
lunghezza_desiderata=int(input("Scegli la lunghezza della password(Tra 8 e 32 caratter): "))

def genera_password(digit=True, minus=True, maius=True, punct=True):
    alphabet= ""
    if digit:
        alphabet += string.digits
    if punct:
        alphabet += string.punctuation
    if minus:
        alphabet += string.ascii_lowercase
    if maius:
        alphabet += string.ascii_uppercase 
    if len(alphabet) == 0:
        print("Scegli almeno un tipo")
        return None
    if lunghezza_desiderata < 8:
        print("[WARNING] Reset lunghezza minima a 8")
        n = 8
    res = ''
    for _ in range(lunghezza_desiderata):
        res += secrets.choice(alphabet)
    if len(res) > 0:
        return res
    return None

print(genera_password(punct=True, maius=True, minus=True))


