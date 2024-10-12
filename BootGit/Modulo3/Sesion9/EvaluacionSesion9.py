def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero."

def operaciones(a, b):
    suma = sumar(a, b)
    resta = restar(a, b)
    multiplicacion = multiplicar(a, b)
    division = dividir(a, b)
    return (suma, resta, multiplicacion, division)

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

resultados = operaciones(num1, num2)

diccionario_resultados = {
    "Suma": resultados[0],
    "Resta": resultados[1],
    "Multiplicación": resultados[2],
    "División": resultados[3]
}

print("Resultados de las operaciones:")
for clave, valor in diccionario_resultados.items():
    print(f"{clave}: {valor}")
