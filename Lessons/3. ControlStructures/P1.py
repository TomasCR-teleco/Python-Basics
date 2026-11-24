try:
    i = int(input("Introduce un entero: "))
    if i==0:
        print("Su entero es zero")
    elif i<0:
        print("Su entero es negativo")
    else:
        print("Su entero es positivo")
except Exception:
    raise Exception("No ha introducido un entero")
    print("Error: Debes introducir un número entero")