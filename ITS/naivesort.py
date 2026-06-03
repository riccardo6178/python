from random import randint

def bubblesort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
# ── Esempio d'uso ──
if __name__ == "__main__":
    parole = ["banana", "mela", "arancia", "kiwi", "fragola"]
    print(f"Prima: {parole}")
    bubblesort(parole)  
    print(f"Dopo:  {parole}")
    # Test con numeri
    numeri = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nNumeri prima: {numeri}")
    bubblesort(numeri)
    print(f"Numeri dopo:  {numeri}")

numero=list(map(int,(randint(1,100) for i in range (0,4))))
print(numero)