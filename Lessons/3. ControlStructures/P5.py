try:
    a = int(input("Introduce el primer lado: "))
    b = int(input("Introduce el segundo lado: "))
    c = int(input("Introduce el tercer lado: "))
except ValueError:
    raise ValueError("Debes introducir números enteros válidos")
if a<=0 or b<=0 or c<=0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
    raise ValueError("Los lados no forman un triángulo válido")

if a==b==c:
    print("El triángulo es equilátero")
elif a==b or b==c or a==c:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")