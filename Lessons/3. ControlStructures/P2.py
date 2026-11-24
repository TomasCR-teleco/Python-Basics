vocales = ("a","e","i","o","u")
letra = input("Introduce una letra: ")

if len(letra) != 1:
    print("Error: Debes introducir una sola letra")

if letra.lower()==letra:
    l_u = ("minuscula")
else:
    l_u = ("mayuscula")

l_min = letra.lower()
if l_min in vocales:
    print(f"Su letra es una vocal {l_u}.")
else:
    print(f"Su letra es una consonante {l_u}.")