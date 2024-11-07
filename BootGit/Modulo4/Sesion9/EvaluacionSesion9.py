nombre_archivo = "informacion.dat"

def reemplazar_informacion():

    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
    
    nuevo_contenido, num_reemplazos = contenido.replace("Información", "Procesamiento"), contenido.count("Información")

    with open(nombre_archivo, 'w') as archivo:
        archivo.write(nuevo_contenido)

    print(f"Se realizaron {num_reemplazos} reemplazos")

reemplazar_informacion()

with open(nombre_archivo, 'r') as archivo:
    print(archivo.read())
