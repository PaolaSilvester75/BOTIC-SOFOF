# Creamos una lista con 10 números enteros
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Recorremos la lista con un bucle for
for numero in numeros:
    if numero == 0:
        print(f"El número {numero} es cero.")
    elif numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")
