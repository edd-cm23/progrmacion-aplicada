# clase empleado con atributos y metodos
class Empleado:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}'

# Programa principal
emp01 = Empleado('Jose Diaz', 35)
print('Nombre: ', emp01.nombre)
print('Edad : ', emp01.edad)
print(emp01)