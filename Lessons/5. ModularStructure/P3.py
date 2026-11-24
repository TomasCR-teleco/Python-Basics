def flecha(t):
    flecha = (t-1)*"-"+">"
    return flecha

tamano = int(input("Tamano de la felcha:"))
flecha = flecha(tamano)
print(flecha)