import os
nombre_archivo = "informacion.dat"

def leer_archivo():
    if os.path.exists(nombre_archivo):
        print(f"El archivo {nombre_archivo} ya existe, ha sido creado previamente.")
        
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.readlines()
            for linea in contenido:
                print(linea.strip())
    else:
        print(f"El archivo {nombre_archivo} no existe.")

leer_archivo()
