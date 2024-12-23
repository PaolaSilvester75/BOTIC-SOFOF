palabra = "paralelepípedo"
vocales = "aeiouáéíóú"

# Recorremos la palabra 
for i, letra in enumerate(palabra):
    if letra.lower() not in vocales:
        # Imprimimos la consonante y su posición
        print(f"Consonante: {letra}, Posición: {i}")
