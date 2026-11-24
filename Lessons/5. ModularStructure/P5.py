def minimo(n1,n2):
    if n1<n2:
        minimo=n1
    else:
        minimo=n2
    return minimo

numero1 = int(input("inrtoduce el primer numero: "))
numero2 = int(input("inrtoduce el segundoi numero: "))
minimo = minimo(numero1,numero2)
print(f"El minimo es {minimo}")