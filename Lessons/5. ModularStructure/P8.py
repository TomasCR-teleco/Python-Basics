def es_primo(n):
        if n<2:
            return False
        for i in range(2,n):
            if n % i == 0:
                return False
        return True



def primos(ini,f):
    contador = 0
    for i in range (ini,f+1):
        if es_primo(i):
            contador +=1
    return contador


inicio = int(input("Introduce el inicio del rango: "))
final = int(input("Introduce el final del rango: "))
numero = int(print("Introduce el numero: "))

if es_primo(numero):
    print("Es primo")
else:
    print("No es primo")

print(primos(inicio, final))
