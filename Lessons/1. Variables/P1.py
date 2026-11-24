###1. Escribe una instrucción en Python que asigne a una variable la media aritmética de tres
###números enteros (a, b y c).

print("A continuación introduce los 3 reales")
a = float(input("Introduce a:"))
b = float(input("Introduce b:"))
c = float(input("Introduce c:"))

suma_abc = a + b + c
media_aritmetica = suma_abc / 3

print(media_aritmetica)