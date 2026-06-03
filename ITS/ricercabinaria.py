def ricercabinaria(arr, num):
    inf, sup = 0, len(arr)-1
    while inf<sup:
        m=round((inf+sup)/2)
        if arr[m]==num:
            return m
        if arr[m] < num:
            inf = m+1
        else:
            sup=m-1
    return -1
    



print(ricercabinaria([1,2,3,4,2,3,4,1,2,3,4,5,32,3,5,4,3,23,3,5,6,6,21,2,34,5,4], 21))