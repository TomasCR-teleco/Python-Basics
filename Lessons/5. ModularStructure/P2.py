def nombre_cordialidad(n,c):
    if c == 1:
        print(f"Hola {n}")
    elif c == 2:
        print(f"Hola, {n}, espero que estes bien")
    else:
        print(f"Querido {n}, te envio un cordial saludo")
        
nombre = input("Dime tu nombre: ")
cordialidad = int(input("Dime el nivel de cordialidad: "))
nombre_cordialidad(nombre,cordialidad)