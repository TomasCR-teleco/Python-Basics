def media(l):
    suma = 0
    for x in l:
        suma += x
    m = (suma)/(len(l))
    return m

def main():
    lista = input("Introduce una lista de numeros, separados por espacios: ").split()
    lista_list = []
    for i in lista:
        lista_list.append(int(i))
    promedio = media(lista_list)
    print(f"La media de la lista es de: {promedio}")

if __name__ == '__main__': main()