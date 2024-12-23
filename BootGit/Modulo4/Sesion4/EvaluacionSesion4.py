class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def movimiento(self):
        return f"{self.nombre} está caminando."

class Maratonista(Persona):
    def movimiento(self):
        return f"{self.nombre} está trotando."

class Ciclista(Persona):
    def movimiento(self):
        return f"{self.nombre} está rodando."

persona = Persona("Juan")
maratonista = Maratonista("Carlos")
ciclista = Ciclista("Ana")
print(persona.movimiento()) 
print(maratonista.movimiento())
print(ciclista.movimiento())  
