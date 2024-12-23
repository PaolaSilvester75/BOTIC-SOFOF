while True:
    try:
        edad = int(input("Por favor, ingrese su edad: "))
        break
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")
        
if edad >= 18:
    print("Es Adulto.")
else:
    print("No es un adulto.")
