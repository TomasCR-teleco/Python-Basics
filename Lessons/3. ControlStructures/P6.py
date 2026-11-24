try:
    a = int(input("Introduce un año: "))
    
    if (a%4 == 0) and (not(a%100 == 0) or (a%400 == 0)):
        print("Es un año bisiesto.")
    else:
        print("No es un año bisiesto.")
except ValueError:
    raise ValueError("Debes introducir un entero válido.")