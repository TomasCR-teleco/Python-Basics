def sensacion(t,v):
    sensacion = 13.12 + 0.6215 * t - 11.37 * v**0.16 + 0.3965 * t * v**0.16
    return sensacion
temperatura = float(input("Introduce la remepratura en grados celsius: "))
velocidad_viento = float(input("Introduce la velocidad del viento: "))
sensacion_termica = sensacion(temperatura, velocidad_viento)
print(f"La sensacion termica acorde a tus parametros es de {sensacion_termica}")