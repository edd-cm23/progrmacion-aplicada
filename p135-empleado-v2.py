# clase empleado con atributos y metodos
# ampliamos la clase
class Empleado:
    def __init__(self, nombre, edad, sexo, casado):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.casado = casado
    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Sexo:{"Mujer" if self.sexo=="M"
    else "Hombre"} Casado : {"Casad@" if self.casado else "No Casado"}'

# Programa principal
emp01 = Empleado('Jose Diaz', 35, 'H', True)
print('Nombre: ', emp01.nombre)
print('Edad : ', emp01.edad)
print('Sexo : ', emp01.sexo)
print('Casado: ', emp01.casado)
print(emp01)

emp02 = Empleado('Jose Diaz', 35, 'H', True)
print('Nombre: ', emp01.nombre)
print('Edad : ', emp01.edad)
print('Sexo : ', emp01.sexo)
print('Casado: ', emp01.casado)
print(emp01)

emp03 = Empleado('Jose Diaz', 35, 'H', True)
print(emp01)

pedad = (emp01.edad + emp02.edad + emp03.edad) / 3
print(f'promedio edad de 3 empleados: {pedad}')