### 2. Escribe un programa en Python que convierta una cantidad de horas en días y horas.
### Usa fstrings para formatear la salida.

horas = int(input("Introduce la cantidad de horas: "))
dias = horas // 24
horas_restantes = horas % 24
print(f"{dias} días y {horas_restantes} horas.")