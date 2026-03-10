import math 

def equaz_2_grado(a,b,c):
    delta = math.sqrt(float(b*b-4*a*c))
    soluz_a = (-b + delta)/2*a
    soluz_b = (-b - delta)/2*a


    return soluz_a, soluz_b 

print(equaz_2_grado(-1, 2, 3))

