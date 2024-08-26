# Uso de las funciones trigonometricas en python
import math #se importa la libreria que tiene las funciones trigonometricas
#importas si pones math as mt estas importando la funcion y asignando otro nombre 
print('Calculo de las funciones trigonometricas')
print('Dame un angulo :')
angulo = int(input())
angulor = math.radians(angulo)
seno = math.sin(angulor)
coseno = math.cos(angulor)
tangente = math.tan(angulor)
grados = math.degrees(angulor)
salida=('Resumen de funciones\n'
f'El seno es {seno:.3f}\n'
f'El coseno es {coseno:.3f}\n'
f'La tangente es {tangente:.3f}\n'
f'El angulo {angulor:.3f} en radianes equivale a {grados}\n')
print ( salida)