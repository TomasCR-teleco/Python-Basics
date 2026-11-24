try:
    edad = int(input("Introduce tu edad: "))
except ValueError:
    raise ValueError("Debes introducir un entero válido")
if edad<0:
    raise Exception("La edad no puede ser negativa")

if 0<=edad<=12:
    print("Eres un niño")
elif 13<=edad<=19:
    print("Eres un adolescente")
elif 20<=edad<=59:
    print("Eres un adulto")
else:
    print("Eres un mayor")