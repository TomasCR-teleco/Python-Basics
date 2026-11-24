###Crea un programa que pida al usuario una frase de al menos 4 palabras
###separadas por comas (el programa debe funcionar para cualquier número de
###palabras igual o superior a 4). Luego:
###• Separa la frase en una lista de palabras.
###• Crea una nueva lista con solo las tres últimas palabras en mayúsculas.
###• Une las palabras modificadas en una sola cadena, separadas por guiones
###(-).
###• Muestra las listas y la frase transformada en la consola con el siguiente

lista_original = input("Introduce una frase de al menos 4 palabras separadas por comas: ")

lista_palabras = lista_original.split(",")
print(lista_palabras)
lista_modificada = [lista_palabras[len(lista_palabras)-3].upper(), lista_palabras[len(lista_palabras)-2].upper(), lista_palabras[len(lista_palabras)-1].upper()]
print(lista_modificada)
cadena_guiones = "-".join(lista_modificada)
print(cadena_guiones)