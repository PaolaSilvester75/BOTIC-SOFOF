lista_de_listas = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]
diccionario = {}

# Letras para las claves del diccionario
claves = ['A', 'B', 'C', 'D']

# Recorrer la lista de listas con excepciones
for i, sublista in enumerate(lista_de_listas):
    # Verificar si el primer número es cero, en cuyo caso se omite la sublista completa
    if sublista[0] == 0:
        continue
    
    # Filtrar los ceros en posiciones distintas de la primera posición
    sublista_filtrada = [num for num in sublista if num != 0]
    
    # Asignar la sublista filtrada a la clave correspondiente en el diccionario
    diccionario[claves[i]] = sublista_filtrada

# Imprimir las sublistas bajo sus respectivas claves
for clave, sublista in diccionario.items():
    print(f"{clave}: {sublista}")
