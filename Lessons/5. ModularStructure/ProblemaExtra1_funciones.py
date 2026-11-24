def sumaLista(l):
    suma = 0
    for i in l:
        suma += i
    return suma

def mayorLista(l):
    mayor = 0
    for i in l:
        if i > mayor:
            mayor = i
    return mayor
    
def terceroLista(l):
    pasos = [1,2,3]
    for 