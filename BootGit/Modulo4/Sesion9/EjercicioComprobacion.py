nombre_archivo = "informacion.dat"
contenido_a_agregar = """\
Este en una nueva línea en el archivo
agregando la segunda línea del archivo
finalizando la línea agregada
"""

with open(nombre_archivo, 'a') as archivo:
    archivo.write(contenido_a_agregar)

with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.read()
    print(contenido)
