# Solicitamos al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

# Evaluamos si el número es cero
if numero == 0:
    print("El número es cero.")
else:
    # Si no es cero, evaluamos si es positivo o negativo
    if numero > 0:
        print("El número es positivo.")
    else:
        print("El número es negativo.")
    
    # Evaluamos si es par o impar
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")
