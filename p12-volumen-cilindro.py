#volumen de un cilindro 

import os ; os.system("cls")

radio = float(input('¿cual es el radio del circulo en el cilindro?'))
altura = float(input('¿que altura tiene el cilindro?'))

import math

print(f'el area del cilindro es: {math.pi * pow(radio,2) * altura:.2f}')