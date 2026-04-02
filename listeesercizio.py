from functools import reduce

numbers=[1, 2, 3, 4, 5, 6, 7] 
def custom_sum(first, second):
    return first + second 
result=reduce(custom_sum, numbers, 0)
print(result)
indice=int(input(f"Inserisci l'indice(numeri validi da 1 a {len(numbers)})"))
valore=int(input("Inserisci il valaore: "))
numbers.insert(indice, valore)
print(numbers)

