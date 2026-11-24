### 4. Escribe un programa en Python que convierta una cantidad en millas a kilómetros.
## Usa fstrings para mostrar un mensaje de salida como el siguiente, redondeando a 2 decimales:

millas = float(input("Introduce la cantidad en millas: "))
km = millas * 1.609344
print(f"{millas} millas equivalen a {km:.2f} kilómetros")
