# Lista de estudiantes
estudiantes = [
    {'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]},
    {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]},
    {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]},
    {'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]},
    {'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]},
]
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Estudiantes con más de 18 años y promedio de calificaciones superior a 85:")
for estudiante in estudiantes:
    edad = estudiante['edad']
    promedio = sum(estudiante['calificaciones']) / len(estudiante['calificaciones'])
    if edad > 18 and promedio > 85:
        print(f"Nombre: {estudiante['nombre']}, Edad: {edad}, Promedio: {promedio:.2f}")

suma_promedios = 0
contador = 0
for estudiante in estudiantes:
    edad = estudiante['edad']
    if edad > 18 and es_primo(edad):
        promedio = sum(estudiante['calificaciones']) / len(estudiante['calificaciones'])
        suma_promedios += promedio
        contador += 1

if contador > 0:
    promedio_final = suma_promedios / contador
    print(f"\nPromedio de calificaciones de estudiantes con edad mayor a 18 y número primo: {promedio_final:.2f}")
else:
    print("\nNo hay estudiantes con edad mayor a 18 y número primo.")
