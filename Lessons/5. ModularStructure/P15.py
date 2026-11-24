from P14 import media

def main():
    lista = input("Introduce una lista de numeros, separados por espacios: ").split()
    lista_int = []
    for i in lista:
        lista_int.append(int(i))
    promedio = media(lista_int)
    mayor_igual_media = []
    for x in lista_int:
        if x >= promedio:
            mayor_igual_media.append(x)
    cantidad_MayIgual_media = len(mayor_igual_media)
    print(f"En la lista proporcionada por el usuario hay estos numeros mayores o iguales a la media: {cantidad_MayIgual_media}")
    
if __name__ == '__main__': main()