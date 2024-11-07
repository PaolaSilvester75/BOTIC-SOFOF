class RangoSalarioError(Exception):
    def __init__(self, salario):
        self.salario = salario
        super().__init__(self._mensaje())

    def _mensaje(self):
        return f"{self.salario} -> Salario no está definido en el rango (1000 a 2000)"

def ingresar_salario():
    try:
        salario = int(input("Ingrese el salario: "))
        if salario < 1000 or salario > 2000:
            raise RangoSalarioError(salario)
        print(f"El salario ingresado es: {salario}")
    except RangoSalarioError as e:
        print(e)
        
ingresar_salario()
