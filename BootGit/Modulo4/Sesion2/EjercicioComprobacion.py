class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso

    def __str__(self):
        return f"Nombre: {self.nombre}, Raza: {self.raza}, Edad: {self.edad} años, Peso: {self.peso} kg"

caballo = Animal("Zeus", "Pura sangre", 5, 450)
leon = Animal("Boulder", "Atlas", 10, 130)

print("Detalles del Caballo:")
print(caballo)
print("\nDetalles del León:")
print(leon)
