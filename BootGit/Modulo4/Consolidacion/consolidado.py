import csv

class Vehiculo:
    def __init__(self, marca, modelo, num_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Número de ruedas: {self.num_ruedas}"

    def guardar_datos_csv(self, archivo):
        with open(archivo, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.__class__.__name__, self.marca, self.modelo, self.num_ruedas])


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, num_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"{super().__str__()}, Velocidad: {self.velocidad} km/h, Cilindrada: {self.cilindrada} cc"

    def guardar_datos_csv(self, archivo):
        with open(archivo, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.__class__.__name__, self.marca, self.modelo, self.num_ruedas, self.velocidad, self.cilindrada])


class Particular(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, num_puestos):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.num_puestos = num_puestos

    def __str__(self):
        return f"{super().__str__()}, Número de puestos: {self.num_puestos}"

    def guardar_datos_csv(self, archivo):
        with open(archivo, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.__class__.__name__, self.marca, self.modelo, self.num_ruedas, self.velocidad, self.cilindrada, self.num_puestos])


class Carga(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga

    def __str__(self):
        return f"{super().__str__()}, Peso de carga: {self.peso_carga} kg"

    def guardar_datos_csv(self, archivo):
        with open(archivo, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.__class__.__name__, self.marca, self.modelo, self.num_ruedas, self.velocidad, self.cilindrada, self.peso_carga])


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, tipo_bicicleta):
        super().__init__(marca, modelo, num_ruedas)
        self.tipo_bicicleta = tipo_bicicleta

    def __str__(self):
        return f"{super().__str__()}, Tipo de bicicleta: {self.tipo_bicicleta}"

    def guardar_datos_csv(self, archivo):
        with open(archivo, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.__class__.__name__, self.marca, self.modelo, self.num_ruedas, self.tipo_bicicleta])


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, num_ruedas, tipo_bicicleta, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, num_ruedas, tipo_bicicleta)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor

    def __str__(self):
        return f"{super().__str__()}, Número de radios: {self.nro_radios}, Cuadro: {self.cuadro}, Motor: {self.motor}"

    def guardar_datos_csv(self, archivo):
        with open(archivo, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.__class__.__name__, self.marca, self.modelo, self.num_ruedas, self.tipo_bicicleta, self.nro_radios, self.cuadro, self.motor])


def leer_datos_csv(archivo):
    vehiculos = []
    with open(archivo, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            vehiculos.append(row)
    return vehiculos


def main():
    archivo_csv = 'vehiculos.csv'

    particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
    carga = Carga("Caterpillar", "CAT 600", 10, 120, 1000, 20000)
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("Yamaha", "YZF R1", 2, "Deportiva", 21, "Doble Viga", "998 cc")
    particular.guardar_datos_csv(archivo_csv)
    carga.guardar_datos_csv(archivo_csv)
    bicicleta.guardar_datos_csv(archivo_csv)
    motocicleta.guardar_datos_csv(archivo_csv)
    print("\nDatos recuperados del archivo CSV:")
    vehiculos = leer_datos_csv(archivo_csv)


if __name__ == "__main__":
    main()
