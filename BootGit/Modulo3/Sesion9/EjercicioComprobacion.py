def calcular_area_rectangulo(base, altura):
   
    if base > 0 and altura > 0:
        area = base * altura
        return f"El área del rectángulo es: {area}"
    else:
        return "Error: La base y la altura deben ser números positivos."


base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))


print(calcular_area_rectangulo(base, altura))

