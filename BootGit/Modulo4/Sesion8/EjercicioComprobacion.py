import os
nombre_archivo = "informacion.dat"

if os.path.exists(nombre_archivo):
    print(f"El archivo '{nombre_archivo}' ya se encuentra creado.")
else:

    with open(nombre_archivo, 'w') as archivo:
        for i in range(1, 6):
            archivo.write(f"Datos de información en la línea {i}\n")
    print(f"El archivo '{nombre_archivo}' ha sido creado exitosamente.")
