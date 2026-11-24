#Eliminar un elemento
a = input("Introduce un nombre:")
b = input("Introduce un nombre:")
c = input("Introduce un nombre:")

lista = [a,b,c]

print(lista)

eliminar = input("Nombre a eliminar:")
lista.remove(eliminar)

print(lista)

pos_eliminar = int(input("Posición a eliminar:"))
del lista[pos_eliminar]

print(lista)