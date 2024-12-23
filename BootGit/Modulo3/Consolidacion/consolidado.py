# Lista de nombres
nombres = [
    "Harry Houdini", "Newton", "David Blaine", "Hawking", 
    "Messi", "Teller", "Einstein", "Pele", "Juanes"
]
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]
otros = [nombre for nombre in nombres if nombre not in magos and nombre not in cientificos]

def hacer_grandioso(lista_magos):
    for i in range(len(lista_magos)):
        lista_magos[i] = "El gran " + lista_magos[i]


def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)

print("Lista completa de nombres antes de ser modificados:")
imprimir_nombres(nombres)
print()
hacer_grandioso(magos)

print("Nombres de los magos grandiosos:")
imprimir_nombres(magos)
print()

print("Nombres de los científicos:")
imprimir_nombres(cientificos)
print()

print("Nombres restantes:")
imprimir_nombres(otros)
