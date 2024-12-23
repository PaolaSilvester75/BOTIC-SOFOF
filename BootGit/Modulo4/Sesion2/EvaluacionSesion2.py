class Persona:
    def __init__(self, nombre, apellidos, sexo, edad, estatura, peso):
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura
        self.peso = peso

    def get_nombre(self):
        return self.nombre

    def get_apellidos(self):
        return self.apellidos

    def get_sexo(self):
        return self.sexo

    def get_edad(self):
        return self.edad

    def get_estatura(self):
        return self.estatura

    def get_peso(self):
        return self.peso


    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellidos(self, apellidos):
        self.apellidos = apellidos

    def set_sexo(self, sexo):
        self.sexo = sexo

    def set_edad(self, edad):
        self.edad = edad

    def set_estatura(self, estatura):
        self.estatura = estatura

    def set_peso(self, peso):
        self.peso = peso

    def __str__(self):
        return (f"Nombre: {self.nombre}, Apellidos: {self.apellidos}, Sexo: {self.sexo}, "
                f"Edad: {self.edad} años, Estatura: {self.estatura} mts, Peso: {self.peso} kg")
persona_1 = Persona("Pedro", "Vivas", "Masculino", 20, 1.78, 68)
persona_2 = Persona("Juan", "Camargo", "Masculino", 18, 1.80, 75)


print("Datos iniciales de las personas:")
print(persona_1)
print(persona_2)

persona_1.set_edad(21)
persona_2.set_apellidos("Santiago")
print("\nDatos actualizados de las personas:")
print(persona_1)
print(persona_2)
