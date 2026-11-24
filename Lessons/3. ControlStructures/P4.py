try:
    nota = float(input("Introduce tu nota: "))
except ValueError:
    raise ValueError("Debes introducir un número válido.")
if not (0<=nota<=100):
    raise ValueError("La nota debe estar entre 0 y 100.")

if 0<=nota<=59:
    print("Tu calificación es: F")
elif 60<=nota<=69:
    print("Tu calificación es: D")
elif 70<=nota<=79:
    print("Tu calificación es: C")
elif 80<=nota<=89:
    print("Tu calificación es: B")
elif 90<=nota<=100:
    print("Tu calificación es: A")